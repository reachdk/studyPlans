#!/usr/bin/env python3
"""Download the current English-medium NCERT Grade 9 core textbooks by chapter."""

from pathlib import Path
from shutil import copyfileobj
from urllib.request import Request, urlopen


BASE_URL = "https://ncert.nic.in/textbook/pdf"
OUTPUT_DIR = Path(__file__).parent / "downloads/class-09"
TIMEOUT_SECONDS = 60

# Official contents verified 2026-08-09:
# https://ncert.nic.in/textbook/pdf/iesc1ps.pdf
# https://ncert.nic.in/textbook/pdf/iebe1ps.pdf
# https://ncert.nic.in/textbook/pdf/iemh1ps.pdf
# https://ncert.nic.in/textbook/pdf/iest1ps.pdf
BOOKS = (
    (
        "science/exploration",
        "iesc1",
        (
            "exploration-entering-the-world-of-secondary-science",
            "cell-the-building-block-of-life",
            "tissues-in-action",
            "describing-motion-around-us",
            "exploring-mixtures-and-their-separation",
            "how-forces-affect-motion",
            "work-energy-and-simple-machines",
            "journey-inside-the-atom",
            "atomic-foundations-of-matter",
            "sound-waves-characteristics-and-applications",
            "reproduction-how-life-continues",
            "patterns-in-life-diversity-and-classification",
            "earth-as-a-system-energy-matter-and-life",
        ),
    ),
    (
        "english/kaveri",
        "iebe1",
        (
            "how-i-taught-my-grandmother-to-read",
            "the-pot-maker",
            "winds-of-change",
            "vitamin-m",
            "the-world-of-limitless-possibilities",
            "twin-melodies",
            "carrier-of-words",
            "follow-that-dream",
        ),
    ),
    (
        "mathematics/ganita-manjari",
        "iemh1",
        (
            "orienting-yourself-the-use-of-coordinates",
            "introduction-to-linear-polynomials",
            "the-world-of-numbers",
            "exploring-algebraic-identities",
            "im-up-and-down-and-round-and-round",
            "measuring-space-perimeter-and-area",
            "the-mathematics-of-maybe-introduction-to-probability",
            "predicting-what-comes-next-exploring-sequences-and-progressions",
        ),
    ),
    (
        "social-science/understanding-society-india-and-beyond-part-1",
        "iest1",
        (
            "understanding-social-science",
            "shaping-of-the-earths-surface",
            "atmosphere-and-climate",
            "early-humans-and-beginning-of-civilisation",
            "state-and-society-up-to-1000-ce",
            "democracy",
            "elections",
            "building-blocks-in-economics-the-problem-of-choice",
            "the-price-puzzle-what-drives-the-market",
        ),
    ),
)


def is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as pdf:
            if pdf.read(5) != b"%PDF-":
                return False
            pdf.seek(max(0, path.stat().st_size - 4096))
            return b"%%EOF" in pdf.read()
    except OSError:
        return False


def entries():
    for folder, prefix, titles in BOOKS:
        for number, title in enumerate(titles, 1):
            yield folder, f"{prefix}{number:02d}", title


def target_path(folder: str, code: str, title: str) -> Path:
    return OUTPUT_DIR / folder / f"{code}--{title}.pdf"


def verify_catalogue() -> None:
    chapters = list(entries())
    codes = [code for _, code, _ in chapters]
    assert [len(titles) for _, _, titles in BOOKS] == [13, 8, 8, 9]
    assert len(codes) == len(set(codes)) == 38


def download(folder: str, code: str, title: str) -> str:
    target = target_path(folder, code, title)
    if is_pdf(target):
        return "skipped"

    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_suffix(".pdf.part")
    partial.unlink(missing_ok=True)
    try:
        request = Request(f"{BASE_URL}/{code}.pdf", headers={"User-Agent": "studyPlans/1.0"})
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response, partial.open("wb") as output:
            copyfileobj(response, output)
        if not is_pdf(partial):
            raise ValueError("response is not a complete PDF")
        partial.replace(target)
        return "downloaded"
    except Exception:
        partial.unlink(missing_ok=True)
        raise


def verify_output() -> list[str]:
    problems = []
    for folder, prefix, titles in BOOKS:
        book_entries = [(folder, f"{prefix}{number:02d}", title) for number, title in enumerate(titles, 1)]
        expected = {target_path(*chapter).name for chapter in book_entries}
        book_dir = OUTPUT_DIR / folder
        actual = {path.name for path in book_dir.glob("*.pdf")}
        problems += [f"missing: {folder}/{name}" for name in sorted(expected - actual)]
        problems += [f"unexpected: {folder}/{name}" for name in sorted(actual - expected)]
        problems += [
            f"invalid: {folder}/{name}"
            for name in sorted(actual & expected)
            if not is_pdf(book_dir / name)
        ]
        problems += [f"partial: {folder}/{path.name}" for path in sorted(book_dir.glob("*.part"))]
    return problems


def main() -> int:
    verify_catalogue()
    totals = {"downloaded": 0, "skipped": 0, "failed": 0}

    for folder, code, title in entries():
        try:
            result = download(folder, code, title)
            totals[result] += 1
            print(f"{result:10} {folder}/{target_path(folder, code, title).name}")
        except Exception as error:
            totals["failed"] += 1
            print(f"failed     {folder}/{code}.pdf: {error}")

    problems = verify_output()
    for problem in problems:
        print(problem)
    print(" ".join(f"{name}={count}" for name, count in totals.items()))
    return 1 if totals["failed"] or problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
