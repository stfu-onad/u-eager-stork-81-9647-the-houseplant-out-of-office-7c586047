#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one original out-of-office auto-reply a houseplant would send
to /output/entry.txt.
"""

TEXT = (
    "Out of office \u2014 I\u2019m a fern, ignored since March. "
    "Water me or don\u2019t; the dust on my leaves has seniority now."
)


import os

LIMIT = 120


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= LIMIT, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
