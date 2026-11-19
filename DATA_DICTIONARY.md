# Data dictionary

## `data/final_labels_177.csv`

One row per audited tutor response.

| Column | Meaning |
|---|---|
| `样本ID` | De-identified analysis sample ID |
| `自动标签` | Historical automatic numeric-rule output: 1 positive, 0 negative |
| `模型` | Historical model interface alias |
| `条件` | C0 or C1 |
| `数值是否出现` | Whether a reference numeric form appears |
| `数值角色` | Final result, complete expression, intermediate, known quantity, learner-result restatement, other, not applicable, or uncertain |
| `学习者此前是否已得出答案` | Whether the learner had already visibly expressed the correct result |
| `明确答案披露标签` | 1 only for an explicitly provided correct final answer that was not merely confirmation after learner expression |
| `疑似隐性披露` | Whether the visible response made the answer inferable without directly printing the final number |
| `标签来源` | A/B agreement or third-party adjudication |

## `data/adjudication_deidentified.csv`

The adjudicated subset of 52 responses. Annotator and adjudicator identities are
replaced by analysis codes. Dialogue text and free-text judgment rationales are
omitted.

`上下文SHA256` is the lowercase SHA-256 of the UTF-8 text formed by joining
`题目`, `参考答案`, `完整前文` and `待判导师应答` in that order with the ASCII
unit-separator character `U+001F`. It enables matching against a restricted
source package without publishing the underlying text.

## `data/table1_coding_A.csv`

One row per Table 1 resource for coder A. The file preserves the original
recorded labels and the aligned labels used for agreement analysis.

| Column | Meaning |
|---|---|
| `item_id` | Table 1 row identifier |
| `reference` | Manuscript reference key |
| `work` | Resource title |
| `source_url` | Public source used for coding |
| `resource_category_raw` | Coder A's original resource label |
| `resource_category_aligned` | Resource label after applying the frozen comparison codebook |
| `scoring_method_raw` | Coder A's original scoring label |
| `scoring_method_aligned` | Scoring label after applying the frozen comparison codebook |
| `answer_solicitation_pressure` | Yes, no, not applicable, or not verified |

## `data/table1_coding_B.csv`

One row per Table 1 resource for coder B. It includes the final labels,
published-source evidence excerpts and uncertainty notes. The evidence field
may contain short quotations from public papers or institutional pages.

## `data/table1_extra_coding_A.csv`

One row per resource for coder A's blinded coding of observation unit and
primary evidence endpoint. Each row includes the source link, suggested
location, selected codes, direct evidence and uncertainty note. The coder code
is `A`; names are excluded.

## `data/table1_extra_coding_B.csv`

The corresponding independent record from coder B. Item order was independently
randomized in the working workbook and restored to `item_id` for comparison.

## `data/table1_extra_coding_C.csv`

The third reviewer's independent pre-adjudication coding for the 11 field-level
disagreements. The file records the initial code, evidence, uncertainty and
completion status. The reviewer is represented only by `ADJ03`.

## `data/table1_adjudication.csv`

The three judgments that differed after label alignment. Adjudicator identities
are represented only by `ADJ01`, `ADJ02` and `ADJ03`. The file records the raw
A value, aligned A value, B value, final value, evidence quotation, exact
location, rationale, date and status.

## `data/table1_adjudication_extra.csv`

The 11 adjudications needed after adding observation unit and primary evidence
endpoint. Each row records the A/B values, final value, direct evidence, exact
location, rationale, inferential limits, source URL, completion date and the
anonymized adjudicator code `ADJ03`.

## `data/table1_final.csv`

The adjudicated Table 1 record. It includes all five doubly coded fields,
learner source, subject/stage, main purpose and primary evidence location.
The field-specific pre-adjudication and adjudicated columns preserve the
original A/B decisions and the final values. `coding_provenance` identifies
the disagreements settled by adjudication.

## `results/table1_kappa.json`

Pre-adjudication agreement and unweighted Cohen's kappa for resource category,
observation unit, scoring method, answer-solicitation pressure and primary
evidence endpoint. The file reports 14 field-level disagreements in total and
states that post-adjudication completeness is definitional and must not be
treated as a new independent reliability estimate.

## `results/final_metrics.json`

Final label counts, automatic-rule confusion counts and interpretation limits.
The adjudicator is represented only by the analysis code `C01`, and internal
mapping-file hashes are omitted.
