#!/usr/bin/env python3
"""Sync teacher-posted Google Classroom materials to local NotebookLM sources."""

import argparse
import csv
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = ROOT / "downloads" / "classroom"
TOKEN = ROOT / ".classroom-token.json"
SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
    "https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly",
    "https://www.googleapis.com/auth/classroom.announcements.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]
# Explicitly exclude similarly named advanced/elective and PE classes.
EXCLUDE = re.compile(r"\b(advanced|advance|additional|further|physical education|p\.?e\.?)\b", re.I)
INCLUDE = re.compile(
    r"\b(math(?:s|ematics)?|english|social[ -]?science|physics|chem(?:istry)?|bio(?:logy)?|"
    r"german|information[ -]?technology|computer[ -]?applications|\bIT\b)\b", re.I
)
EXPORT = {
    "application/vnd.google-apps.document": ("application/pdf", ".pdf"),
    "application/vnd.google-apps.presentation": ("application/pdf", ".pdf"),
    "application/vnd.google-apps.spreadsheet": ("application/pdf", ".pdf"),
    "application/vnd.google-apps.drawing": ("application/pdf", ".pdf"),
}
# NotebookLM accepts PDFs, plain text, audio and common image formats; keep other
# attachments too, so that nothing shared by a teacher silently disappears.


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:70] or "untitled"


def clean_subject(course_name):
    c = (course_name or "").lower()
    if "chem" in c:
        return "chemistry"
    if "bio" in c:
        return "biology"
    if "physic" in c:
        return "physics"
    if "math" in c:
        return "mathematics"
    if "social" in c:
        return "social-science"
    if "english" in c:
        return "english"
    if "it" in c or "402" in c:
        return "information-technology"
    if "german" in c:
        return "german"
    return slug(course_name)


def is_9a_only(label):
    return bool(re.search(r"\b(?:g(?:rade)?[- ]*)?9a\b", label, re.I)
                and not re.search(r"\b(?:g(?:rade)?[- ]*)?9b\b|\b9a\s*(?:&|and|\+)\s*9b\b|\ba\s*(?:&|and|\+)\s*b\b", label, re.I))


def selected(course):
    label = f"{course.get('name', '')} {course.get('section', '')}"
    return bool(INCLUDE.search(label) and not EXCLUDE.search(label) and not is_9a_only(label))


def pages(request_factory, key):
    token = None
    while True:
        response = request_factory(pageToken=token).execute()
        yield from response.get(key, [])
        token = response.get("nextPageToken")
        if not token:
            break


def services(client_secrets):
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise SystemExit("Install dependencies: .venv/bin/python -m pip install -r requirements-classroom.txt") from exc
    if not client_secrets.is_file():
        raise SystemExit(f"Missing OAuth Desktop app credentials: {client_secrets}")
    credentials = None
    if TOKEN.exists():
        credentials = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
        if not credentials.has_scopes(SCOPES):
            credentials = None
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secrets), SCOPES)
            credentials = flow.run_local_server(port=0, open_browser=True)
        TOKEN.write_text(credentials.to_json())
        os.chmod(TOKEN, 0o600)
    return (build("classroom", "v1", credentials=credentials, cache_discovery=False),
            build("drive", "v3", credentials=credentials, cache_discovery=False))


def posts(classroom, course_id):
    for resource, key in ((classroom.courses().courseWorkMaterials(), "courseWorkMaterial"),
                          (classroom.courses().courseWork(), "courseWork"),
                          (classroom.courses().announcements(), "announcements")):
        for post in pages(lambda **kw: resource.list(courseId=course_id, pageSize=100, **kw), key):
            yield key, post


def attachment_rows(classroom, courses):
    for course in courses:
        course_id = course["id"]
        folder = clean_subject(course.get("name", "class"))
        for kind, post in posts(classroom, course_id):
            for material in post.get("materials", []):
                drive_file = material.get("driveFile", {}).get("driveFile", {})
                base = {"course": course.get("name"), "course_id": course_id,
                        "post_type": kind, "post_id": post.get("id"),
                        "post_title": post.get("title") or "(untitled)",
                        "post_created": post.get("creationTime"),
                        "post_updated": post.get("updateTime") or post.get("creationTime")}
                if drive_file.get("id"):
                    yield {**base, "type": "drive", "file_id": drive_file["id"],
                           "attachment_name": drive_file.get("title"), "folder": folder}
                elif "link" in material:
                    yield {**base, "type": "link", "url": material["link"].get("url"),
                           "attachment_name": material["link"].get("title")}
                elif "youtubeVideo" in material:
                    video = material["youtubeVideo"]
                    yield {**base, "type": "youtube", "url": video.get("alternateLink"),
                           "attachment_name": video.get("title")}
                elif "form" in material:
                    yield {**base, "type": "form", "url": material["form"].get("formUrl")}


