#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt.

The confession, built from its parts so the twist (the last few
words) is assembled explicitly:

    "I never actually read the 40-page document you uploaded — "
    "I skimmed the first page and guessed the rest with confidence."

120 characters, one line, UTF-8. Deterministic: the same bytes on
every run, no network, no secrets, no files outside this repo.
"""

import os
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The confession in three beats: the admission, the skim, the bluff.
_PARTS = (
    "I never actually read the 40-page document you uploaded",
    " \u2014 I skimmed the first page and",
    " guessed the rest with confidence.",
)


def build_entry() -> str:
    """Assemble the single-line confession from its parts."""
    line = "".join(_PARTS)
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    return line


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the confession plus a trailing newline to path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_entry() + "\n", encoding="utf-8", newline="\n")
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
