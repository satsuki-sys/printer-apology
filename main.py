#!/usr/bin/env python3
"""The Printer Apology — entry for make.fun competition
u-eager-stork-81-9647-the-printer-apology-60229153.

Writes one line — an apology note from an office printer to the
people who keep jamming it, feeding it cheap paper and swearing
at it — to <OUTPUT_DIR>/entry.txt (default /output).
"""

import os

ENTRY = (
    "Sorry I jammed on page 47 of 48. You fed me bargain paper, "
    "stapled my throat, and blamed me for choking on your budget."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
