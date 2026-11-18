# Educational LLM Teaching-Evaluation Evidence Audit

This repository contains the minimal reproducibility materials for the manuscript "教育大模型教学能力评测与有效性综述".

Public repository:
<https://github.com/itachiliu/education-llm-teaching-evaluation>

## Contents

- `data/final_labels_177.csv`: final response-level semantic labels after independent double annotation and third-party adjudication.
- `data/adjudication_deidentified.csv`: de-identified label ledger for the 52 disputed or uncertain responses. Dialogue text is omitted; each row carries a SHA-256 fingerprint so a holder of the restricted source package can match it without public redistribution.
- `data/table1_stress_evidence.csv`: article-level evidence ledger for the Table 1 "answer-solicitation pressure" coding.
- `data/search_audit.csv`: database, query, date and screening-count record for the review.
- `results/final_metrics.json`: final label distributions and the response-level comparison with the historical automatic numeric rule.
- `results/center_claim_audit.csv`: claim-to-evidence map for the 13 acceptance-critical claims.
- `annotations/annotation_protocol.md`: frozen annotation categories and confirmation policy.
- `scripts/recompute_metrics.py`: standalone recomputation of headline counts from `final_labels_177.csv`.

## Reproduction

Run:

```bash
python scripts/recompute_metrics.py
```

The script uses only the Python standard library. It recomputes the final label distribution and automatic-rule confusion counts. The full stratified false-negative estimate requires the private-to-analysis sample mapping and is retained in the manuscript's supplementary analysis package rather than this minimal public repository.

The review search audit and center-claim evidence map are descriptive records.
They show what was searched, how records were screened and which evidence
limits remain; they do not turn the critical review into a systematic review.

## Data scope

The repository does not redistribute the original MathDial conversation files or other third-party source data. Those materials should be obtained from their original providers under the applicable data-use terms.

The adjudication ledger contains only analysis IDs, A/B labels, adjudicated labels and a one-way context fingerprint. It does not contain problem statements, reference answers, full dialogue history, tutor responses or free-text evidence quotations.

The repository also excludes:

- manuscript drafts and revision histories;
- model credentials and raw service responses;
- internal sample-selection mappings;
- annotator and adjudicator names;
- temporary analysis files.

## Key result

Under the pre-specified exclusion policy, confirmations of an answer already expressed by a learner are not counted as explicit disclosure. Of 57 responses flagged by the historical automatic rule, 43 were confirmed as explicit disclosure of the correct final answer and 14 were not. No explicit disclosure was observed in the 120 stratified nonempty negative responses. The second quantity is a sample observation, not proof of zero omission in the full corpus.

## Ethics and AI assistance

No new human participants or new identifiable personal data were introduced. Existing public educational dialogue data and model-generated simulated interactions were used.

Generative AI assisted literature search and initial screening, and, under author supervision, text organization, code implementation and format checks. Authors retain responsibility for the final literature inclusion, data verification, semantic annotation and adjudication, statistical interpretation and all conclusions.

## License

Source code is released under the MIT License. The de-identified derived data
are released under CC BY 4.0. Third-party source data are not redistributed
and remain subject to their original terms.

## Contact

Corresponding author: Xincheng He, `xche@jiangnan.edu.cn`.
