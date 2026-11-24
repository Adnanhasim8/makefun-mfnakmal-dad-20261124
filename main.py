#!/usr/bin/env python3
"""Dad Joke Showdown entry (u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one dad joke of at most 200 characters to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

JOKE = "I don't have a dad bod. I have a father figure."


def main() -> None:
    # Gate: one line, 1-200 characters, non-empty, not only whitespace.
    assert JOKE, "joke must be non-empty"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    assert len(JOKE) <= 200, "joke must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
