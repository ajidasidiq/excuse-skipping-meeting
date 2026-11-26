"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes a single razor-sharp excuse line (at most 200 characters) to
/output/entry.txt, the path the make.fun program/v1 harness grades.

The line is original, written for this bounty: a laptop that would
rather sit through a two-hour update than a pointless meeting, and an
owner who cannot argue with its judgement.
"""

import os

ENTRY = (
    "Sorry, I can't join \u2014 my laptop read the invite, started a "
    "two-hour update, and honestly, I respect its judgment."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters -> {OUTPUT_PATH})")


if __name__ == "__main__":
    main()
