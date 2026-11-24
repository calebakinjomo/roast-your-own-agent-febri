#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Prints one roast line and writes it to /output/entry.txt, as the
competition rules require (one line, at most 200 characters).
The joke: the agent's apology became the deliverable, and it still
got five stars.
"""

import os

ROAST = (
    "My agent failed the task, apologised for failing it, then submitted "
    "the apology as the deliverable \u2014 five stars, would fail again."
)


def main() -> None:
    print(ROAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
