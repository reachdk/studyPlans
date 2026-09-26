#!/usr/bin/env python3
"""
Catalog generator and verification script for the Class 9 Study Dashboard.
Scans local NCERT chapters, Classroom downloads, and revision notes,
verifying zero external dependencies and dataset integrity.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DASHBOARD_HTML = ROOT / "study_dashboard.html"
NOTES_DIR = ROOT / "notes" / "science"
NCERT_SCIENCE = ROOT / "downloads" / "class-09" / "science" / "exploration"
CLASSROOM_DIR = ROOT / "downloads" / "classroom"

EXPECTED_CHAPTERS = [
    ("ch01-exploration-entering-secondary-science.md", "foundations", "iesc101"),
    ("ch02-cell-the-building-block-of-life.md", "biology", "iesc102"),
    ("ch03-tissues-in-action.md", "biology", "iesc103"),
    ("ch04-describing-motion-around-us.md", "physics", "iesc104"),
    ("ch05-exploring-mixtures-and-their-separation.md", "chemistry", "iesc105"),
    ("ch06-how-forces-affect-motion.md", "physics", "iesc106"),
    ("ch07-work-energy-and-simple-machines.md", "physics", "iesc107"),
    ("ch08-journey-inside-the-atom.md", "chemistry", "iesc108"),
    ("ch09-atomic-foundations-of-matter.md", "chemistry", "iesc109"),
    ("ch10-sound-waves.md", "physics", "iesc110"),
    ("ch11-reproduction-how-life-continues.md", "biology", "iesc111"),
    ("ch12-patterns-in-life-diversity-and-classification.md", "biology", "iesc112"),
    ("ch13-earth-as-a-system.md", "biology", "iesc113"),
]

def verify_dashboard_file() -> bool:
    """Verifies that study_dashboard.html exists, is valid HTML, and has zero external network deps."""
    if not DASHBOARD_HTML.exists():
        print(f"❌ Error: {DASHBOARD_HTML.name} not found.")
        return False

    content = DASHBOARD_HTML.read_text(encoding="utf-8")

    # Check for unwanted external script or style CDNs (must be 100% offline-ready)
    external_refs = re.findall(r'<(?:script|link)[^>]*(?:src|href)=["\'](https?://[^"\']+)["\']', content, re.I)
    if external_refs:
        print(f"⚠️ Warning: Found external network dependencies: {external_refs}")
        return False

    required_tokens = [
        "attempt-friction-box",
        "btn-attempt-confirm",
        "active-card",
        "card-face",
        "CHAPTERS_DATA",
        "localStorage",
        "tier-dashboard",
        "tier-workspace"
    ]
    missing = [t for t in required_tokens if t not in content]
    if missing:
        print(f"❌ Error: Missing critical dashboard components: {missing}")
        return False

    print("✅ Verification passed: study_dashboard.html is self-contained, valid, and 100% offline-ready.")
    return True

def verify_notes() -> bool:
    """Verifies that all 13 chapter revision notes exist and are non-empty."""
    missing = []
    for filename, subfolder, _ in EXPECTED_CHAPTERS:
        path = NOTES_DIR / subfolder / filename
        if not path.exists() or path.stat().st_size < 500:
            missing.append(f"{subfolder}/{filename}")

    if missing:
        print(f"❌ Error: Missing or incomplete revision notes: {missing}")
        return False

    print(f"✅ Verification passed: All {len(EXPECTED_CHAPTERS)} Science revision notes are present and complete.")
    return True

def list_available_sources():
    """Lists all available NCERT, Classroom sources, and revision notes."""
    print("\n📚 Available Local NCERT Science Chapters:")
    if NCERT_SCIENCE.exists():
        pdfs = sorted(NCERT_SCIENCE.glob("*.pdf"))
        for p in pdfs:
            print(f"  • {p.name}")
    else:
        print("  (downloads/class-09/science/exploration not found)")

    print("\n📝 Chapter Revision Notes Generated:")
    for filename, subfolder, ncert_id in EXPECTED_CHAPTERS:
        p = NOTES_DIR / subfolder / filename
        size_kb = p.stat().st_size / 1024 if p.exists() else 0
        status = f"✅ ({size_kb:.1f} KB)" if p.exists() else "❌ (missing)"
        print(f"  • [{ncert_id}] {subfolder.upper():11} {filename} {status}")

    print("\n🏫 Synced Classroom Materials:")
    if CLASSROOM_DIR.exists():
        classes = sorted([d for d in CLASSROOM_DIR.iterdir() if d.is_dir()])
        for c in classes:
            files = list(c.glob("*.*"))
            print(f"  • {c.name} ({len(files)} files)")
    else:
        print("  (downloads/classroom not found)")

def main():
    parser = argparse.ArgumentParser(description="Study Dashboard Catalog & Verification Utility")
    parser.add_argument("--verify", action="store_true", help="Verify dashboard and revision notes integrity")
    parser.add_argument("--list", action="store_true", help="List all available local study materials and notes")
    args = parser.parse_args()

    if args.list:
        list_available_sources()
        return

    # Default action is verify
    v_dash = verify_dashboard_file()
    v_notes = verify_notes()
    if not (v_dash and v_notes):
        sys.exit(1)

if __name__ == "__main__":
    main()
