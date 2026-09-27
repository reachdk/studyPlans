#!/usr/bin/env python3
"""
Study Portal Distribution Packager.
Assembles a lean, clean Google Drive distribution bundle:
- Compiled dashboard HTML
- Only the specific NCERT PDFs referenced by the active chapters
- Markdown revision notes
- Zero developer scripts, zero virtual environments, zero tokens/profiles.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

def package_bundle(subject_id: str, output_dir: Path):
    subject_dir = ROOT / "subjects" / subject_id
    if not subject_dir.exists():
        print(f"❌ Error: Subject directory not found: {subject_dir}")
        sys.exit(1)

    manifest_path = subject_dir / "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # 1. Compile or find dashboard HTML
    dashboard_filename = f"study_{manifest['id']}_dashboard.html"
    dashboard_file = ROOT / dashboard_filename

    # Always ensure it is built
    from portal_engine.builder import build_portal
    print(f"🔨 Compiling latest {dashboard_filename}...")
    dashboard_file = build_portal(manifest['id'], dashboard_file)

    # 2. Prepare output directory
    output_dir = output_dir.resolve()
    print(f"\n📦 Packaging clean distribution bundle to: {output_dir}")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 3. Copy Dashboard HTML
    shutil.copy2(dashboard_file, output_dir / dashboard_filename)
    print(f"  ✅ Copied: {dashboard_filename} ({dashboard_file.stat().st_size / 1024:.1f} KB)")

    # 4. Copy ONLY referenced NCERT PDFs
    chapters_dir = subject_dir / "chapters"
    copied_pdfs = 0
    for ch_info in manifest.get("chapters", []):
        meta_file = chapters_dir / ch_info["folder"] / "meta.json"
        if meta_file.exists():
            with open(meta_file, "r", encoding="utf-8") as mf:
                meta = json.load(mf)
            pdf_rel = meta.get("pdf")
            if pdf_rel:
                src_pdf = ROOT / pdf_rel
                if src_pdf.exists():
                    dst_pdf = output_dir / pdf_rel
                    dst_pdf.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_pdf, dst_pdf)
                    copied_pdfs += 1

    print(f"  ✅ Copied: {copied_pdfs} referenced NCERT PDFs")

    # 5. Copy raw markdown notes if present
    notes_src = ROOT / "notes" / subject_id
    if notes_src.exists():
        notes_dst = output_dir / "notes" / subject_id
        notes_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(notes_src, notes_dst)
        print(f"  ✅ Copied: Markdown revision notes ({subject_id})")

    # 6. Calculate total package size
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*") if f.is_file())
    total_mb = total_size / (1024 * 1024)

    print(f"\n✨ Distribution Bundle Ready!")
    print(f"📁 Location: {output_dir}")
    print(f"📊 Total Size: {total_mb:.1f} MB (vs 1.5 GB repository)")
    print(f"🚀 Ready to drop directly into Google Drive for the kids.\n")

def main():
    parser = argparse.ArgumentParser(description="Study Portal Packager")
    parser.add_argument("--subject", required=True, help="Subject ID (e.g. mathematics, science)")
    parser.add_argument("--output", help="Destination folder (defaults to dist/<subject>_portal)")
    args = parser.parse_args()

    out_path = Path(args.output) if args.output else ROOT / "dist" / f"{args.subject}_study_portal"
    package_bundle(args.subject, out_path)

if __name__ == "__main__":
    main()
