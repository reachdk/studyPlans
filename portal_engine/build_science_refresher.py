#!/usr/bin/env python3
"""
Builds the standalone, self-contained Science Refresher Dashboard:
1. All key terms across Physics, Chemistry, and Biology (with definitions, formulas, and examples).
2. Biology Diagram Atlas covering all 17 GCR revision diagrams with SVG schematics, checklists, and recall modes.
3. Chemistry Chapter 9 Table 9.1(a) and 9.1(b) Ion Matrix, Interactive Criss-Cross Formula Builder, and Quizzer.
"""

import json
import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from portal_engine.refresher_data import KEY_TERMS_DATA, BIOLOGY_DIAGRAMS_DATA, CHEMISTRY_TABLE_9_1_DATA
VENDOR_DIR = ROOT / "portal_engine" / "vendor"
OUTPUT_HTML = ROOT / "study_science_refresher.html"

def load_vendor_assets():
    katex_dir = VENDOR_DIR / "katex"
    katex_css = (katex_dir / "katex.embedded.css").read_text(encoding="utf-8") if (katex_dir / "katex.embedded.css").exists() else ""
    katex_js = (katex_dir / "katex.min.js").read_text(encoding="utf-8") if (katex_dir / "katex.min.js").exists() else ""
    katex_auto = (katex_dir / "auto-render.min.js").read_text(encoding="utf-8") if (katex_dir / "auto-render.min.js").exists() else ""
    return katex_css, katex_js, katex_auto

def load_diagram_images():
    images = {}
    img_dir = ROOT / "images" / "ncert_diagrams"
    for img_file in sorted(img_dir.glob("diag_*.png")):
        diag_id = img_file.stem
        b64 = base64.b64encode(img_file.read_bytes()).decode("utf-8")
        images[diag_id] = f"data:image/png;base64,{b64}"
    return images