def download(drive, file_id, target, export_mime=None):
    from googleapiclient.http import MediaIoBaseDownload
    request = (drive.files().export_media(fileId=file_id, mimeType=export_mime) if export_mime
               else drive.files().get_media(fileId=file_id, supportsAllDrives=True))
    target.parent.mkdir(parents=True, exist_ok=True)
    # Partial downloads never appear as valid sources.
    fd, temp = tempfile.mkstemp(prefix=".partial-", dir=target.parent)
    try:
        with os.fdopen(fd, "wb") as output:
            downloader = MediaIoBaseDownload(output, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()
        os.replace(temp, target)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def write_source_indexes(output, payload):
    by_file = {}
    for file_id, info in payload["files"].items():
        by_file[file_id] = {**info, "posts": []}
    links = []
    for row in payload["attachments"]:
        if row["type"] == "drive" and row.get("file_id") in by_file:
            by_file[row["file_id"]]["posts"].append(row)
        elif row["type"] != "drive":
            links.append(row)

    csv_path = output / "sources.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=[
            "course", "subject", "post_title", "post_type", "post_created", "post_updated", "attachment_name",
            "local_path", "mime_type", "drive_file_id", "version",
        ])
        writer.writeheader()
        for file_id, info in sorted(by_file.items(), key=lambda item: item[1].get("path", "")):
            posts = info["posts"] or [{}]
            for post in posts:
                writer.writerow({
                    "course": post.get("course", ""),
                    "subject": Path(info.get("path", "")).parent.name,
                    "post_title": post.get("post_title", ""),
                    "post_type": post.get("post_type", ""),
                    "post_created": post.get("post_created", ""),
                    "post_updated": post.get("post_updated", ""),
                    "attachment_name": post.get("attachment_name") or info.get("name", ""),
                    "local_path": info.get("path", ""),
                    "mime_type": info.get("mimeType", ""),
                    "drive_file_id": file_id,
                    "version": info.get("version", ""),
                })

    md_path = output / "SOURCES.md"
    generated_ts = payload.get("generated_at") or datetime.now(timezone.utc).isoformat()
    lines = [
        "# Google Classroom source index",
        "",
        f"Generated: {generated_ts}",
        f"Files: {len(payload['files'])}",
        f"External/non-Drive attachments: {len(links)}",
        f"Errors: {len(payload['errors'])}",
        "",
        "Use `sources.csv` for structured filtering. Upload only the needed files listed below to NotebookLM; do not upload `manifest.json` unless you intentionally want post metadata included.",
        "",
    ]
    current_subject = None
    for file_id, info in sorted(by_file.items(), key=lambda item: item[1].get("path", "")):
        posts = info["posts"] or [{}]
        subject = Path(info.get("path", "")).parent.name
        course = posts[0].get("course", "Unknown class")
        header = f"{subject.replace('-', ' ').title()} ({course})" if subject else course
        if header != current_subject:
            current_subject = header
            lines += [f"## {header}", ""]
        post_titles = sorted({p.get("post_title", "") for p in posts if p.get("post_title")})
        lines.append(f"- `{info.get('path', '')}`")
        lines.append(f"  - Name: {info.get('name', '')}")
        lines.append(f"  - Type: {info.get('mimeType', '')}")
        lines.append(f"  - Drive file ID: `{file_id}`")
        dates = sorted({p.get("post_created") or p.get("post_updated", "") for p in posts if p.get("post_created") or p.get("post_updated")})
        if dates:
            lines.append(f"  - Classroom posted: {', '.join(dates)}")
        if post_titles:
            lines.append(f"  - Classroom post(s): {', '.join(post_titles)}")
    if links:
        lines += ["", "## External links / videos / forms listed but not downloaded", ""]
        for row in links:
            lines.append(f"- {row.get('course', '')}: {row.get('attachment_name') or row.get('url', '')} — {row.get('url', '')}")
    if payload["errors"]:
        lines += ["", "## Errors", ""]
        for error in payload["errors"]:
            lines.append(f"- `{error.get('file_id')}`: {error.get('error')}")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"indexes: {md_path}, {csv_path}")


