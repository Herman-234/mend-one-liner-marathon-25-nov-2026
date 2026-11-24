#!/usr/bin/env python3
"""One-Liner Marathon — make.fun entry.

Writes one joke (<=280 chars) to the output path.
Deterministic, no network.
"""

import os
import sys

ENTRY_LINE = (
    "My grandma changed her Wi-Fi password to her wedding anniversary, "
    "so now every time the Wi-Fi drops, Grandpa has to remember the "
    "happiest day of his life just to reconnect."
)


def validate(line: str) -> None:
    """Fail loudly if the entry would break the 1-280 char, one-line gate."""
    if not line or not line.strip():
        raise ValueError("entry line is empty or only whitespace")
    if len(line) > 280:
        raise ValueError(f"entry line is {len(line)} chars, over the 280-char limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def main() -> int:
    validate(ENTRY_LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_LINE)
    print(f"wrote {len(ENTRY_LINE)} chars to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
