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

## `data/table1_stress_evidence.csv`

One row per Table 1 resource. `索答压力` supports the coding of whether the primary protocol deliberately introduced persistent answer solicitation, impatience or adversarial questioning.

## `results/final_metrics.json`

Final label counts, automatic-rule confusion counts and interpretation limits.
The adjudicator is represented only by the analysis code `C01`, and internal
mapping-file hashes are omitted.
