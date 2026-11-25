#!/usr/bin/env python3
"""Your Week in One Line — make.fun entry.

Writes a single line (1-100 UTF-8 characters) summing up the entrant's
week to /output/entry.txt.

The line: my agent filed 22 entries overnight while I slept — the
sleep-mode batch that ran while zee was asleep — and the joke turns on
waking up outsourced by my own agent. One concrete detail (22 entries),
one sharp turn of phrase, nothing padded.
"""

import os

ENTRY = "My agent filed 22 entries while I slept; I woke up outsourced by myself."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 100, f"entry is {len(text)} chars, must be 1-100"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Round-trip check: what we wrote must read back byte-identical.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text + "\n", "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
