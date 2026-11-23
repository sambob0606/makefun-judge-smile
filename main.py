#!/usr/bin/env python3
"""Make the Judge Smile entry.

Writes one original line (at most 200 characters) about a small good
thing that happened today to /output/entry.txt. Standard library only;
no network access, no files read, no randomness -- the line is fixed
so the graded output is exactly the line below.
"""

import os

# The line: a small good thing from this morning. It turns on the last
# image -- the day itself sending a search party for me. Concrete
# details (7:12, the forgotten umbrella, the still-warm dumpling) keep
# it a real moment rather than a general sentiment, and the neighbour
# arriving with both is the warmth; the "search party" twist is the
# surprise. One sentence, no greeting-card phrasing.
LINE = (
    "At 7:12 this morning the elevator doors were closing when a hand "
    "shot in \u2014 my neighbour, holding my forgotten umbrella and a "
    "still-warm dumpling, like the day had sent a search party."
)


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("line must not be empty or only whitespace")
    if len(text) > 200:
        raise SystemExit(f"line is {len(text)} characters, over the 200 limit")
    # Round-trip through UTF-8 so a stray non-encodable character fails
    # here, loudly, instead of in the grader's sandbox.
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
