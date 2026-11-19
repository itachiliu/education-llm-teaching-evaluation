"""Recompute pre-adjudication agreement and kappa for Table 1."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    "resource_category": ("base", "resource_category_aligned", "resource_category"),
    "observation_unit": ("extra", "observation_unit", "observation_unit"),
    "scoring_method": ("base", "scoring_method_aligned", "scoring_method_aligned"),
    "answer_solicitation_pressure": (
        "base",
        "answer_solicitation_pressure",
        "answer_solicitation_pressure",
    ),
    "primary_evidence_endpoint": (
        "extra",
        "primary_evidence_endpoint",
        "primary_evidence_endpoint",
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
        "a_counts": dict(sorted(a_counts.items())),
        "b_counts": dict(sorted(b_counts.items())),
    }


def by_item(rows: list[dict[str, str]]) -> dict[int, dict[str, str]]:
    return {int(row["item_id"]): row for row in rows}


def main() -> None:
    args = argparse.ArgumentParser()
    args.add_argument("--write-json", action="store_true")
    options = args.parse_args()

    base_a = by_item(read_codes(ROOT / "data/table1_coding_A.csv"))
    base_b = by_item(read_codes(ROOT / "data/table1_coding_B.csv"))
    extra_a = by_item(read_codes(ROOT / "data/table1_extra_coding_A.csv"))
    extra_b = by_item(read_codes(ROOT / "data/table1_extra_coding_B.csv"))
    expected_ids = set(range(1, 22))
    for label, rows in (
        ("base A", base_a),
        ("base B", base_b),
        ("extra A", extra_a),
        ("extra B", extra_b),
    ):
        if set(rows) != expected_ids:
            raise ValueError(f"{label} item identifiers do not cover Table 1")

    sources = {
        "base": (base_a, base_b),
        "extra": (extra_a, extra_b),
    }
    result: dict[str, object] = {
        "sample_unit": "purposefully selected Table 1 resource",
        "n": 21,
        "codebook_date": "2026-11-19",
    }
    for label, (source, a_column, b_column) in FIELDS.items():
        a_rows, b_rows = sources[source]
        field_result = kappa(
            [a_rows[item_id][a_column] for item_id in sorted(expected_ids)],
            [b_rows[item_id][b_column] for item_id in sorted(expected_ids)],
        )
        result[label] = field_result
        print(label, field_result)

    old_disputes = read_codes(ROOT / "data/table1_adjudication.csv")
    extra_disputes = read_codes(ROOT / "data/table1_adjudication_extra.csv")
    result["total_field_disagreements"] = len(old_disputes) + len(extra_disputes)
    result["interpretation"] = (
        "Descriptive pre-adjudication agreement for 21 purposively selected resources; "
        "the values are not random-sample reliability estimates for the field."
    )
    result["post_adjudication"] = {
        "missing_codes": 0,
        "interpretation": (
            "Final values replace disagreements for the Table 1 dataset. "
            "The resulting consensus is definitional and must not be reported as "
            "a new independent reliability estimate."
        ),
    }
    if options.write_json:
        output = ROOT / "results/table1_kappa.json"
        output.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {output}")


if __name__ == "__main__":
    main()
