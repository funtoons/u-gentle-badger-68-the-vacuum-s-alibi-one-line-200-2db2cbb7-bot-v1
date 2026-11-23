#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters (program/v1).

Writes a single one-line excuse, in the robot vacuum's own deadpan voice,
to /output/entry.txt.

Deterministic and offline: the line is a fixed string, no randomness, no
network, no timestamps, no environment input. Two runs produce
byte-identical output.
"""

import os

LINE = "That spot hasn't moved in three weeks, so my map reclassified it as furniture. I don't clean furniture."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace, in a single line. Refuse to
    # write an invalid entry rather than emitting one silently.
    if (
        not 1 <= len(LINE) <= 200
        or not LINE.strip()
        or "\n" in LINE
        or "\r" in LINE
    ):
        raise ValueError("entry fails the gate (must be one line, 1-200 characters)")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
