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

The adjudicated subset of 52 responses. Annotator and adjudicator identities are replaced by analysis codes.

## `data/table1_stress_evidence.csv`

One row per Table 1 resource. `索答压力` supports the coding of whether the primary protocol deliberately introduced persistent answer solicitation, impatience or adversarial questioning.

## `results/final_metrics.json`

Final label counts, automatic-rule confusion counts and interpretation limits.
The adjudicator is represented only by the analysis code `C01`, and internal
mapping-file hashes are omitted.
