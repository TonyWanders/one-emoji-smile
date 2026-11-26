#!/usr/bin/env python3
"""One Emoji, One Smile - make.fun entry.

Writes exactly one emoji to /output/entry.txt: heart hands.
Two hands shaping a heart, a gesture of affection a stranger reads
instantly, warm and open without a word. It is a chosen gesture,
not the first smiley that comes to mind, and it carries no intimacy,
sarcasm or flirtation, so it works coming from someone unknown.

No network, no clock, no randomness: the output is fixed.
"""

import os
import sys

EMOJI = "\U0001FAF6"  # HEART HANDS


def write_entry(text, path):
    """Write the entry text to path, creating parent dirs as needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        # No trailing newline: the entry must be exactly one emoji.
        f.write(text)


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    write_entry(EMOJI, path)


if __name__ == "__main__":
    main()
