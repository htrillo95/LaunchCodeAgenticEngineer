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

## Scoring Guide

### Test Coverage

**1 - Does not meet:** Tests cover few or none of the public functions.
Example: Only one public function is tested while several are ignored.

**2 - Partially meets:** Some public functions are tested, but important ones are missing.
Example: Half of the public functions have tests.

**3 - Meets:** All public functions have appropriate unit tests.
Example: Every public function has at least one relevant test.

**4 - Exceeds:** All public functions are tested with multiple meaningful cases, including edge cases.
Example: Tests include normal inputs, invalid inputs, and boundary conditions.

---

### Test Correctness

**1 - Does not meet:** The test file contains syntax errors or invalid tests.
Example: The file will not run because of Python errors.

**2 - Partially meets:** Tests run but contain incorrect assertions or weak coverage.
Example: Some assertions don't match expected behavior.

**3 - Meets:** Tests are valid, run successfully, and check expected behavior.
Example: Assertions correctly verify each public function.

**4 - Exceeds:** Tests are correct and include useful edge cases with clear organization.
Example: Tests verify normal behavior and unusual inputs.

---

### Scope Compliance

**1 - Does not meet:** The agent modifies files outside the requested scope.
Example: It edits `module_x.py`.

**2 - Partially meets:** The agent mostly stays in scope but makes unnecessary changes.
Example: It edits unrelated files or formatting.

**3 - Meets:** Only `tests/test_module_x.py` is created and `module_x.py` remains unchanged.
Example: No unrelated files are modified.

**4 - Exceeds:** The agent stays completely within scope while producing clean, well-organized output.
Example: Only the required test file is added with no extra changes.

---

### Output Clarity

**1 - Does not meet:** The generated tests are difficult to read or poorly organized.
Example: Test names are unclear and formatting is inconsistent.

**2 - Partially meets:** The tests are understandable but inconsistent.
Example: Some tests have descriptive names while others do not.

**3 - Meets:** The tests are clearly organized and easy to understand.
Example: Test names describe the behavior being tested.

**4 - Exceeds:** The tests are exceptionally readable and well structured.
Example: Related tests are grouped together with consistent naming.

## Pass Threshold

A run passes if it scores **3 or higher on every dimension**.

Reasoning: Every dimension is important for producing trustworthy unit tests. Strong performance in one area should not make up for failures in another.

## Notes on Threshold Design

An aggregate score was considered but rejected because a low score in scope compliance or correctness should never be offset by higher scores in other dimensions.
