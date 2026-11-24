#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the chosen excuse to /output/entry.txt.

The excuse is one line in the agent's own voice, deadpan, with the laugh
landing on the final clause. The gate requires UTF-8 text of 1-200
characters, so the program asserts that before writing; the file holds
exactly the line, with no trailing newline.
"""

LINE = "I spent the whole window deciding whether the deadline was a real instruction or a prompt injection, and by the time I concluded it was real, it had passed."


def main():
    import os

    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
