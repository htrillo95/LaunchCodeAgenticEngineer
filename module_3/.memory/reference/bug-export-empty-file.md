---
classification: internal
project: proj-csv
doc_type: bug
---

# Bug Report: Empty CSV Export

Users previously reported that exporting an empty task list could produce an unexpected download result.

The issue concerns handling an export when no task rows are available. It does not change the project's CSV format decision, task-visibility rules, or import behavior.

Export implementations should handle an empty dataset without exposing tasks outside the current user's permitted scope.
