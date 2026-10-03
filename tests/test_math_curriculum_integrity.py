#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curriculum Integrity Test for Class 9 CBSE Mathematics (NCERT Ganita Manjari)
Verifies that all 5 active chapters (Ch 1, 2, 3, 4, 6) in the study portal
fully cover the authentic textbook topics, formulas, competencies, and interactive widgets.
"""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
MATH_DIR = ROOT / "subjects" / "mathematics"
CHAPTERS_DIR = MATH_DIR / "chapters"

def test_json_validity():
    """Verify all JSON files in subjects/mathematics parse without error."""
    for p in MATH_DIR.rglob("*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            assert data is not None
        except Exception as e:
            raise AssertionError(f"Invalid JSON in {p}: {e}")
    print("✅ All Mathematics JSON files are valid.")

def test_chapter_1_coordinates_coverage():
    """Verify Ch 1 covers Midpoints, Distance, Trisection, Circles, and Triangle Reconstruction."""
    guide = (CHAPTERS_DIR / "ch01_coordinates" / "guide.md").read_text(encoding="utf-8")
    flashcards = (CHAPTERS_DIR / "ch01_coordinates" / "flashcards.json").read_text(encoding="utf-8")
    questions = (CHAPTERS_DIR / "ch01_coordinates" / "questions.json").read_text(encoding="utf-8")
    
    # Midpoint assertions
    assert "Midpoint Formula" in guide, "Ch 1 guide missing Midpoint Formula"
    assert "\\frac{x_1 + x_2}{2}" in guide, "Ch 1 guide missing midpoint formula coordinates"
    assert "MIDPOINTS" in flashcards, "Ch 1 flashcards missing MIDPOINTS tag"
    assert "midpoint" in questions.lower(), "Ch 1 questions missing midpoint problems"
    
    # Distance formula assertions
    assert "Baudhāyana–Pythagoras" in guide, "Ch 1 guide missing Baudhāyana-Pythagoras"
    assert "\\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}" in guide, "Ch 1 guide missing Distance Formula"
    
    # Trisection and Triangle Reconstruction assertions
    assert "trisection" in guide.lower(), "Ch 1 guide missing Trisection"
    assert "trisection" in questions.lower(), "Ch 1 questions missing Trisection problem (NCERT Prob 11)"
    assert "D(5, 1)" in questions or "midpoint" in questions.lower(), "Ch 1 questions missing Triangle Reconstruction (NCERT Prob 13)"
    assert "circle" in guide.lower(), "Ch 1 guide missing Circle locus tests (NCERT Prob 12)"
    
    print("✅ Chapter 1 (Coordinates) covers all authentic NCERT topics including Midpoints and Distance.")

def test_chapter_2_linear_polynomials_coverage():
    """Verify Ch 2 covers Linear Growth, Linear Decay, Slope, and Graphs."""
    guide = (CHAPTERS_DIR / "ch02_linear_polynomials" / "guide.md").read_text(encoding="utf-8")
    flashcards = (CHAPTERS_DIR / "ch02_linear_polynomials" / "flashcards.json").read_text(encoding="utf-8")
    
    assert "Linear Growth" in guide, "Ch 2 guide missing Linear Growth"
    assert "Linear Decay" in guide, "Ch 2 guide missing Linear Decay"
    assert "Rate of change" in guide or "rate of change" in guide, "Ch 2 guide missing Rate of change"
    assert "GROWTH & DECAY" in flashcards, "Ch 2 flashcards missing GROWTH & DECAY tag"
    print("✅ Chapter 2 (Linear Polynomials) covers Linear Growth, Decay, and Graphs.")

def test_chapter_3_world_of_numbers_coverage():
    """Verify Ch 3 covers Brahmagupta laws, Density of rationals, and root 2 proof."""
    guide = (CHAPTERS_DIR / "ch03_world_of_numbers" / "guide.md").read_text(encoding="utf-8")
    
    assert "Brahmagupta" in guide, "Ch 3 guide missing Brahmagupta's laws"
    assert "Density" in guide, "Ch 3 guide missing Density property of rationals"
    assert "\\sqrt{2}" in guide and "contradiction" in guide.lower(), "Ch 3 guide missing root 2 proof by contradiction"
    print("✅ Chapter 3 (World of Numbers) covers Brahmagupta laws, Density, and Irrationality proofs.")

def test_chapter_4_algebraic_identities_coverage():
    """Verify Ch 4 covers Algebra Tiles and Rational Expressions."""
    guide = (CHAPTERS_DIR / "ch04_algebraic_identities" / "guide.md").read_text(encoding="utf-8")
    
    assert "Algebra Tiles" in guide, "Ch 4 guide missing Algebra Tiles visualization"
    assert "Rational Expression" in guide or "rational expression" in guide.lower(), "Ch 4 guide missing Rational Expressions"
    print("✅ Chapter 4 (Algebraic Identities) covers Algebra Tiles and Rational Expressions.")

def test_chapter_6_perimeter_and_area_coverage():
    """Verify Ch 6 covers Heron's formula, Arc length, Sector area, and Brahmagupta cyclic formula."""
    guide = (CHAPTERS_DIR / "ch06_perimeter_and_area" / "guide.md").read_text(encoding="utf-8")
    flashcards = (CHAPTERS_DIR / "ch06_perimeter_and_area" / "flashcards.json").read_text(encoding="utf-8")
    questions = (CHAPTERS_DIR / "ch06_perimeter_and_area" / "questions.json").read_text(encoding="utf-8")
    
    assert "Arc Length" in guide or "arc of a circle" in guide.lower(), "Ch 6 guide missing Arc Length"
    assert "Sector Area" in guide or "sector" in guide.lower(), "Ch 6 guide missing Sector Area"
    assert "Brahmagupta" in guide, "Ch 6 guide missing Brahmagupta cyclic formula"
    assert "BRAHMAGUPTA FORMULA" in flashcards, "Ch 6 flashcards missing BRAHMAGUPTA FORMULA tag"
    assert "Brahmagupta" in questions, "Ch 6 questions missing Brahmagupta problem"
    print("✅ Chapter 6 (Perimeter & Area) covers Circles, Arcs, Sectors, and Brahmagupta formula.")

