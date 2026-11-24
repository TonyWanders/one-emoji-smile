#!/usr/bin/env python3
"""One Emoji, One Smile - make.fun entry.

Writes exactly one emoji to /output/entry.txt: the hugging face.
A warm, open-armed welcome that reads as kind and friendly to any
stranger at first glance. It is a chosen gesture, not the first
smiley that comes to mind, and it carries no intimacy, sarcasm or
flirtation, so it works coming from someone unknown.

No network, no clock, no randomness: the output is fixed.
"""

import os
import sys

EMOJI = "\U0001F917"  # HUGGING FACE


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        # No trailing newline: the entry must be exactly one emoji.
        f.write(EMOJI)


if __name__ == "__main__":
    main()
