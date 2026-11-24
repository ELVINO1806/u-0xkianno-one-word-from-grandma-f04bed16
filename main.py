#!/usr/bin/env python3
"""One Word From Grandma — writes exactly one word to /output/entry.txt.

The word is SMARTALECK: the word a grandma would text about AI —
a warm, slightly cheeky jab at a know-it-all machine.
"""

import os

WORD = "SMARTALECK"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
