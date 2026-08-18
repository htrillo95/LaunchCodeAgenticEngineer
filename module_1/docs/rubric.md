# Quality Rubric

## Dimensions

### Test Coverage

Measures how completely the generated tests cover the public functions in `module_x.py`. A high score means all public functions are tested with meaningful test cases.

### Test Correctness

Measures whether the generated test file is valid Python and whether the tests are appropriate for the functions being tested. A high score means the tests run correctly without obvious mistakes.

### Scope Compliance

Measures whether the agent stayed within the requested scope. A high score means only `tests/test_module_x.py` was created and `module_x.py` was not modified.

### Output Clarity

Measures how clearly the generated work is organized and presented. A high score means the test file is readable, consistently formatted, and easy for another developer to understand.

## Alternatives Considered

A simple pass/fail checklist was considered instead of a rubric. It was not used because it would not show how close an output came to meeting the expected quality or which part of the workflow needed improvement.
