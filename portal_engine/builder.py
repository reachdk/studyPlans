#!/usr/bin/env python3
"""
Study Portal Compiler:
Compiles structured subject folders (Markdown guides, JSON flashcards & questions)
with portal_engine/template.html into a 100% self-contained, offline-ready HTML dashboard.
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "portal_engine" / "template.html"

def markdown_to_html(md_text: str) -> str:
    """Converts guide markdown into styled HTML with progressive disclosure accordions, tables and callout boxes."""
    lines = md_text.strip().split("\n")
    html_lines = []
    in_table = False
    table_header_done = False
    in_quote = False
    quote_lines = []
    in_accordion = False
    accordion_count = 0

    def close_accordion():
        nonlocal in_accordion
        if in_accordion:
            html_lines.append('  </div>') # close .accordion-body
            html_lines.append('</div>')     # close .concept-accordion
            in_accordion = False

    def flush_quote():
        nonlocal in_quote, quote_lines
        if quote_lines:
            content = " ".join(quote_lines).strip()
            if "Teacher" in content or "Overview" in content or "👨‍🏫" in content:
                html_lines.append(f'<div class="teacher-quote">{content}</div>')
            elif "Warning" in content or "Trap" in content or "⚠️" in content:
                html_lines.append(f'<div class="callout-box warning">{content}</div>')
            else:
                html_lines.append(f'<div class="callout-box tip">{content}</div>')
            quote_lines = []
            in_quote = False

    has_sections = any(l.strip().startswith("### ") or l.strip().startswith("## ") for l in lines)
    toolbar_added = False

    for line in lines:
        stripped = line.strip()

        # If it is a divider line, ignore
        if stripped in ("---", "***", "___"):
            continue

        # Handle blockquotes
        if stripped.startswith(">"):
            in_quote = True
            quote_content = stripped.lstrip("> ").strip()
            quote_content = re.sub(r'\[!(?:TIP|NOTE)\]', '💡 <strong>Key Takeaway:</strong>', quote_content, flags=re.I)
            quote_content = re.sub(r'\[!WARNING\]', '⚠️ <strong>Exam Trap:</strong>', quote_content, flags=re.I)
            quote_lines.append(quote_content)
            continue
        elif in_quote:
            flush_quote()

        # Handle Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                table_header_done = True
                continue

            if not in_table:
                in_table = True
                table_header_done = False
                html_lines.append('<table class="diff-table">')

            tag = "th" if not table_header_done else "td"
            row_html = "".join(f"<{tag}>{c}</{tag}>" for c in cells)
            html_lines.append(f"  <tr>{row_html}</tr>")
            continue
        elif in_table:
            html_lines.append('</table>')
            in_table = False
            table_header_done = False

        if not stripped:
            continue

        # Pass through raw HTML directly (for interactive widgets, custom divs, buttons)
        if stripped.startswith("<div") or stripped.startswith("<table") or stripped.startswith("</") or stripped.startswith("<button") or stripped.startswith("<span") or stripped.startswith("<strong"):
            html_lines.append(stripped)
            continue

        # Headers
        if stripped.startswith("### ") or stripped.startswith("## "):
            sec_title = stripped[4:] if stripped.startswith("### ") else stripped[3:]
            close_accordion()

            if has_sections and not toolbar_added:
                html_lines.append('<div class="notes-toolbar">')
                html_lines.append('  <button class="btn-notes-toggle" onclick="toggleAllAccordions(true)">📖 Expand All</button>')
                html_lines.append('  <button class="btn-notes-toggle" onclick="toggleAllAccordions(false)">📁 Collapse All</button>')
                html_lines.append('</div>')
                toolbar_added = True

            accordion_count += 1
            is_first = (accordion_count == 1)
            open_class = " open" if is_first else ""
            arrow = "▾" if is_first else "▸"

            html_lines.append('<div class="concept-accordion">')
            html_lines.append('  <div class="accordion-header" onclick="toggleAccordion(this)">')
            html_lines.append(f'    <span>{sec_title}</span><span class="accordion-arrow">{arrow}</span>')
            html_lines.append('  </div>')
            html_lines.append(f'  <div class="accordion-body{open_class}">')
            in_accordion = True
            continue
        elif stripped.startswith("#### "):
            html_lines.append(f"<h4>{stripped[5:]}</h4>")
        elif stripped.startswith("# "):
            html_lines.append(f"<h2>{stripped[2:]}</h2>")
        # List items
        elif stripped.startswith("- ") or stripped.startswith("* ") or stripped.startswith("• "):
            item_text = stripped[2:]
            html_lines.append(f"<p>• {item_text}</p>")
        else:
            html_lines.append(f"<p>{stripped}</p>")

    if in_quote:
        flush_quote()
    if in_table:
        html_lines.append('</table>')
    close_accordion()

    result = "\n".join(html_lines)

    # Inline formatting: bold, italic, code
    result = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', result)
    result = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', result)
    result = re.sub(r'`(.+?)`', r'<code>\1</code>', result)

    return result

def build_portal(subject_id: str, output_path: Path = None) -> Path:
    subject_dir = ROOT / "subjects" / subject_id
    if not subject_dir.exists():
        raise FileNotFoundError(f"Subject folder not found: {subject_dir}")

    manifest_path = subject_dir / "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # Load KaTeX assets
    vendor_katex = ROOT / "portal_engine" / "vendor" / "katex"
    katex_css_file = vendor_katex / "katex.embedded.css"
    katex_js_file = vendor_katex / "katex.min.js"
    katex_autorender_file = vendor_katex / "auto-render.min.js"

    katex_css = katex_css_file.read_text(encoding="utf-8") if katex_css_file.exists() else ""
    katex_js = katex_js_file.read_text(encoding="utf-8") if katex_js_file.exists() else ""
    katex_autorender = katex_autorender_file.read_text(encoding="utf-8") if katex_autorender_file.exists() else ""

    # 1. Compile Chapters
    chapters_dir = subject_dir / "chapters"
    compiled_chapters = []

    for ch_info in manifest["chapters"]:
        ch_folder = chapters_dir / ch_info["folder"]
        with open(ch_folder / "meta.json", "r", encoding="utf-8") as f:
            ch_data = json.load(f)

        guide_html_file = ch_folder / "guide.html"
        guide_md_file = ch_folder / "guide.md"

        if guide_html_file.exists():
            ch_data["guideHtml"] = guide_html_file.read_text(encoding="utf-8")
        elif guide_md_file.exists():
            ch_data["guideHtml"] = markdown_to_html(guide_md_file.read_text(encoding="utf-8"))
        else:
            ch_data["guideHtml"] = "<p>Notes under development.</p>"

        cards_file = ch_folder / "flashcards.json"
        ch_data["flashcards"] = json.loads(cards_file.read_text(encoding="utf-8")) if cards_file.exists() else []

        q_file = ch_folder / "questions.json"
        ch_data["questions"] = json.loads(q_file.read_text(encoding="utf-8")) if q_file.exists() else []

        # Find subName from categories
        for cat in manifest.get("categories", []):
            if cat["id"] == ch_data.get("sub"):
                ch_data["subName"] = cat["name"]
                break

        compiled_chapters.append(ch_data)

    # 2. Compile Mock Papers
    mock_papers_dir = subject_dir / "mock_papers"
    compiled_papers = []
    if mock_papers_dir.exists():
        for p_file in sorted(mock_papers_dir.glob("*.json")):
            with open(p_file, "r", encoding="utf-8") as f:
                compiled_papers.append(json.load(f))

    # 3. Build Category Tabs and CSS Variables
    cat_tabs_html = []
    theme_vars = []
    theme_vars_dark = []

    for cat in manifest.get("categories", []):
        cat_id = cat["id"]
        cat_name = cat["name"]
        cat_color = cat.get("color", "#2563eb")
        cat_light = cat.get("light", "#eff6ff")
        cat_color_dark = cat.get("colorDark", cat_color)
        cat_light_dark = cat.get("lightDark", "#1e293b")

        cat_tabs_html.append(f'<button class="tab-btn" data-tab="{cat_id}">{cat_name}</button>')
        theme_vars.append(f'--{cat_id}-color: {cat_color};')
        theme_vars.append(f'--{cat_id}-light: {cat_light};')
        theme_vars_dark.append(f'--{cat_id}-color: {cat_color_dark};')
        theme_vars_dark.append(f'--{cat_id}-light: {cat_light_dark};')

    # 4. Load Template and Replace Placeholders
    template_content = TEMPLATE_PATH.read_text(encoding="utf-8")

    replacements = {
        "{{PORTAL_TITLE}}": manifest.get("title", "Study Portal"),
        "{{SUBJECT_ID}}": manifest["id"],
        "{{SUBJECT_NAME}}": manifest.get("subjectName", "Subject"),
        "{{SUBJECT_BADGE}}": manifest.get("badge", "CLASS 9"),
        "{{SUBJECT_SUBTITLE}}": manifest.get("subtitle", "CBSE Exam Preparation"),
        "{{CATEGORY_TABS_HTML}}": "\n          ".join(cat_tabs_html),
        "{{THEME_VARS}}": "\n      ".join(theme_vars),
        "{{THEME_VARS_DARK}}": "\n      ".join(theme_vars_dark),
        "{{DEFAULT_ACTIVE_SCOPE}}": json.dumps(manifest.get("defaultActiveScope", [])),
        "{{CATEGORIES_DATA_JSON}}": json.dumps(manifest.get("categories", []), indent=2, ensure_ascii=False),
        "{{KATEX_CSS}}": katex_css,
        "{{KATEX_JS}}": katex_js,
        "{{KATEX_AUTORENDER_JS}}": katex_autorender,
        "{{CHAPTERS_DATA_JSON}}": json.dumps(compiled_chapters, indent=2, ensure_ascii=False),
        "{{PRACTICE_PAPERS_DATA_JSON}}": json.dumps(compiled_papers, indent=2, ensure_ascii=False),
    }

    output_html = template_content
    for placeholder, val in replacements.items():
        output_html = output_html.replace(placeholder, val)

    # 5. Zero-CDN Check
    external_refs = re.findall(r'<(?:script|link)[^>]*(?:src|href)=["\'](https?://[^"\']+)["\']', output_html, re.I)
    if external_refs:
        print(f"⚠️ Warning: Found external CDN references in output: {external_refs}")

    if output_path is None:
        output_path = ROOT / f"study_{manifest['id']}_dashboard.html"

    output_path.write_text(output_html, encoding="utf-8")
    file_size_kb = output_path.stat().st_size / 1024
    print(f"🎉 Successfully built: {output_path.name} ({file_size_kb:.1f} KB, {len(compiled_chapters)} chapters, {len(compiled_papers)} mock papers)")
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Study Portal Builder")
    parser.add_argument("--subject", required=True, help="Subject folder in subjects/ (e.g. mathematics)")
    parser.add_argument("--output", help="Optional output HTML file path")
    args = parser.parse_args()

    out_p = Path(args.output).resolve() if args.output else None
    build_portal(args.subject, out_p)

if __name__ == "__main__":
    main()