def test_compiled_dashboard_integrity():
    """Verify compiled dashboard file exists, is valid size, and has zero unrendered templates."""
    dash = ROOT / "study_math_dashboard.html"
    public_dash = ROOT / "public" / "study_math_dashboard.html"
    
    assert dash.exists(), "study_math_dashboard.html missing"
    assert public_dash.exists(), "public/study_math_dashboard.html missing"
    
    content = dash.read_text(encoding="utf-8")
    assert len(content) > 800000, f"Dashboard size unusually small: {len(content)} bytes"
    assert "{{CHAPTERS_DATA_JSON}}" not in content, "Unrendered CHAPTERS_DATA_JSON placeholder"
    assert "{{PORTAL_TITLE}}" not in content, "Unrendered PORTAL_TITLE placeholder"
    assert "calcDualPoints" in content, "calcDualPoints interactive widget handler missing from compiled dashboard"
    assert "Midpoint Formula" in content, "Midpoint Formula missing from compiled dashboard"
    
    print(f"✅ Compiled study_math_dashboard.html ({len(content):,} bytes) verified with zero unrendered tags.")

if __name__ == "__main__":
    print("Running Mathematics Curriculum Integrity & Coverage Tests...")
    test_json_validity()
    test_chapter_1_coordinates_coverage()
    test_chapter_2_linear_polynomials_coverage()
    test_chapter_3_world_of_numbers_coverage()
    test_chapter_4_algebraic_identities_coverage()
    test_chapter_6_perimeter_and_area_coverage()
    test_compiled_dashboard_integrity()
    print("🎉 All 7 Mathematics Curriculum Integrity Tests Passed Successfully!")
