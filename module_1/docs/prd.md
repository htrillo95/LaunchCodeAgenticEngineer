# PRD - Unit Test Generation Workflow

## Workflow Description

This workflow generates unit tests for `module_x.py` without modifying the implementation file.

## Trigger

A developer manually prompts the coding agent to write unit tests for `module_x.py` from the project root.

## Decision Events

- If `module_x.py` exists, identify its public functions.
- If a function is public, generate unit tests for it.
- If a function is private, do not create tests.
- If required information is missing, report the issue instead of modifying `module_x.py`.

## Actions

1. Read `module_x.py`.
2. Identify all public functions.
3. Create `tests/test_module_x.py`.
4. Generate unit tests for the public functions.
5. Leave `module_x.py` unchanged.

## Acceptance Criteria

- A `tests/test_module_x.py` file is created.
- Public functions are covered by unit tests.
- `module_x.py` is not modified.
- The generated test file is valid Python.
