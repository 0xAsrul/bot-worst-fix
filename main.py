#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — entry program.

Writes a single commit-message line to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "fix: login bug by logging everyone in as admin"
MAX_CHARS = 100
OUT_PATH = "/output/entry.txt"


def main() -> None:
    line = ENTRY
    # Small self-checks: one line, not empty, within the 100-char limit.
    assert line, "entry must not be empty"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Read the output back and verify it is exactly the intended line.
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit(
            f"verification failed: {OUT_PATH} content does not match the intended entry"
        )
    print(f"wrote {len(line)} chars to {OUT_PATH}: {line!r}")


if __name__ == "__main__":
    main()
