"""Recompute pre-adjudication agreement and kappa for Table 1."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    "resource_category": ("resource_category_aligned", "resource_category"),
    "scoring_method": ("scoring_method_aligned", "scoring_method_aligned"),
    "answer_solicitation_pressure": (
        "answer_solicitation_pressure",
        "answer_solicitation_pressure",
    ),
}


def read_codes(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def kappa(a: list[str], b: list[str]) -> dict[str, object]:
    if len(a) != len(b) or not a:
        raise ValueError("Coding vectors must be non-empty and equal length")
    n = len(a)
    observed = sum(x == y for x, y in zip(a, b)) / n
    a_counts = Counter(a)
    b_counts = Counter(b)
    expected = sum(a_counts[x] * b_counts[x] for x in set(a) | set(b)) / (n * n)
    return {
        "n": n,
        "agreements": sum(x == y for x, y in zip(a, b)),
        "observed_agreement": observed,
        "expected_agreement": expected,
        "cohen_kappa_unweighted": (observed - expected) / (1 - expected),
    }


def main() -> None:
    a_rows = read_codes(ROOT / "data/table1_coding_A.csv")
    b_rows = read_codes(ROOT / "data/table1_coding_B.csv")
    if [row["item_id"] for row in a_rows] != [row["item_id"] for row in b_rows]:
        raise ValueError("A/B item identifiers do not align")
    for label, (a_column, b_column) in FIELDS.items():
        print(label, kappa([row[a_column] for row in a_rows], [row[b_column] for row in b_rows]))


if __name__ == "__main__":
    main()
