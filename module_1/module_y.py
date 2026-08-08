"""
Formatting and reporting utilities for the parallel agent-session example.

This module is intentionally correct but lightly documented. It is designed for
the "Session B" agent task: improve docstrings in this file and update README.md,
without modifying any test files.
"""

from __future__ import annotations


def format_currency(amount: float) -> str:
    """Return `amount` formatted as a dollar string, e.g. `$1,234.56` or `-$1,234.56`."""
    if amount < 0:
        return f"-${abs(amount):,.2f}"
    return f"${amount:,.2f}"


def build_report_title(project_name: str, version: str) -> str:
    """Return a "Project — Version" title, filling in defaults for blank inputs.

    Blank/whitespace-only `project_name` becomes "Untitled Project"; blank
    `version` becomes "draft". Extra internal whitespace in `project_name` is
    collapsed to single spaces.
    """
    clean_project = " ".join(project_name.strip().split())
    clean_version = version.strip()

    if not clean_project:
        clean_project = "Untitled Project"
    if not clean_version:
        clean_version = "draft"

    return f"{clean_project} — {clean_version}"


def mask_email(email: str) -> str:
    """Return `email` with the local part partially masked, e.g. `j*e@example.com`.

    The domain is lowercased and left unmasked. A single-character local part
    becomes `*`; a two-character local part keeps its first character and masks
    the second. Longer local parts keep the first and last characters and mask
    everything between.

    Raises:
        ValueError: If `email` has no `@`, or the local part or domain is empty.
    """
    email = email.strip()
    if "@" not in email:
        raise ValueError("email must contain @")

    local_part, domain = email.split("@", 1)
    if not local_part or not domain:
        raise ValueError("email must include a local part and domain")

    if len(local_part) == 1:
        masked_local = "*"
    elif len(local_part) == 2:
        masked_local = local_part[0] + "*"
    else:
        masked_local = local_part[0] + "*" * (len(local_part) - 2) + local_part[-1]

    return f"{masked_local}@{domain.lower()}"


def generate_summary_line(name: str, status: str, score: int) -> str:
    """Return a "Name: status (score)" line.

    `name` is whitespace-normalized and title-cased (falling back to "Unknown"
    if blank). `status` is lowercased with underscores replaced by spaces.
    """
    display_name = " ".join(name.strip().split()).title()
    display_status = status.strip().lower().replace("_", " ")

    if not display_name:
        display_name = "Unknown"

    return f"{display_name}: {display_status} ({score})"


def create_markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    """Return a Markdown table string with a header row built from `columns`.

    Each entry in `rows` supplies one table row; missing keys render as empty
    cells. Values are converted with `str()`.

    Raises:
        ValueError: If `columns` is empty.
    """
    if not columns:
        raise ValueError("columns cannot be empty")

    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"

    body_lines = []
    for row in rows:
        values = [str(row.get(column, "")) for column in columns]
        body_lines.append("| " + " | ".join(values) + " |")

    return "\n".join([header, separator, *body_lines])


def truncate_text(text: str, max_length: int = 80) -> str:
    """Return `text` whitespace-normalized and truncated to `max_length` characters.

    Text longer than `max_length` is cut short and suffixed with "..." so the
    result never exceeds `max_length` characters overall.

    Raises:
        ValueError: If `max_length` is less than 4.
    """
    if max_length < 4:
        raise ValueError("max_length must be at least 4")

    clean_text = " ".join(text.strip().split())
    if len(clean_text) <= max_length:
        return clean_text

    return clean_text[: max_length - 3].rstrip() + "..."
