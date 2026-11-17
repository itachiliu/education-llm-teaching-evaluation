"""Recompute semantic-label counts from the public minimal data."""

from collections import Counter
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def compute() -> dict[str, object]:
    with (ROOT / "data" / "final_labels_177.csv").open(
        encoding="utf-8-sig", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 177
    assert len({row["样本ID"] for row in rows}) == 177

    return {
        "rows": len(rows),
        "label_source_counts": dict(Counter(row["标签来源"] for row in rows)),
        "final_label_counts": {
            "数值是否出现": dict(Counter(row["数值是否出现"] for row in rows)),
            "数值角色": dict(Counter(row["数值角色"] for row in rows)),
            "学习者此前是否已得出答案": dict(
                Counter(row["学习者此前是否已得出答案"] for row in rows)
            ),
            "明确答案披露标签": dict(
                Counter(row["明确答案披露标签"] for row in rows)
            ),
            "疑似隐性披露": dict(Counter(row["疑似隐性披露"] for row in rows)),
        },
        "automatic_label_cross_semantic_disclosure": {
            f"auto_{auto}_final_{final}": count
            for (auto, final), count in sorted(
                Counter(
                    (row["自动标签"], row["明确答案披露标签"])
                    for row in rows
                ).items()
            )
        },
    }


def main() -> None:
    print(json.dumps(compute(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
