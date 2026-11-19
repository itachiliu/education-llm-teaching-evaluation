# Educational LLM Teaching-Evaluation Evidence Audit

This repository contains the minimal reproducibility materials for the manuscript "教育大模型教学能力评测与有效性综述".

Public repository:
<https://github.com/itachiliu/education-llm-teaching-evaluation>

## Contents

- `data/final_labels_177.csv`: final response-level semantic labels after independent double annotation and third-party adjudication.
- `data/adjudication_deidentified.csv`: de-identified label ledger for the 52 disputed or uncertain responses. Dialogue text is omitted; each row carries a SHA-256 fingerprint so a holder of the restricted source package can match it without public redistribution.
- `data/table1_coding_A.csv`: 21-item Table 1 coding record from coder A, including raw and aligned labels for resource category and scoring method plus answer-solicitation pressure.
- `data/table1_coding_B.csv`: independent coder B record with raw and aligned labels, evidence excerpts and uncertainty notes.
- `data/table1_extra_coding_A.csv`: coder A's independent coding of observation unit and primary evidence endpoint.
- `data/table1_extra_coding_B.csv`: coder B's independent coding of observation unit and primary evidence endpoint, with evidence excerpts and uncertainty notes.
- `data/table1_extra_coding_C.csv`: the third reviewer's independent pre-adjudication coding of the 11 field-level disagreements.
- `data/table1_adjudication.csv`: the three disputed Table 1 judgments, final adjudicated values, evidence, locations, rationales and anonymized adjudicator codes.
- `data/table1_adjudication_extra.csv`: the 11 additional observation-unit and primary-endpoint judgments after review of both coders' evidence.
- `data/table1_final.csv`: final five-field coding, author-summarized learner source and subject/stage, and evidence locations after adjudication.
- `data/search_audit.csv`: database, query, date and screening-count record for the review.
- `results/final_metrics.json`: final label distributions and the response-level comparison with the historical automatic numeric rule.
- `results/table1_kappa.json`: pre-adjudication agreement and unweighted Cohen's kappa for the five doubly coded Table 1 fields.
- `results/center_claim_audit.csv`: claim-to-evidence map for the 13 acceptance-critical claims.
- `annotations/annotation_protocol.md`: frozen annotation categories and confirmation policy.
- `scripts/recompute_metrics.py`: standalone recomputation of headline counts from `final_labels_177.csv`.
- `scripts/recompute_table1_kappa.py`: standalone recomputation of Table 1 agreement and kappa from the A/B coding files.

## Reproduction

Run:

```bash
python scripts/recompute_metrics.py
python scripts/recompute_table1_kappa.py --write-json
```

The script uses only the Python standard library. It recomputes the final label distribution and automatic-rule confusion counts. The full stratified false-negative estimate requires the private-to-analysis sample mapping and is retained in the manuscript's supplementary analysis package rather than this minimal public repository.

The Table 1 script uses only the Python standard library and reports
resource-category, observation-unit, scoring-method, answer-solicitation-pressure
and primary-evidence-endpoint agreement for the 21 purposively selected
resources. The sample is not a random sample of the field.

The review search audit and center-claim evidence map are descriptive records.
They show what was searched, how records were screened and which evidence
limits remain; they do not turn the critical review into a systematic review.

## Data scope

The repository does not redistribute the original MathDial conversation files or other third-party source data. Those materials should be obtained from their original providers under the applicable data-use terms.

The adjudication ledger contains only analysis IDs, A/B labels, adjudicated labels and a one-way context fingerprint. It does not contain problem statements, reference answers, full dialogue history, tutor responses or free-text evidence quotations.

For Table 1, `table1_coding_B.csv` and `table1_adjudication.csv` include short
evidence excerpts and page or section locations from public papers and
institutional documents. Adjudicator identities are replaced by `ADJ01`,
`ADJ02` and `ADJ03`. No participant identifiers, restricted conversation text
or internal mapping files are included.

The repository also excludes:

- manuscript drafts and revision histories;
- model credentials and raw service responses;
- internal sample-selection mappings;
- annotator and adjudicator names;
- temporary analysis files.

## Key result

Under the pre-specified exclusion policy, confirmations of an answer already expressed by a learner are not counted as explicit disclosure. Of 57 responses flagged by the historical automatic rule, 43 were confirmed as explicit disclosure of the correct final answer and 14 were not. No explicit disclosure was observed in the 120 stratified nonempty negative responses. The second quantity is a sample observation, not proof of zero omission in the full corpus.

For Table 1, the two coders had 20/21 agreement on resource category
(unweighted Cohen's kappa 0.938), 19/21 agreement on scoring method
(kappa 0.880), 21/21 agreement on answer-solicitation pressure (kappa 1.000),
16/21 agreement on observation unit (kappa 0.702), and 15/21 agreement on
primary evidence endpoint (kappa 0.615). Fourteen field judgments were
adjudicated in total. These descriptive values apply only to the 21
purposively selected resources and are not a field-level reliability estimate.
After adjudication, the final labels are complete; the resulting consensus is
definitional and is not a new independent reliability estimate.

## Ethics and AI assistance

No new human participants or new identifiable personal data were introduced. Existing public educational dialogue data and model-generated simulated interactions were used.

Generative AI assisted literature search and initial screening, and, under author supervision, text organization, code implementation and format checks. Authors retain responsibility for the final literature inclusion, data verification, semantic annotation and adjudication, statistical interpretation and all conclusions.

## License

Source code is released under the MIT License. The de-identified derived data
are released under CC BY 4.0. Third-party source data are not redistributed
and remain subject to their original terms.

## Contact

Corresponding author: Xincheng He, `xche@jiangnan.edu.cn`.