def generate_refresher():
    print("Building Science Refresher Dashboard...")
    katex_css, katex_js, katex_auto = load_vendor_assets()
    diagram_images = load_diagram_images()
    print(f"Loaded {len(diagram_images)} authentic NCERT diagram images.")

    key_terms_json = json.dumps(KEY_TERMS_DATA, ensure_ascii=False)
    biology_diagrams_json = json.dumps(BIOLOGY_DIAGRAMS_DATA, ensure_ascii=False)
    chemistry_table_json = json.dumps(CHEMISTRY_TABLE_9_1_DATA, ensure_ascii=False)
    diagram_images_json = json.dumps(diagram_images, ensure_ascii=False)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Class 9 Science Comprehensive Refresher & Formula Dashboard</title>
  <style>
{katex_css}
  </style>
  <style>
    :root {{
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --primary: #0284c7;
      --primary-light: #e0f2fe;
      --phy-color: #0284c7;
      --phy-light: #f0f9ff;
      --chem-color: #7c3aed;
      --chem-light: #f5f3ff;
      --bio-color: #16a34a;
      --bio-light: #f0fdf4;
      --danger: #dc2626;
      --danger-light: #fef2f2;
      --warning: #d97706;
      --warning-light: #fffbeb;
      --success: #16a34a;
      --radius: 12px;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.07);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.08);
    }}

    [data-theme="dark"] {{
      --bg: #090d16;
      --card-bg: #131b2e;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --border: #1e293b;
      --primary: #38bdf8;
      --primary-light: #082f49;
      --phy-color: #38bdf8;
      --phy-light: #0c4a6e;
      --chem-color: #a78bfa;
      --chem-light: #3b0764;
      --bio-color: #4ade80;
      --bio-light: #052e16;
      --danger-light: #450a0a;
      --warning-light: #451a03;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}

    body {{
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 60px;
    }}

    /* HEADER */
    header {{
      background: var(--card-bg);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-sm);
    }}

    .top-bar {{
      max-width: 1300px;
      margin: 0 auto;
      padding: 12px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}

    .badge-class {{
      background: var(--primary);
      color: white;
      font-weight: 800;
      font-size: 0.78rem;
      padding: 4px 10px;
      border-radius: 20px;
      letter-spacing: 0.5px;
    }}

    .brand-text h1 {{
      font-size: 1.2rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-text p {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn-nav {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }}

    .btn-nav:hover {{
      background: var(--bg);
      border-color: var(--text-muted);
    }}

    .btn-nav.primary {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    .btn-icon {{
      background: transparent;
      border: 1px solid var(--border);
      color: var(--text);
      padding: 6px 10px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 1rem;
    }}

    /* MAIN CONTAINER */
    main {{
      max-width: 1300px;
      margin: 24px auto;
      padding: 0 20px;
    }}

    /* MODULE TABS */
    .module-nav {{
      display: flex;
      gap: 8px;
      background: var(--card-bg);
      padding: 6px;
      border-radius: 14px;
      border: 1px solid var(--border);
      margin-bottom: 24px;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
    }}

    .module-tab-btn {{
      flex: 1;
      min-width: 220px;
      padding: 10px 18px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-weight: 700;
      font-size: 0.9rem;
      border-radius: 10px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
    }}

    .module-tab-btn:hover {{
      color: var(--text);
      background: var(--bg);
    }}

    .module-tab-btn.active {{
      background: var(--primary);
      color: white;
      box-shadow: 0 2px 4px rgba(2, 132, 199, 0.25);
    }}

    /* FILTER BAR */
    .filter-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}

    .search-box {{
      position: relative;
      flex: 1;
      min-width: 280px;
    }}

    .search-box input {{
      width: 100%;
      padding: 10px 16px 10px 38px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      font-size: 0.9rem;
      outline: none;
    }}

    .search-box svg {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }}

    .filter-pills {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      align-items: center;
    }}

    .pill-btn {{
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .pill-btn:hover {{
      border-color: var(--text-muted);
      color: var(--text);
    }}

    .pill-btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    .select-dropdown {{
      padding: 7px 12px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      font-size: 0.85rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }}

    /* CHAPTER ACCORDION */
    .chapter-section {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 20px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}

    .chapter-header {{
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      background: var(--card-bg);
      border-bottom: 1px solid var(--border);
      user-select: none;
    }}

    .chapter-header:hover {{
      background: var(--bg);
    }}

    .chapter-title-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .chapter-badge {{
      font-size: 0.75rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }}

    .badge-phy {{ background: var(--phy-light); color: var(--phy-color); border: 1px solid var(--phy-color); }}
    .badge-chem {{ background: var(--chem-light); color: var(--chem-color); border: 1px solid var(--chem-color); }}
    .badge-bio {{ background: var(--bio-light); color: var(--bio-color); border: 1px solid var(--bio-color); }}

    .chapter-header h3 {{
      font-size: 1.05rem;
      font-weight: 700;
    }}

    .chapter-count {{
      font-size: 0.82rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .chapter-body {{
      padding: 20px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 16px;
    }}

    .chapter-body.collapsed {{
      display: none;
    }}

    /* TERM CARD */
    .term-card {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: all 0.2s;
      position: relative;
    }}

    .term-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow);
      border-color: var(--primary);
    }}

    .term-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 8px;
    }}

    .term-title {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--primary);
    }}

    .term-cat-badge {{
      font-size: 0.7rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 12px;
      background: var(--card-bg);
      border: 1px solid var(--border);
      color: var(--text-muted);
      white-space: nowrap;
    }}

    .btn-star {{
      background: transparent;
      border: none;
      cursor: pointer;
      font-size: 1.1rem;
      opacity: 0.4;
      transition: opacity 0.15s, transform 0.15s;
    }}

    .btn-star:hover {{
      transform: scale(1.2);
    }}

    .btn-star.starred {{
      opacity: 1;
      color: #f59e0b;
    }}

    .term-def {{
      font-size: 0.9rem;
      line-height: 1.5;
    }}

    .term-formula-box {{
      background: var(--card-bg);
      border-left: 3px solid var(--primary);
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      font-size: 0.88rem;
    }}

    .term-example-box {{
      font-size: 0.82rem;
      color: var(--text-muted);
      border-top: 1px dashed var(--border);
      padding-top: 8px;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }}

    /* BIOLOGY DIAGRAM CARD */
    .diagrams-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
      gap: 24px;
    }}

    .diagram-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 16px;
      transition: all 0.2s;
    }}

    .diagram-card:hover {{
      box-shadow: var(--shadow-lg);
      border-color: var(--bio-color);
    }}

    .diagram-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
    }}

    .diagram-fig-badge {{
      background: var(--bio-light);
      color: var(--bio-color);
      border: 1px solid var(--bio-color);
      font-size: 0.78rem;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 6px;
    }}

    .diagram-title {{
      font-size: 1.15rem;
      font-weight: 800;
      margin-top: 4px;
    }}

    .diagram-visual-box {{
      background: #ffffff;
      border: 1.5px solid var(--border);
      border-radius: 10px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 240px;
      position: relative;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s;
    }}

    [data-theme="dark"] .diagram-visual-box {{
      background: #0f172a;
    }}

    .ncert-diagram-img {{
      max-width: 100%;
      max-height: 270px;
      object-fit: contain;
      border-radius: 6px;
      background: #ffffff;
      transition: filter 0.3s ease, transform 0.2s ease;
    }}

    [data-theme="dark"] .ncert-diagram-img {{
      background: #ffffff;
      padding: 4px;
    }}

    .diagram-visual-box.recall-hidden .ncert-diagram-img {{
      filter: blur(14px) grayscale(60%);
    }}

    .diagram-visual-box.recall-hidden.revealed .ncert-diagram-img {{
      filter: none;
    }}

    .recall-overlay-badge {{
      display: none;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: rgba(15, 23, 42, 0.88);
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      pointer-events: none;
      box-shadow: 0 4px 14px rgba(0,0,0,0.35);
      z-index: 5;
    }}

    .diagram-visual-box.recall-hidden .recall-overlay-badge {{
      display: block;
    }}

    .diagram-visual-box.recall-hidden.revealed .recall-overlay-badge {{
      display: none;
    }}

    .btn-zoom {{
      position: absolute;
      top: 8px;
      right: 8px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--border);
      color: var(--text-muted);
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s;
      z-index: 6;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .btn-zoom:hover {{
      background: var(--bio-color);
      color: #ffffff;
      border-color: var(--bio-color);
    }}

    /* LIGHTBOX MODAL */
    .modal-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(15, 23, 42, 0.82);
      backdrop-filter: blur(6px);
      z-index: 99999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-overlay.open {{
      display: flex;
    }}
    .modal-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      max-width: 950px;
      width: 100%;
      max-height: 92vh;
      overflow-y: auto;
      padding: 24px;
      position: relative;
      box-shadow: 0 25px 50px -12px rgba(0,0,0,0.4);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .modal-close-btn {{
      position: absolute;
      top: 16px;
      right: 16px;
      background: var(--bg);
      border: 1px solid var(--border);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      font-size: 1.1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text);
      transition: all 0.15s;
    }}
    .modal-close-btn:hover {{
      background: var(--danger-light);
      color: var(--danger);
    }}
    .modal-header-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--bio-color);
      padding-right: 40px;
    }}
    .modal-img-container {{
      display: flex;
      justify-content: center;
      align-items: center;
      background: #ffffff;
      padding: 16px;
      border-radius: 10px;
      border: 1px solid var(--border);
    }}
    .modal-img-container img {{
      max-width: 100%;
      max-height: 65vh;
      object-fit: contain;
    }}
    .modal-info-box {{
      background: var(--bg);
      padding: 12px 16px;
      border-radius: 8px;
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .diagram-interactive-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      margin-top: 6px;
    }}

    .btn-recall-toggle {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }}

    .btn-recall-toggle.active {{
      background: var(--warning-light);
      color: var(--warning);
      border-color: var(--warning);
    }}

    .labels-checklist {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .label-row {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      padding: 6px 10px;
      background: var(--bg);
      border-radius: 6px;
      font-size: 0.85rem;
      gap: 10px;
    }}

    .label-name {{
      font-weight: 700;
      color: var(--bio-color);
      min-width: 140px;
    }}

    .label-desc {{
      color: var(--text);
      font-size: 0.82rem;
      flex: 1;
    }}

    .test-hidden .label-name {{
      filter: blur(4px);
      user-select: none;
      cursor: pointer;
    }}

    .test-hidden .label-name:hover {{
      filter: none;
    }}

    .examiner-tip-box {{
      background: var(--warning-light);
      border-left: 3px solid var(--warning);
      color: var(--text);
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 0.84rem;
      line-height: 1.45;
    }}

    /* CHEMISTRY VALENCY & FORMULA BUILDER */
    .chem-split {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }}

    @media (max-width: 900px) {{
      .chem-split {{
        grid-template-columns: 1fr;
      }}
    }}

    .builder-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow);
    }}

    .builder-title {{
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--chem-color);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .ion-pickers {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin: 16px 0;
    }}

    .ion-picker-col h4 {{
      font-size: 0.88rem;
      margin-bottom: 8px;
      color: var(--text-muted);
    }}

    .ion-select {{
      width: 100%;
      padding: 10px 14px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: var(--bg);
      color: var(--text);
      font-size: 0.95rem;
      font-weight: 700;
      outline: none;
      cursor: pointer;
    }}

    .criss-cross-stage {{
      background: var(--bg);
      border: 1.5px dashed var(--chem-color);
      border-radius: 12px;
      padding: 20px;
      text-align: center;
      margin: 16px 0;
    }}

    .criss-cross-display {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 40px;
      margin: 14px 0;
    }}

    .ion-step-col {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }}

    .ion-symbol-box {{
      font-size: 1.8rem;
      font-weight: 800;
      color: var(--chem-color);
    }}

    .ion-valency-box {{
      background: var(--chem-light);
      color: var(--chem-color);
      font-size: 1.1rem;
      font-weight: 800;
      padding: 4px 14px;
      border-radius: 20px;
      border: 1px solid var(--chem-color);
    }}

    .cross-arrows {{
      font-size: 2rem;
      color: var(--warning);
      font-weight: bold;
    }}

    .formula-result-box {{
      background: var(--chem-light);
      border: 1.5px solid var(--chem-color);
      border-radius: 10px;
      padding: 16px;
      text-align: center;
      margin-top: 14px;
    }}

    .formula-result-name {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-muted);
    }}

    .formula-result-code {{
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--chem-color);
      letter-spacing: 1px;
      margin: 4px 0;
    }}

    .formula-rule-note {{
      font-size: 0.85rem;
      color: var(--text);
      line-height: 1.4;
      margin-top: 6px;
    }}

    /* ION MATRIX TABLES */
    .ion-table-container {{
      overflow-x: auto;
      margin-top: 16px;
    }}

    .ion-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    .ion-table th, .ion-table td {{
      padding: 10px 14px;
      border: 1px solid var(--border);
      text-align: left;
    }}

    .ion-table th {{
      background: var(--bg);
      font-weight: 800;
      color: var(--text);
    }}

    .ion-table tr:hover td {{
      background: var(--bg);
    }}

    .val-badge {{
      display: inline-block;
      font-weight: 800;
      font-size: 0.75rem;
      padding: 2px 8px;
      border-radius: 12px;
      text-align: center;
    }}

    .val-1 {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
    .val-2 {{ background: #f5f3ff; color: #6d28d9; border: 1px solid #ddd6fe; }}
    .val-3 {{ background: #fdf2f8; color: #be185d; border: 1px solid #fbcfe8; }}

    /* QUIZZER */
    .quizzer-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow);
      margin-top: 24px;
    }}

    .quiz-question-box {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 20px;
      margin-top: 16px;
      text-align: center;
    }}

    .quiz-question-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 16px;
    }}

    .quiz-options-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 12px;
      max-width: 600px;
      margin: 0 auto;
    }}

    .btn-quiz-opt {{
      background: var(--card-bg);
      border: 1.5px solid var(--border);
      color: var(--text);
      font-size: 1.15rem;
      font-weight: 800;
      padding: 12px 18px;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .btn-quiz-opt:hover {{
      border-color: var(--chem-color);
      background: var(--chem-light);
    }}

    .btn-quiz-opt.correct {{
      background: #bbf7d0 !important;
      border-color: #22c55e !important;
      color: #15803d !important;
    }}

    .btn-quiz-opt.wrong {{
      background: #fecaca !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
    }}

    .quiz-feedback {{
      margin-top: 16px;
      padding: 12px;
      border-radius: 8px;
      font-size: 0.95rem;
      font-weight: 700;
      display: none;
    }}

    /* TOAST */
    .toast-msg {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0f172a;
      color: white;
      padding: 12px 20px;
      border-radius: 10px;
      font-size: 0.88rem;
      font-weight: 600;
      box-shadow: var(--shadow-lg);
      z-index: 200;
      display: none;
    }}
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header>
    <div class="top-bar">
      <a href="index.html" class="brand-group" title="Back to Learning Hub">
        <span class="badge-class">CBSE CLASS 9</span>
        <div class="brand-text">
          <h1>🔬 Science Refresher Dashboard</h1>
          <p>Key Terms & Formulae • Biology Diagram Atlas • Table 9.1 Formula Builder</p>
        </div>
      </a>

      <div class="header-actions">
        <a href="study_science_dashboard.html" class="btn-nav primary" title="Open Full Science Study Hub">
          ← Science Hub
        </a>
        <a href="index.html" class="btn-nav" title="Home Hub">
          🏠 Home
        </a>
        <button id="btn-theme-toggle" class="btn-icon" title="Toggle Theme">
          🌓
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN VIEW -->
  <main>
    <!-- MODULE NAVIGATION -->
    <nav class="module-nav" aria-label="Refresher Modules">
      <button class="module-tab-btn active" data-mod="glossary">
        <span>📖</span> Key Terms & Formulae Glossary (<span id="mod-terms-count">0</span>)
      </button>
      <button class="module-tab-btn" data-mod="diagrams">
        <span>🔬</span> Biology Exam Diagrams Atlas (17)
      </button>
      <button class="module-tab-btn" data-mod="chemistry">
        <span>⚗️</span> Chemistry Ch 9: Ion Valency & Formula Builder
      </button>
    </nav>

    <!-- =====================================================================
         MODULE 1: KEY TERMS & FORMULAE GLOSSARY
         ===================================================================== -->
    <section id="module-glossary" class="refresher-module">
      <div class="filter-bar">
        <div class="search-box">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          <input type="text" id="terms-search-input" placeholder="Search any term, formula, definition, or example...">
        </div>

        <div class="filter-pills">
          <button class="pill-btn active" data-filter-sub="all">All Subjects</button>
          <button class="pill-btn" data-filter-sub="phy">⚡ Physics</button>
          <button class="pill-btn" data-filter-sub="chem">🧪 Chemistry</button>
          <button class="pill-btn" data-filter-sub="bio">🌿 Biology</button>
          <button class="pill-btn" id="btn-starred-filter">⭐ Starred Only (<span id="starred-count">0</span>)</button>

          <select id="chapter-select-jump" class="select-dropdown" aria-label="Jump to Chapter">
            <option value="all">Jump to Chapter ▾</option>
            <option value="Ch 4">Ch 4: Describing Motion Around Us</option>
            <option value="Ch 6">Ch 6: How Forces Affect Motion</option>
            <option value="Ch 7">Ch 7: Work, Energy and Simple Machines</option>
            <option value="Ch 5">Ch 5: Exploring Mixtures & Separation</option>
            <option value="Ch 8">Ch 8: Journey Inside the Atom</option>
            <option value="Ch 9">Ch 9: Atomic Foundations of Matter</option>
            <option value="Ch 2">Ch 2: Cell — Building Block of Life</option>
            <option value="Ch 3">Ch 3: Tissues in Action</option>
            <option value="Ch 11">Ch 11: Reproduction: How Life Continues</option>
          </select>

          <button id="btn-toggle-all-accordions" class="btn-nav" style="padding: 6px 12px; font-size: 0.8rem;">
            ⇕ Expand All
          </button>
        </div>
      </div>

      <div id="glossary-chapters-container">
        <!-- Rendered dynamically -->
      </div>
    </section>

    <!-- =====================================================================
         MODULE 2: BIOLOGY EXAM DIAGRAMS ATLAS
         ===================================================================== -->
    <section id="module-diagrams" class="refresher-module" style="display: none;">
      <div class="filter-bar">
        <div class="search-box">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
          <input type="text" id="diagrams-search-input" placeholder="Search diagrams, organelle, tissue or flower parts...">
        </div>

        <div class="filter-pills">
          <button class="pill-btn active" data-filter-diag="all">All 17 Diagrams</button>
          <button class="pill-btn" data-filter-diag="Ch 3">🌿 Tissues (3)</button>
          <button class="pill-btn" data-filter-diag="Ch 2">🧬 Cell (9)</button>
          <button class="pill-btn" data-filter-diag="Ch 11">🌸 Reproduction (5)</button>
          <button id="btn-toggle-all-recall" class="pill-btn" style="border-color: var(--warning); color: var(--warning); font-weight: 700;">
            🧠 Test Recall Mode (Hide Labels)
          </button>
        </div>
      </div>

      <div class="diagrams-grid" id="diagrams-grid-container">
        <!-- Rendered dynamically -->
      </div>
    </section>

    <!-- =====================================================================
         MODULE 3: CHEMISTRY CH 9 ION VALENCY & FORMULA BUILDER
         ===================================================================== -->
    <section id="module-chemistry" class="refresher-module" style="display: none;">
      <div class="chem-split">
        <!-- LEFT: CRISS-CROSS INTERACTIVE BUILDER -->
        <div class="builder-card">
          <div class="builder-title">
            <span>✨</span> Interactive Formula Builder (Criss-Cross Rule)
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted);">
            Pick any cation and anion from Table 9.1. Watch the valencies criss-cross step-by-step with automatic ratio simplification and polyatomic bracket rules.
          </p>

          <div class="ion-pickers">
            <div class="ion-picker-col">
              <h4>1. Select Cation (Metal / Positive Ion)</h4>
              <select id="builder-cation-select" class="ion-select" aria-label="Select Cation"></select>
            </div>
            <div class="ion-picker-col">
              <h4>2. Select Anion (Non-metal / Negative Ion)</h4>
              <select id="builder-anion-select" class="ion-select" aria-label="Select Anion"></select>
            </div>
          </div>

          <div class="criss-cross-stage">
            <div style="font-size: 0.82rem; font-weight: 800; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;">
              Criss-Cross Valency Derivation
            </div>
            <div class="criss-cross-display">
              <div class="ion-step-col">
                <div class="ion-symbol-box" id="disp-cation-sym">Na</div>
                <div class="ion-valency-box" id="disp-cation-val">Valency: 1</div>
              </div>
              <div class="cross-arrows">✕</div>
              <div class="ion-step-col">
                <div class="ion-symbol-box" id="disp-anion-sym">Cl</div>
                <div class="ion-valency-box" id="disp-anion-val">Valency: 1</div>
              </div>
            </div>
            <div id="disp-step-explanation" style="font-size: 0.85rem; color: var(--text-muted);">
              Crossover valencies: Na receives valency 1, Cl receives valency 1.
            </div>
          </div>

          <div class="formula-result-box">
            <div class="formula-result-name" id="disp-compound-name">Sodium chloride</div>
            <div class="formula-result-code" id="disp-compound-formula">NaCl</div>
            <div class="formula-rule-note" id="disp-bracket-rule">Both valencies are 1; subscripts are omitted in standard IUPAC chemical formulae.</div>
          </div>
        </div>

        <!-- RIGHT: TABLE 9.1(a) & 9.1(b) MATRIX WITH FILTERS -->
        <div class="builder-card">
          <div class="builder-title">
            <span>📋</span> NCERT Table 9.1: Ions & Valencies Matrix
          </div>
          <p style="font-size: 0.85rem; color: var(--text-muted);">
            Official NCERT Chapter 9 (Pages 174–175) reference table of monoatomic & polyatomic ions.
          </p>

          <div class="filter-pills" style="margin: 12px 0;">
            <button class="pill-btn active" data-ion-table-filter="all">All Ions (27)</button>
            <button class="pill-btn" data-ion-table-filter="mono">9.1(a) Monoatomic</button>
            <button class="pill-btn" data-ion-table-filter="poly">9.1(b) Polyatomic</button>
            <button class="pill-btn" data-ion-table-filter="val1">Valency 1</button>
            <button class="pill-btn" data-ion-table-filter="val2">Valency 2</button>
            <button class="pill-btn" data-ion-table-filter="val3">Valency 3</button>
          </div>

          <div class="ion-table-container">
            <table class="ion-table" id="ion-matrix-table">
              <thead>
                <tr>
                  <th>Ion Name</th>
                  <th>Formula</th>
                  <th>Charge</th>
                  <th>Valency</th>
                  <th>Type</th>
                </tr>
              </thead>
              <tbody id="ion-matrix-tbody">
                <!-- Injected dynamically -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- FORMULA PRACTICE DRILL / QUIZZER -->
      <div class="quizzer-card">
        <div class="builder-title">
          <span>🎯</span> CBSE Chemical Formula Mastery Quizzer
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted);">
          Test your exam recall on CBSE Class 9 authentic chemical compounds. Identify the correct chemical formula based on the criss-cross and polyatomic bracket rules.
        </p>

        <div class="quiz-question-box">
          <div style="font-size: 0.82rem; font-weight: 800; color: var(--chem-color); margin-bottom: 4px;">
            QUESTION <span id="quiz-index-stat">1</span> OF <span id="quiz-total-stat">15</span>
          </div>
          <div class="quiz-question-title" id="quiz-question-text">
            What is the chemical formula for Calcium hydroxide?
          </div>

          <div class="quiz-options-grid" id="quiz-options-container">
            <!-- Injected dynamically -->
          </div>

          <div class="quiz-feedback" id="quiz-feedback-box"></div>

          <div style="margin-top: 18px; display: flex; justify-content: center; gap: 12px;">
            <button id="btn-next-quiz" class="btn-nav primary" style="display: none;">Next Compound →</button>
            <button id="btn-restart-quiz" class="btn-nav">🔀 New Random Question</button>
          </div>
        </div>
      </div>
    </section>
  </main>

  <div id="toast-el" class="toast-msg"></div>

  <!-- KATEX JS -->
  <script>
{katex_js}
  </script>
  <script>
{katex_auto}
  </script>

  <!-- DATA & APP LOGIC -->
  <script>
    const KEY_TERMS_DATA = {key_terms_json};
    const BIOLOGY_DIAGRAMS_DATA = {biology_diagrams_json};
    const CHEMISTRY_TABLE_9_1_DATA = {chemistry_table_json};
    const DIAGRAM_IMAGES = {diagram_images_json};

    /* =========================================================================
       STATE & STORAGE
       ========================================================================= */
    const STORAGE_KEY_STARRED = "refresher_starred_terms";
    const STORAGE_KEY_THEME = "refresher_theme";

    function getStarredTerms() {{
      try {{
        const saved = localStorage.getItem(STORAGE_KEY_STARRED);
        return saved ? JSON.parse(saved) : {{}};
      }} catch (e) {{
        return {{}};
      }}
    }}

    function toggleStarredTerm(termId) {{
      const starred = getStarredTerms();
      starred[termId] = !starred[termId];
      if (!starred[termId]) delete starred[termId];
      try {{
        localStorage.setItem(STORAGE_KEY_STARRED, JSON.stringify(starred));
      }} catch (e) {{}}
      updateStarredCount();
      return !!starred[termId];
    }}

    function updateStarredCount() {{
      const count = Object.keys(getStarredTerms()).length;
      const el = document.getElementById("starred-count");
      if (el) el.textContent = count;
    }}

    /* =========================================================================
       MATH RENDERING HELPER
       ========================================================================= */
    function triggerMath(element) {{
      if (typeof renderMathInElement === 'function') {{
        try {{
          renderMathInElement(element || document.body, {{
            delimiters: [
              {{left: '$$', right: '$$', display: true}},
              {{left: '$', right: '$', display: false}},
              {{left: '\\\\(', right: '\\\\)', display: false}},
              {{left: '\\\\[', right: '\\\\]', display: true}}
            ],
            throwOnError: false
          }});
        }} catch (e) {{}}
      }}
    }}

    /* =========================================================================
       MODULE 1: GLOSSARY ENGINE
       ========================================================================= */
    let currentGlossarySubFilter = "all";
    let showStarredOnly = false;

    function renderGlossary() {{
      const container = document.getElementById("glossary-chapters-container");
      if (!container) return;
      container.innerHTML = "";

      const query = (document.getElementById("terms-search-input")?.value || "").toLowerCase().trim();
      const starredMap = getStarredTerms();
      const jumpVal = document.getElementById("chapter-select-jump")?.value || "all";

      // Group terms by Chapter
      const chaptersMap = new Map();
      KEY_TERMS_DATA.forEach(t => {{
        if (!chaptersMap.has(t.chCode)) {{
          chaptersMap.set(t.chCode, {{
            code: t.chCode,
            title: t.chTitle,
            sub: t.sub,
            terms: []
          }});
        }}
        chaptersMap.get(t.chCode).terms.push(t);
      }});

      let totalVisibleTerms = 0;

      chaptersMap.forEach(ch => {{
        // Filter by subject
        if (currentGlossarySubFilter !== "all" && ch.sub !== currentGlossarySubFilter) return;
        // Filter by jump chapter
        if (jumpVal !== "all" && ch.code !== jumpVal) return;

        // Filter terms
        const filteredTerms = ch.terms.filter(t => {{
          if (showStarredOnly && !starredMap[t.id]) return false;
          if (query) {{
            const matchName = t.term.toLowerCase().includes(query);
            const matchDef = t.definition.toLowerCase().includes(query);
            const matchEx = t.example.toLowerCase().includes(query);
            const matchForm = (t.formula || "").toLowerCase().includes(query);
            return matchName || matchDef || matchEx || matchForm;
          }}
          return true;
        }});

        if (filteredTerms.length === 0) return;
        totalVisibleTerms += filteredTerms.length;

        const chBadgeClass = ch.sub === "phy" ? "badge-phy" : ch.sub === "chem" ? "badge-chem" : "badge-bio";
        const subLabel = ch.sub === "phy" ? "Physics" : ch.sub === "chem" ? "Chemistry" : "Biology";

        const sec = document.createElement("div");
        sec.className = "chapter-section";
        sec.id = `sec-${{ch.code.replace(/\\s+/g, '-').toLowerCase()}}`;

        sec.innerHTML = `
          <div class="chapter-header" onclick="toggleChapterSection(this)">
            <div class="chapter-title-wrap">
              <span class="chapter-badge ${{chBadgeClass}}">${{subLabel}} • ${{ch.code}}</span>
              <h3>${{ch.title}}</h3>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              <span class="chapter-count">${{filteredTerms.length}} Term${{filteredTerms.length > 1 ? 's' : ''}}</span>
              <span class="accordion-arrow" style="font-size:1.1rem; color:var(--text-muted);">▾</span>
            </div>
          </div>
          <div class="chapter-body">
            ${{filteredTerms.map(t => {{
              const isStarred = !!starredMap[t.id];
              return `
                <div class="term-card" id="term-${{t.id}}">
                  <div class="term-top">
                    <div class="term-title">${{t.term}}</div>
                    <div style="display:flex; align-items:center; gap:6px;">
                      <span class="term-cat-badge">${{t.category}}</span>
                      <button class="btn-star ${{isStarred ? 'starred' : ''}}" onclick="handleStarClick(event, '${{t.id}}')" title="Star for quick revision">
                        ${{isStarred ? '★' : '☆'}}
                      </button>
                    </div>
                  </div>
                  <div class="term-def">${{t.definition}}</div>
                  ${{t.formula || t.unit ? `
                    <div class="term-formula-box">
                      ${{t.formula ? `<div><strong>Formula:</strong> $${{t.formula}}$</div>` : ''}}
                      ${{t.unit ? `<div style="margin-top:2px;"><strong>SI Unit:</strong> $${{t.unit}}$</div>` : ''}}
                    </div>
                  ` : ''}}
                  ${{t.example ? `
                    <div class="term-example-box">
                      <strong>Example:</strong> <span>${{t.example}}</span>
                    </div>
                  ` : ''}}
                </div>
              `;
            }}).join("")}}
          </div>
        `;

        container.appendChild(sec);
      }});

      if (totalVisibleTerms === 0) {{
        container.innerHTML = `
          <div style="text-align:center; padding:50px 20px; color:var(--text-muted);">
            <h3>No matching key terms found</h3>
            <p style="margin-top:8px; font-size:0.9rem;">Try modifying your search or clearing the starred filter.</p>
          </div>
        `;
      }}

      triggerMath(container);
    }}

    function toggleChapterSection(header) {{
      const body = header.nextElementSibling;
      const arrow = header.querySelector(".accordion-arrow");
      if (body) {{
        const isCollapsed = body.classList.toggle("collapsed");
        if (arrow) arrow.textContent = isCollapsed ? "▸" : "▾";
      }}
    }}

    function handleStarClick(e, termId) {{
      e.stopPropagation();
      const isNowStarred = toggleStarredTerm(termId);
      const btn = e.currentTarget;
      btn.textContent = isNowStarred ? "★" : "☆";
      btn.classList.toggle("starred", isNowStarred);
      showToast(isNowStarred ? "⭐ Term starred for quick review" : "Unstarred term");
      if (showStarredOnly) renderGlossary();
    }}

    /* =========================================================================
       MODULE 2: BIOLOGY DIAGRAM ATLAS ENGINE
       ========================================================================= */
    let currentDiagFilter = "all";
    let isRecallModeActive = false;

    function renderBiologyDiagrams() {{
      const container = document.getElementById("diagrams-grid-container");
      if (!container) return;
      container.innerHTML = "";

      const query = (document.getElementById("diagrams-search-input")?.value || "").toLowerCase().trim();

      const filtered = BIOLOGY_DIAGRAMS_DATA.filter(d => {{
        if (currentDiagFilter !== "all" && d.chapter !== currentDiagFilter) return false;
        if (query) {{
          const matchTitle = d.title.toLowerCase().includes(query);
          const matchFig = d.figCode.toLowerCase().includes(query);
          const matchLabels = d.labels.some(l => l.part.toLowerCase().includes(query) || l.desc.toLowerCase().includes(query));
          return matchTitle || matchFig || matchLabels;
        }}
        return true;
      }});

      if (filtered.length === 0) {{
        container.innerHTML = `<div style="grid-column:1/-1; text-align:center; padding:40px; color:var(--text-muted);">No diagrams match your search.</div>`;
        return;
      }}

      filtered.forEach(d => {{
        const card = document.createElement("div");
        card.className = "diagram-card";
        card.id = `card-${{d.id}}`;

        const imgData = DIAGRAM_IMAGES[d.id];
        const svgIllustration = getSvgIllustration(d.svgType, d.figCode);

        card.innerHTML = `
          <div class="diagram-header">
            <div>
              <span class="diagram-fig-badge">${{d.figCode}} • NCERT Page ${{d.ncertPage}}</span>
              <div class="diagram-title">${{d.title}}</div>
              <div style="font-size:0.8rem; color:var(--text-muted); margin-top:2px;">${{d.chapter}}: ${{d.chTitle}}</div>
            </div>
            <a href="${{d.pdfPath}}" target="_blank" class="btn-nav" style="font-size:0.75rem; padding:4px 10px;" title="Open original NCERT page in PDF">
              📄 NCERT PDF
            </a>
          </div>

          <div class="diagram-visual-box ${{isRecallModeActive ? 'recall-hidden' : ''}}" onclick="toggleImageCardRecall(this)" title="Click to reveal / hide image in recall mode">
            ${{imgData ? `
              <img src="${{imgData}}" alt="${{d.figCode}}: ${{d.title}}" class="ncert-diagram-img" loading="lazy" />
              <div class="recall-overlay-badge">🧠 Click to reveal / hide image</div>
              <button class="btn-zoom" onclick="event.stopPropagation(); openDiagramModal('${{d.id}}')" title="Zoom in full resolution">🔍 Zoom</button>
            ` : `
              ${{svgIllustration}}
            `}}
          </div>

          <div class="diagram-interactive-bar">
            <span style="font-size:0.82rem; font-weight:700; color:var(--text-muted);">Must-Label Criteria (CBSE Rubric)</span>
            <button class="btn-recall-toggle ${{isRecallModeActive ? 'active' : ''}}" onclick="toggleSingleCardRecall(this)">
              <span>🧠</span> Toggle Label Recall
            </button>
          </div>

          <div class="labels-checklist ${{isRecallModeActive ? 'test-hidden' : ''}}">
            ${{d.labels.map(l => `
              <div class="label-row">
                <span class="label-name" title="Click to reveal if hidden">${{l.part}}</span>
                <span class="label-desc">${{l.desc}}</span>
              </div>
            `).join("")}}
          </div>

          <div class="examiner-tip-box">
            💡 <strong>Examiner Guidance:</strong> ${{d.examinerTip}}
          </div>
        `;

        container.appendChild(card);
      }});

      triggerMath(container);
    }}

    function toggleImageCardRecall(box) {{
      if (box.classList.contains("recall-hidden")) {{
        box.classList.toggle("revealed");
      }}
    }}

    function toggleSingleCardRecall(btn) {{
      const card = btn.closest(".diagram-card");
      if (!card) return;
      const checklist = card.querySelector(".labels-checklist");
      const visualBox = card.querySelector(".diagram-visual-box");
      if (checklist) {{
        const isHidden = checklist.classList.toggle("test-hidden");
        if (visualBox) {{
          visualBox.classList.toggle("recall-hidden", isHidden);
          visualBox.classList.remove("revealed");
        }}
        btn.classList.toggle("active", isHidden);
      }}
    }}

    function openDiagramModal(diagId) {{
      const diag = BIOLOGY_DIAGRAMS_DATA.find(d => d.id === diagId);
      if (!diag) return;
      const modal = document.getElementById("diagram-modal");
      const title = document.getElementById("modal-title");
      const img = document.getElementById("modal-img");
      const info = document.getElementById("modal-info");

      title.textContent = `${{diag.figCode}}: ${{diag.title}} (NCERT Page ${{diag.ncertPage}})`;
      img.src = DIAGRAM_IMAGES[diagId] || `images/ncert_diagrams/${{diagId}}.png`;
      info.innerHTML = `
        <div style="margin-bottom:6px;"><strong>Chapter:</strong> ${{diag.chapter}}: ${{diag.chTitle}} &nbsp;|&nbsp; <strong>NCERT Page:</strong> ${{diag.ncertPage}}</div>
        <div>💡 <strong>CBSE Examiner Guidance:</strong> ${{diag.examinerTip}}</div>
      `;
      modal.classList.add("open");
      document.body.style.overflow = "hidden";
    }}

    function closeDiagramModal() {{
      const modal = document.getElementById("diagram-modal");
      if (modal) modal.classList.remove("open");
      document.body.style.overflow = "";
    }}

    window.addEventListener("keydown", (e) => {{
      if (e.key === "Escape") closeDiagramModal();
    }});

    /* SVG ILLUSTRATIONS GENERATOR FOR BIOLOGY DIAGRAMS */
    function getSvgIllustration(type, figCode) {{
      if (type === "mitochondrion") {{
        return `
          <svg width="340" height="190" viewBox="0 0 340 190" fill="none" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="170" cy="95" rx="140" ry="70" fill="#fef3c7" stroke="#b45309" stroke-width="4"/>
            <!-- Cristae folds -->
            <path d="M 50 95 C 70 60, 90 60, 110 95 C 130 130, 150 130, 170 95 C 190 60, 210 60, 230 95 C 250 130, 270 130, 290 95" stroke="#d97706" stroke-width="5" fill="none" stroke-linecap="round"/>
            <path d="M 80 80 Q 95 40 110 80" stroke="#d97706" stroke-width="4" fill="none"/>
            <path d="M 140 110 Q 155 150 170 110" stroke="#d97706" stroke-width="4" fill="none"/>
            <path d="M 200 80 Q 215 40 230 80" stroke="#d97706" stroke-width="4" fill="none"/>
            <!-- Circular DNA -->
            <circle cx="120" cy="95" r="10" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,2" fill="none"/>
            <text x="120" y="125" font-size="10" font-weight="700" fill="#dc2626" text-anchor="middle">Circular DNA</text>
            <!-- Matrix dots (Ribosomes) -->
            <circle cx="160" cy="80" r="3" fill="#0284c7"/>
            <circle cx="180" cy="115" r="3" fill="#0284c7"/>
            <circle cx="240" cy="90" r="3" fill="#0284c7"/>
            <text x="170" y="24" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">Outer Membrane (Smooth)</text>
            <line x1="170" y1="26" x2="170" y2="40" stroke="#b45309" stroke-width="1.5"/>
            <text x="270" y="165" font-size="12" font-weight="800" fill="#d97706" text-anchor="middle">Cristae (Folded Inner Membrane)</text>
            <line x1="270" y1="150" x2="250" y2="120" stroke="#d97706" stroke-width="1.5"/>
          </svg>
        `;
      }} else if (type === "chloroplast") {{
        return `
          <svg width="340" height="190" viewBox="0 0 340 190" fill="none" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="170" cy="95" rx="140" ry="70" fill="#dcfce7" stroke="#15803d" stroke-width="4"/>
            <!-- Grana stacks -->
            <g fill="#16a34a" stroke="#166534" stroke-width="1.5">
              <!-- Stack 1 -->
              <rect x="75" y="70" width="35" height="8" rx="3"/>
              <rect x="75" y="82" width="35" height="8" rx="3"/>
              <rect x="75" y="94" width="35" height="8" rx="3"/>
              <rect x="75" y="106" width="35" height="8" rx="3"/>
              <!-- Stack 2 -->
              <rect x="152" y="65" width="35" height="8" rx="3"/>
              <rect x="152" y="77" width="35" height="8" rx="3"/>
              <rect x="152" y="89" width="35" height="8" rx="3"/>
              <rect x="152" y="101" width="35" height="8" rx="3"/>
              <rect x="152" y="113" width="35" height="8" rx="3"/>
              <!-- Stack 3 -->
              <rect x="230" y="72" width="35" height="8" rx="3"/>
              <rect x="230" y="84" width="35" height="8" rx="3"/>
              <rect x="230" y="96" width="35" height="8" rx="3"/>
              <rect x="230" y="108" width="35" height="8" rx="3"/>
            </g>
            <!-- Stroma lamellae bridges -->
            <line x1="110" y1="90" x2="152" y2="89" stroke="#166534" stroke-width="2"/>
            <line x1="187" y1="101" x2="230" y2="96" stroke="#166534" stroke-width="2"/>
            <text x="92" y="145" font-size="11" font-weight="700" fill="#15803d" text-anchor="middle">Granum (Thylakoids)</text>
            <text x="210" y="50" font-size="11" font-weight="700" fill="#166534" text-anchor="middle">Stroma Lamella</text>
            <text x="170" y="170" font-size="12" font-weight="800" fill="#166534" text-anchor="middle">Fluid Stroma (Matrix)</text>
          </svg>
        `;
      }} else if (type === "nucleus") {{
        return `
          <svg width="320" height="190" viewBox="0 0 320 190" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="160" cy="95" r="75" fill="#f5f3ff" stroke="#7c3aed" stroke-width="4" stroke-dasharray="25, 8"/>
            <circle cx="160" cy="95" r="69" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="23, 10"/>
            <!-- Nucleolus -->
            <circle cx="185" cy="80" r="22" fill="#7c3aed" opacity="0.8"/>
            <text x="185" y="84" font-size="9" font-weight="800" fill="#fff" text-anchor="middle">Nucleolus</text>
            <!-- Chromatin network -->
            <path d="M 120 70 Q 140 120 160 80 T 190 120 T 140 140 T 120 100" stroke="#6d28d9" stroke-width="2" fill="none"/>
            <path d="M 135 110 Q 160 130 180 110" stroke="#6d28d9" stroke-width="1.5" fill="none"/>
            <text x="160" y="16" font-size="11" font-weight="800" fill="#7c3aed" text-anchor="middle">Nuclear Pores in Envelope</text>
            <line x1="160" y1="18" x2="160" y2="30" stroke="#7c3aed" stroke-width="1.5"/>
            <text x="80" y="150" font-size="11" font-weight="700" fill="#6d28d9">Chromatin Network</text>
          </svg>
        `;
      }} else if (type === "flower_ls") {{
        return `
          <svg width="340" height="200" viewBox="0 0 340 200" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Receptacle & Pedicel -->
            <path d="M 170 170 L 170 195" stroke="#15803d" stroke-width="6"/>
            <path d="M 140 170 C 140 150, 200 150, 200 170 Z" fill="#16a34a"/>
            <!-- Petals -->
            <path d="M 145 155 C 90 120, 80 50, 130 70 C 150 80, 160 120, 155 155 Z" fill="#f472b6" opacity="0.75"/>
            <path d="M 195 155 C 250 120, 260 50, 210 70 C 190 80, 180 120, 185 155 Z" fill="#f472b6" opacity="0.75"/>
            <!-- Ovary & Pistil -->
            <ellipse cx="170" cy="140" rx="18" ry="16" fill="#86efac" stroke="#15803d" stroke-width="2"/>
            <line x1="170" y1="124" x2="170" y2="60" stroke="#15803d" stroke-width="3.5"/>
            <ellipse cx="170" cy="58" rx="8" ry="5" fill="#16a34a"/>
            <text x="170" y="45" font-size="10" font-weight="800" fill="#15803d" text-anchor="middle">Stigma</text>
            <!-- Stamens -->
            <path d="M 152 145 Q 120 100 125 65" stroke="#ca8a04" stroke-width="2.5" fill="none"/>
            <ellipse cx="125" cy="62" rx="6" ry="4" fill="#eab308" stroke="#a16207"/>
            <path d="M 188 145 Q 220 100 215 65" stroke="#ca8a04" stroke-width="2.5" fill="none"/>
            <ellipse cx="215" cy="62" rx="6" ry="4" fill="#eab308" stroke="#a16207"/>
            <text x="100" y="55" font-size="10" font-weight="800" fill="#a16207">Anther</text>
            <text x="230" y="145" font-size="10" font-weight="800" fill="#15803d">Ovary</text>
          </svg>
        `;
      }} else {{
        return `
          <div style="text-align:center; padding:20px;">
            <div style="font-size:2.5rem; margin-bottom:8px;">📐</div>
            <div style="font-size:0.95rem; font-weight:800; color:var(--text);">${{figCode}} NCERT Reference Schematic</div>
            <div style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Direct high-resolution diagram available in NCERT Chapter PDF</div>
          </div>
        `;
      }}
    }}

    /* =========================================================================
       MODULE 3: CHEMISTRY CH 9 ION VALENCY & FORMULA BUILDER ENGINE
       ========================================================================= */
    const ALL_CATIONS = [
      ...CHEMISTRY_TABLE_9_1_DATA.table_a_monoatomic.filter(i => i.type === "cation"),
      ...CHEMISTRY_TABLE_9_1_DATA.table_b_polyatomic.filter(i => i.type === "cation")
    ];

    const ALL_ANIONS = [
      ...CHEMISTRY_TABLE_9_1_DATA.table_a_monoatomic.filter(i => i.type === "anion"),
      ...CHEMISTRY_TABLE_9_1_DATA.table_b_polyatomic.filter(i => i.type === "anion")
    ];

    function initChemistryBuilder() {{
      const catSelect = document.getElementById("builder-cation-select");
      const anSelect = document.getElementById("builder-anion-select");
      if (!catSelect || !anSelect) return;

      catSelect.innerHTML = ALL_CATIONS.map((c, idx) => `
        <option value="${{idx}}">${{c.name}} (${{c.formula}} — Valency ${{c.valency}})</option>
      `).join("");

      anSelect.innerHTML = ALL_ANIONS.map((a, idx) => `
        <option value="${{idx}}">${{a.name}} (${{a.formula}} — Valency ${{a.valency}})</option>
      `).join("");

      // Set default to Aluminium and Sulfate for a rich showcase
      const alIdx = ALL_CATIONS.findIndex(c => c.symbol === "Al");
      const so4Idx = ALL_ANIONS.findIndex(a => a.symbol === "SO₄");
      if (alIdx >= 0) catSelect.value = alIdx;
      if (so4Idx >= 0) anSelect.value = so4Idx;

      catSelect.addEventListener("change", updateFormulaDerivation);
      anSelect.addEventListener("change", updateFormulaDerivation);

      updateFormulaDerivation();
      renderIonMatrixTable("all");
      initFormulaQuizzer();
    }}

    function gcd(a, b) {{
      return b === 0 ? a : gcd(b, a % b);
    }}

    function toSubscript(num) {{
      const subs = {{ '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉' }};
      return String(num).split('').map(d => subs[d] || d).join('');
    }}

    function updateFormulaDerivation() {{
      const catIdx = parseInt(document.getElementById("builder-cation-select").value, 10);
      const anIdx = parseInt(document.getElementById("builder-anion-select").value, 10);

      const cation = ALL_CATIONS[catIdx];
      const anion = ALL_ANIONS[anIdx];
      if (!cation || !anion) return;

      document.getElementById("disp-cation-sym").textContent = cation.symbol;
      document.getElementById("disp-cation-val").textContent = `Valency: ${{cation.valency}}`;

      document.getElementById("disp-anion-sym").textContent = anion.symbol;
      document.getElementById("disp-anion-val").textContent = `Valency: ${{anion.valency}}`;

      // Criss-cross math
      let cSub = anion.valency;
      let aSub = cation.valency;

      const common = gcd(cSub, aSub);
      cSub /= common;
      aSub /= common;

      // Polyatomic formatting rules
      let catFormatted = cation.symbol;
      if (cSub > 1) {{
        catFormatted = cation.poly ? `(${{cation.symbol}})${{toSubscript(cSub)}}` : `${{cation.symbol}}${{toSubscript(cSub)}}`;
      }}

      let anFormatted = anion.symbol;
      if (aSub > 1) {{
        anFormatted = anion.poly ? `(${{anion.symbol}})${{toSubscript(aSub)}}` : `${{anion.symbol}}${{toSubscript(aSub)}}`;
      }}

      const finalFormula = `${{catFormatted}}${{anFormatted}}`;
      const compoundName = `${{cation.name}} ${{anion.name.toLowerCase()}}`;

      document.getElementById("disp-compound-name").textContent = compoundName;
      document.getElementById("disp-compound-formula").textContent = finalFormula;

      let ruleText = `Criss-cross: ${{cation.symbol}} receives valency ${{anion.valency}}, ${{anion.symbol}} receives valency ${{cation.valency}}.`;
      if (common > 1) {{
        ruleText += ` Subscripts simplified by common factor of ${{common}}.`;
      }}
      if ((cation.poly && cSub > 1) || (anion.poly && aSub > 1)) {{
        ruleText += ` Enclosed polyatomic ion in parentheses because its subscript > 1.`;
      }}
      document.getElementById("disp-bracket-rule").textContent = ruleText;
    }}

    function renderIonMatrixTable(filter) {{
      const tbody = document.getElementById("ion-matrix-tbody");
      if (!tbody) return;
      tbody.innerHTML = "";

      const allIons = [
        ...CHEMISTRY_TABLE_9_1_DATA.table_a_monoatomic.map(i => ({{ ...i, source: "9.1(a) Monoatomic" }})),
        ...CHEMISTRY_TABLE_9_1_DATA.table_b_polyatomic.map(i => ({{ ...i, source: "9.1(b) Polyatomic" }}))
      ];

      const filtered = allIons.filter(i => {{
        if (filter === "mono") return !i.poly;
        if (filter === "poly") return !!i.poly;
        if (filter === "val1") return i.valency === 1;
        if (filter === "val2") return i.valency === 2;
        if (filter === "val3") return i.valency === 3;
        return true;
      }});

      filtered.forEach(i => {{
        const row = document.createElement("tr");
        const valClass = i.valency === 1 ? "val-1" : i.valency === 2 ? "val-2" : "val-3";
        row.innerHTML = `
          <td><strong>${{i.name}}</strong></td>
          <td style="font-weight:800; color:var(--chem-color);">${{i.formula}}</td>
          <td>${{i.charge}}</td>
          <td><span class="val-badge ${{valClass}}">${{i.valency}}</span></td>
          <td style="font-size:0.8rem; color:var(--text-muted);">${{i.source}} (${{i.type}})</td>
        `;
        tbody.appendChild(row);
      }});
    }}

    /* FORMULA QUIZZER */
    let currentQuizIndex = 0;
    const QUIZ_ITEMS = CHEMISTRY_TABLE_9_1_DATA.quiz_compounds;

    function initFormulaQuizzer() {{
      currentQuizIndex = 0;
      loadQuizQuestion(currentQuizIndex);

      document.getElementById("btn-next-quiz")?.addEventListener("click", () => {{
        currentQuizIndex = (currentQuizIndex + 1) % QUIZ_ITEMS.length;
        loadQuizQuestion(currentQuizIndex);
      }});

      document.getElementById("btn-restart-quiz")?.addEventListener("click", () => {{
        currentQuizIndex = Math.floor(Math.random() * QUIZ_ITEMS.length);
        loadQuizQuestion(currentQuizIndex);
      }});
    }}

    function loadQuizQuestion(idx) {{
      const q = QUIZ_ITEMS[idx];
      if (!q) return;

      document.getElementById("quiz-index-stat").textContent = idx + 1;
      document.getElementById("quiz-total-stat").textContent = QUIZ_ITEMS.length;
      document.getElementById("quiz-question-text").textContent = `What is the chemical formula for ${{q.name}}?`;

      const feedback = document.getElementById("quiz-feedback-box");
      feedback.style.display = "none";
      document.getElementById("btn-next-quiz").style.display = "none";

      // Generate 3 plausible distractors
      const distractors = new Set([q.formula]);
      // Variations: inverted subscripts, missing brackets, unsimplified
      distractors.add(`${{q.cation}}${{q.anion}}`);
      distractors.add(`${{q.cation}}${{toSubscript(q.aVal)}}${{q.anion}}${{toSubscript(q.cVal)}}`);
      distractors.add(`${{q.cation}}${{q.anion}}${{toSubscript(q.cVal)}}`);
      if (q.isPoly) {{
        distractors.add(`${{q.cation}}${{q.anion}}${{q.cVal}}`);
      }}

      const optionsArray = Array.from(distractors).slice(0, 4).sort(() => Math.random() - 0.5);

      const container = document.getElementById("quiz-options-container");
      container.innerHTML = "";

      optionsArray.forEach(opt => {{
        const btn = document.createElement("button");
        btn.className = "btn-quiz-opt";
        btn.textContent = opt;
        btn.addEventListener("click", () => handleQuizAnswer(opt, q.formula, q.rule));
        container.appendChild(btn);
      }});
    }}

    function handleQuizAnswer(selected, correct, rule) {{
      const container = document.getElementById("quiz-options-container");
      const buttons = container.querySelectorAll(".btn-quiz-opt");
      const feedback = document.getElementById("quiz-feedback-box");

      buttons.forEach(btn => {{
        btn.disabled = true;
        if (btn.textContent === correct) {{
          btn.classList.add("correct");
        }} else if (btn.textContent === selected) {{
          btn.classList.add("wrong");
        }}
      }});

      feedback.style.display = "block";
      if (selected === correct) {{
        feedback.style.background = "#dcfce7";
        feedback.style.color = "#166534";
        feedback.innerHTML = `✅ <strong>Nailed it!</strong> Correct formula: <code>${{correct}}</code>. ${{rule ? '<br>' + rule : ''}}`;
      }} else {{
        feedback.style.background = "#fee2e2";
        feedback.style.color = "#991b1b";
        feedback.innerHTML = `❌ <strong>Not quite!</strong> Correct formula is <code>${{correct}}</code>. ${{rule ? '<br>Explanation: ' + rule : ''}}`;
      }}

      document.getElementById("btn-next-quiz").style.display = "inline-flex";
    }}

    /* =========================================================================
       GENERAL NAVIGATION & TOAST
       ========================================================================= */
    function showToast(msg) {{
      const toast = document.getElementById("toast-el");
      if (!toast) return;
      toast.textContent = msg;
      toast.style.display = "block";
      setTimeout(() => {{ toast.style.display = "none"; }}, 2500);
    }}

    function setupApp() {{
      // Module Tab Switcher
      document.querySelectorAll(".module-tab-btn").forEach(btn => {{
        btn.addEventListener("click", () => {{
          document.querySelectorAll(".module-tab-btn").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");

          const mod = btn.dataset.mod;
          document.getElementById("module-glossary").style.display = mod === "glossary" ? "block" : "none";
          document.getElementById("module-diagrams").style.display = mod === "diagrams" ? "block" : "none";
          document.getElementById("module-chemistry").style.display = mod === "chemistry" ? "block" : "none";

          window.scrollTo({{ top: 0, behavior: "smooth" }});
        }});
      }});

      // Glossary Filters
      document.getElementById("terms-search-input")?.addEventListener("input", renderGlossary);

      document.querySelectorAll("[data-filter-sub]").forEach(btn => {{
        btn.addEventListener("click", () => {{
          document.querySelectorAll("[data-filter-sub]").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          currentGlossarySubFilter = btn.dataset.filterSub;
          renderGlossary();
        }});
      }});

      document.getElementById("chapter-select-jump")?.addEventListener("change", renderGlossary);

      document.getElementById("btn-starred-filter")?.addEventListener("click", (e) => {{
        showStarredOnly = !showStarredOnly;
        e.currentTarget.classList.toggle("active", showStarredOnly);
        renderGlossary();
      }});

      let allExpanded = true;
      document.getElementById("btn-toggle-all-accordions")?.addEventListener("click", (e) => {{
        allExpanded = !allExpanded;
        e.currentTarget.textContent = allExpanded ? "⇕ Collapse All" : "⇕ Expand All";
        document.querySelectorAll(".chapter-body").forEach(b => {{
          b.classList.toggle("collapsed", !allExpanded);
          const arrow = b.previousElementSibling?.querySelector(".accordion-arrow");
          if (arrow) arrow.textContent = allExpanded ? "▾" : "▸";
        }});
      }});

      // Diagrams Filters
      document.getElementById("diagrams-search-input")?.addEventListener("input", renderBiologyDiagrams);

      document.querySelectorAll("[data-filter-diag]").forEach(btn => {{
        btn.addEventListener("click", () => {{
          document.querySelectorAll("[data-filter-diag]").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          currentDiagFilter = btn.dataset.filterDiag;
          renderBiologyDiagrams();
        }});
      }});

      document.getElementById("btn-toggle-all-recall")?.addEventListener("click", (e) => {{
        isRecallModeActive = !isRecallModeActive;
        e.currentTarget.classList.toggle("active", isRecallModeActive);
        document.querySelectorAll(".labels-checklist").forEach(c => {{
          c.classList.toggle("test-hidden", isRecallModeActive);
        }});
        document.querySelectorAll(".diagram-visual-box").forEach(b => {{
          b.classList.toggle("recall-hidden", isRecallModeActive);
          b.classList.remove("revealed");
        }});
        document.querySelectorAll(".btn-recall-toggle").forEach(b => {{
          b.classList.toggle("active", isRecallModeActive);
        }});
      }});

      // Ion Table Filter
      document.querySelectorAll("[data-ion-table-filter]").forEach(btn => {{
        btn.addEventListener("click", () => {{
          document.querySelectorAll("[data-ion-table-filter]").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          renderIonMatrixTable(btn.dataset.ionTableFilter);
        }});
      }});

      // Theme Toggle
      document.getElementById("btn-theme-toggle")?.addEventListener("click", () => {{
        const current = document.documentElement.getAttribute("data-theme") || "light";
        const next = current === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", next);
        try {{ localStorage.setItem(STORAGE_KEY_THEME, next); }} catch (e) {{}}
      }});

      const savedTheme = localStorage.getItem(STORAGE_KEY_THEME);
      if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);

      // Initial stats
      document.getElementById("mod-terms-count").textContent = KEY_TERMS_DATA.length;
      updateStarredCount();

      renderGlossary();
      renderBiologyDiagrams();
      initChemistryBuilder();
    }}

    window.addEventListener("DOMContentLoaded", setupApp);
  </script>

  <!-- DIAGRAM LIGHTBOX MODAL -->
  <div id="diagram-modal" class="modal-overlay" onclick="closeDiagramModal()">
    <div class="modal-card" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeDiagramModal()" title="Close (Esc)">✕</button>
      <div id="modal-title" class="modal-header-title"></div>
      <div class="modal-img-container">
        <img id="modal-img" src="" alt="High-Resolution Diagram" />
      </div>
      <div id="modal-info" class="modal-info-box"></div>
    </div>
  </div>
</body>
</html>
"""

    OUTPUT_HTML.write_text(html_template, encoding="utf-8")
    print(f"🎉 Generated {OUTPUT_HTML.name} ({len(html_template) / 1024:.1f} KB)")

    # Sync to public/ directory for Cloudflare deployment
    public_dir = ROOT / "public"
    public_dir.mkdir(exist_ok=True)
    (public_dir / OUTPUT_HTML.name).write_text(html_template, encoding="utf-8")
    for src_name in ["index.html", "study_science_dashboard.html", "study_math_dashboard.html"]:
        src_path = ROOT / src_name
        if src_path.exists():
            (public_dir / src_name).write_text(src_path.read_text(encoding="utf-8"), encoding="utf-8")
    if (ROOT / "images").exists():
        import shutil
        shutil.copytree(ROOT / "images", public_dir / "images", dirs_exist_ok=True)
    print("📁 Synced static portal distribution to public/")

if __name__ == "__main__":
    generate_refresher()
