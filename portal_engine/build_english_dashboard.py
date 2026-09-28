#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the standalone, self-contained Class 9 CBSE English (Track R1) Revision Dashboard:
- Injects structured JSON from english_data.py into english_template.html.
- Writes to study_english_dashboard.html.
- Syncs to public/study_english_dashboard.html for Cloudflare Workers deployment.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import portal_engine.english_data as ed

TEMPLATE_FILE = ROOT / "portal_engine" / "english_template.html"
OUTPUT_HTML = ROOT / "study_english_dashboard.html"
PUBLIC_HTML = ROOT / "public" / "study_english_dashboard.html"

def generate_english_dashboard():
    print("Building English Language & Literature Revision Dashboard (Track R1)...")
    
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Template file not found: {TEMPLATE_FILE}")
        
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    
    units_json = json.dumps(ed.UNITS_DATA, ensure_ascii=False)
    writing_json = json.dumps(ed.MASTER_WRITING_STUDIO, ensure_ascii=False)
    mock_papers_json = json.dumps(ed.MOCK_PAPERS, ensure_ascii=False)
    meta_json = json.dumps(ed.CURRICULUM_META, ensure_ascii=False)
    
    html = (
        template.replace("__UNITS_JSON__", units_json)
        .replace("__WRITING_JSON__", writing_json)
        .replace("__MOCK_PAPERS_JSON__", mock_papers_json)
        .replace("__META_JSON__", meta_json)
    )
    
    OUTPUT_HTML.write_text(html, encoding="utf-8")
    print(f"✅ Generated {OUTPUT_HTML} ({len(html):,} bytes)")
    
    # Sync to public directory for Cloudflare deployment
    PUBLIC_HTML.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC_HTML.write_text(html, encoding="utf-8")
    print(f"✅ Synced to {PUBLIC_HTML} ({len(html):,} bytes)")

if __name__ == "__main__":
    generate_english_dashboard()
