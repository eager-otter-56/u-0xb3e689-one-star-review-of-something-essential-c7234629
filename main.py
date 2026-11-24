#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes a single deadpan one-star review of sleep to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""
import os

ENTRY_TEXT = (
    "One star. Sleep takes eight hours nightly, non-negotiable, "
    "cannot be banked, and the night you beg hardest, "
    "it arrives at 4 a.m. and leaves before the alarm."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