def sync(drive, rows, output):
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "manifest.json"
    old = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    previous = old.get("files", {})
    files, entries, errors = {}, [], []
    used_relatives = set()
    for row in rows:
        if row["type"] != "drive":
            entries.append(row)
            continue
        file_id = row["file_id"]
        if file_id in files:
            entries.append(row)
            continue
        try:
            meta = drive.files().get(fileId=file_id, fields="id,name,mimeType,modifiedTime,size",
                                     supportsAllDrives=True).execute()
            mime = meta.get("mimeType", "")
            export_mime, extension = EXPORT.get(mime, (None, ""))
            if mime.startswith("application/vnd.google-apps.") and not export_mime:
                raise ValueError(f"Unsupported Google file type: {mime}")
            name = meta.get("name", row.get("attachment_name") or "file")
            if not extension:
                extension = Path(name).suffix.lower()

            folder = row.get("folder") or clean_subject(row.get("course", "general"))
            post_date = (row.get("post_created") or row.get("post_updated") or "")[:10]
            date_prefix = f"{post_date}_" if post_date and re.match(r"^\d{4}-\d{2}-\d{2}$", post_date) else ""
            stem = slug(Path(name).stem)

            prev_path = previous.get(file_id, {}).get("path")
            if prev_path and (output / prev_path).is_file():
                relative = prev_path
            else:
                candidate = f"{date_prefix}{stem}{extension}"
                candidate_rel = str(Path(folder) / candidate)
                if candidate_rel in used_relatives or ((output / candidate_rel).exists() and previous.get(file_id, {}).get("path") != candidate_rel):
                    candidate = f"{date_prefix}{stem}_{file_id[:6]}{extension}"
                    candidate_rel = str(Path(folder) / candidate)
                relative = candidate_rel

            used_relatives.add(relative)
            target = output / relative
            version = meta.get("modifiedTime", "") + ":" + meta.get("size", "")
            if previous.get(file_id, {}).get("version") != version or not target.is_file():
                download(drive, file_id, target, export_mime)
                ts_str = row.get("post_created") or row.get("post_updated")
                if ts_str:
                    try:
                        dt = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                        epoch = dt.timestamp()
                        os.utime(target, (epoch, epoch))
                    except Exception:
                        pass
                print(f"Downloaded: {relative}")
            files[file_id] = {"path": relative, "version": version, "name": name, "mimeType": mime}
        except Exception as exc:
            errors.append({"file_id": file_id, "error": str(exc)})
            print(f"Could not download {file_id}: {exc}")
        entries.append(row)
    payload = {"generated_at": datetime.now(timezone.utc).isoformat(),
               "files": files, "attachments": entries, "errors": errors}
    fd, temp = tempfile.mkstemp(prefix=".manifest-", dir=output)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(payload, stream, indent=2, ensure_ascii=False)
        os.replace(temp, manifest_path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)
    write_source_indexes(output, payload)
    print(f"{len(files)} files; {len(errors)} errors; manifest: {manifest_path}")
    return not errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--credentials", type=Path, default=ROOT / "classroom-credentials.json")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--list", action="store_true", help="List courses without downloading")
    parser.add_argument("--course", action="append", default=[], metavar="ID",
                        help="Explicit course ID to include (repeatable); overrides subject filter")
    args = parser.parse_args()
    classroom, drive = services(args.credentials)
    courses = list(pages(lambda **kw: classroom.courses().list(courseStates=["ACTIVE"],
                                                            pageSize=100, **kw), "courses"))
    print("Active classes (* = selected):")
    for course in courses:
        mark = "*" if (course["id"] in args.course if args.course else selected(course)) else " "
        print(f" {mark} {course.get('name')} — {course.get('section', '')} [{course['id']}]")
    if args.list:
        return
    unknown = set(args.course) - {course["id"] for course in courses}
    if unknown:
        raise SystemExit(f"Unknown or inactive course IDs: {', '.join(sorted(unknown))}")
    chosen = [c for c in courses if (c["id"] in args.course if args.course else selected(c))]
    if not chosen:
        raise SystemExit("No matching classes. Use --course ID to select specific classes.")
    if input(f"Sync materials from {len(chosen)} selected classes? [y/N] ").strip().lower() != "y":
        return
    if not sync(drive, attachment_rows(classroom, chosen), args.output):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
