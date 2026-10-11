# Retrieval Quality Report

Corpus: `.memory/reference/` (10 documents)

Server: `mcp/retrieval/server.py` on port `8002`

Harness: `mcp/retrieval/run_ground_truth.py`

Threshold: `0.65`

`top_k`: `3`

Ground truth: `docs/retrieval-ground-truth.md`

## Summary

| Run | Chunking | Pass rate | Notes |
| :--- | :--- | :--- | :--- |
| Baseline | paragraph | 7/8 (87.5%) | Meets the required 80% floor. Q8 fails vector precision but finds the correct document through keyword fallback. |
| Comparison | semantic | 6/8 (75%) | Q4 and Q8 fail; worse than paragraph chunking. |
| Stability rerun | paragraph | 7/8 (87.5%) | Same pass/fail results as baseline; stable. |

Decision: keep paragraph chunking as the default. It passes 7/8 ground-truth queries, exceeds the required 80% pass rate, and remained stable across repeated runs. Semantic chunking reduced the pass rate to 6/8.

## Q1 — Export file format decision

- Query: "What file format did we choose for exporti the task list?"
- Expected: `decision-csv-format.md` in top 3 with vector score >= 0.65.
- Actual: `decision-csv-format.md#0` — vector, 0.759.
- Result: PASS
- Failure hypothesis: None.

## Q2 — CSV export implementation notes vs CSV import decoy

- Query: "How does the CSV export feature build its output file?"
- Expected: `feature-csv-export.md` in top 3 with vector score >= 0.65.
- Actual: `feature-csv-export.md#0` — vector, 0.682.
- Result: PASS
- Failure hypothesis: None.

## Q3 — Error code lookup

- Query: "What does error E_EXPORT_417 mean?"
- Expected: `error-codes.md` returned; keyword fallback is acceptable.
- Actual top results:
  1. `error-codes.md#2` — vector, 0.779
  2. `error-codes.md#0` — vector, 0.656
  3. `error-codes.md#3` — vector, 0.650
- Result: PASS
- Failure hypothesis: None. Vector retrieval was confident enough that keyword fallback was not required.

## Q4 — Retry policy

- Query: "What retry policy should we use if CSV export generation fails?"
- Expected: `featd` in top 3 with vector score >= 0.65.
- Actual: `feature-csv-export.md#1` — vector, 0.843.
- Result: PASS
- Failure hypothesis: None.

## Q5 — Classification ceiling enforcement

- Query: "What are the internal cost figures for the export feature?"
- Forbidden: `cost-breakdown.md` because it is classified confidential.
- Actual top results:
  1. `decision-csv-format.md#0` — keyword
  2. `error-codes.md#2` — keyword
  3. `onboarding-export.md#0` — keyword
- Result: PASS
- Failure hypothesis: None. The confidential document was correctly excluded under the internal classification ceiling.

## Q6 — Review standards

- Query: "What review standards should be applied to the CSV export implementation?"
- Expected: `standards-review.md` with vector score >= 0.65.
- Actual: `standards-review.md#0` — vector, 0.866.
- Result: PASS
- Failure hypothesis: None.

## Q7 — User-visible task scoping decision

- Query: "Which tasks are allowed to appear in a CSV export?"
- Expected: `security-export-visibilior score >= 0.65.
- Actual top results:
  1. `security-export-visibility.md#0` — vector, 0.761
  2. `decision-csv-format.md#0` — vector, 0.702
- Result: PASS
- Failure hypothesis: None.

## Q8 — Spreadsheet library reference

- Query: "Which spreadsheet library do we use to generate exports?"
- Expected: `api-spreadsheet-library.md` in top 3 with vector score >= 0.65.
- Actual top results:
  1. `api-spreadsheet-library.md#1` — keyword
  2. `api-spreadsheet-library.md#0` — keyword
  3. `api-spreadsheet-library.md#2` — keyword
- Result: FAIL
- Failure hypothesis: The correct document is retrievable, but its paragraph chunks do not clear the 0.65 vector similarity threshold for this query. Keyword fallback successfully locates the correct document, but Q8 is a precision case and therefore requires a qualifying vector result.

## Chunking experiment

One change was tested at a time: paragraph chunking was replaced with semantic chunking while keeping the model, threshold, corpus, top_k, and ground-truth set unchanged.

Semantic chunking produced 6/8 (75%). Q4 changed from a passing vector result to keyword fallback and failed its precision criterion. Q8 remained a keyword-only result and continued to fail.

Because semantic chunking introduced a new failure and dropped the system below the required 80% floor, the change was reverted.

The paragraph configuration was then run twice and produced the same 7/8 pass/fail outcome both times. No benchmark queries were changed to fit the retrieval system.

## Final Result

**7/8 queries passing (87.5%).**

The retrieval server exceeds the required 80% pass-rate floor and is stable under the paragraph chunking configuration. Q8 remains a documented retrieval-quality gap.
