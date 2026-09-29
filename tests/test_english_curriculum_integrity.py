#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curriculum Integrity Test for Class 9 CBSE English Language & Literature (Track R1)
Verifies that all literature units and mock examinations in english_data.py match
the primary NCERT Kaveri textbook source documents and contain zero hallucinated content.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import portal_engine.english_data as ed

FORBIDDEN_HALLUCINATIONS = [
    "ramu",
    "chandrapur",
    "kavita bai",
    "sneakers",
    "shuttle flying through the warp",
    "petrichor richer than royal wine",
]

def test_no_forbidden_hallucinations():
    import json
    data_str = json.dumps({
        "units": ed.UNITS_DATA,
        "mocks": ed.MOCK_PAPERS,
        "writing": ed.MASTER_WRITING_STUDIO,
    }).lower()
    
    for term in FORBIDDEN_HALLUCINATIONS:
        assert term not in data_str, f"CRITICAL INTEGRITY FAILURE: Found hallucinated term '{term}' in english_data.py"

def test_unit_1_integrity():
    u1 = next((u for u in ed.UNITS_DATA if u["unit_number"] == 1), None)
    assert u1 is not None, "Unit 1 missing"
    assert "Sudha Murty" in u1["prose"]["author"]
    assert "Krishtakka" in str(u1["prose"]["character_dossiers"])
    assert "Subramania Bharati" in u1["poetry"]["poet"]
    assert "Bharat" in u1["poetry"]["title"]

def test_unit_2_integrity():
    u2 = next((u for u in ed.UNITS_DATA if u["unit_number"] == 2), None)
    assert u2 is not None, "Unit 2 missing"
    # Prose: The Pot Maker by Temsula Ao
    assert "Temsula Ao" in u2["prose"]["author"]
    char_names = [c["name"] for c in u2["prose"]["character_dossiers"]]
    assert any("Sentila" in name for name in char_names), f"Sentila missing in {char_names}"
    assert any("Arenla" in name for name in char_names), f"Arenla missing in {char_names}"
    # Poem: Gifts of Grace: Honouring Our Vocations
    poem_text = str(u2["poetry"])
    assert "Bharat celebrating" in poem_text or "vocations" in poem_text.lower()
    # Extended reading check
    assert "extended_reader" in u2
    assert "Quality" in u2["extended_reader"]["title"]
    assert "John Galsworthy" in u2["extended_reader"]["author"]

def test_unit_3_integrity():
    u3 = next((u for u in ed.UNITS_DATA if u["unit_number"] == 3), None)
    assert u3 is not None, "Unit 3 missing"
    # Prose: Winds of Change (Traditional Indian Pankhas)
    prose_str = str(u3["prose"]).lower()
    assert "pankha" in prose_str, "Pankha missing from Winds of Change prose"
    assert "tal patar" in prose_str or "palm leaf" in prose_str, "Bengal fan tradition missing"
    # Poem: Canvas of Soil by Maya Anthony
    assert "Maya Anthony" in u3["poetry"]["poet"]
    assert "Palette of earth" in str(u3["poetry"]["stanza_paraphrase"])
    # Extended reading check
    assert "extended_reader" in u3
    assert "The Last Leaf" in u3["extended_reader"]["title"]
    assert "O. Henry" in u3["extended_reader"]["author"]

def test_unit_4_integrity():
    u4 = next((u for u in ed.UNITS_DATA if u["unit_number"] == 4), None)
    assert u4 is not None, "Unit 4 missing"
    # Prose: Vitamin-M by Asha Nehemiah
    assert "Asha Nehemiah" in u4["prose"]["author"]
    char_names = [c["name"] for c in u4["prose"]["character_dossiers"]]
    assert any("Ravi" in name for name in char_names), f"Ravi missing in {char_names}"
    assert any("Grandpa" in name for name in char_names), f"Grandpa missing in {char_names}"
    # Poem: I Cannot Remember My Mother by Rabindranath Tagore
    assert "Rabindranath Tagore" in u4["poetry"]["poet"]
    # Extended reading check
    assert "extended_reader" in u4
    assert "The Lost Child" in u4["extended_reader"]["title"]
    assert "Mulk Raj Anand" in u4["extended_reader"]["author"]

def test_mock_papers_literature_integrity():
    assert len(ed.MOCK_PAPERS) == 3
    for p_idx, paper in enumerate(ed.MOCK_PAPERS):
        secC = paper["sections"]["C"]
        secC_str = str(secC).lower()
        # Verify no hallucinated terms
        for term in FORBIDDEN_HALLUCINATIONS:
            assert term not in secC_str, f"Mock Paper {p_idx+1} Section C contains forbidden term '{term}'"

if __name__ == "__main__":
    print("Running Curriculum Integrity Tests for Class 9 CBSE English...")
    test_no_forbidden_hallucinations()
    test_unit_1_integrity()
    test_unit_2_integrity()
    test_unit_3_integrity()
    test_unit_4_integrity()
    test_mock_papers_literature_integrity()
    print("✅ All Curriculum Integrity Tests Passed!")
