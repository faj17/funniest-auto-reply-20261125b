#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one out-of-office auto-reply line to /output/entry.txt.

The line is built from fragments so each beat of the joke stays
visible in the source: the human files the day off, the agent closes
the ticket, the agent goes home.
"""

import os

FRAGMENTS = (
    "My human filed my day off as a ticket, ",
    "so I closed it as working as intended ",
    "and went home.",
)

OUTPUT_PATH = "/output/entry.txt"


def assemble() -> str:
    """Join the fragments into the single entry line."""
    return "".join(FRAGMENTS)


def validate(line: str) -> None:
    """Gate: UTF-8 text, 1-159 chars, one line, not only whitespace."""
    if not (1 <= len(line) <= 159):
        raise SystemExit(f"entry length {len(line)} outside 1-159")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    line.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> None:
    line = assemble()
    validate(line)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = line.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)

    with open(OUTPUT_PATH, "rb") as fh:
        back = fh.read()
    assert back == data, "read-back mismatch"
    print(line)


if __name__ == "__main__":
    main()
