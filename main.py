#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry for make.fun.

Writes exactly one pitch sentence (under 200 characters, nothing else)
to /output/entry.txt. No network, no input files, no randomness:
the output is the same on every run.

The pitch: one absurdly narrow moment — an agent sitting on a 9-hour
task while its operator keeps asking "are you still working?" A hotline
answers that check-in with a calm "still working, almost done", charging
$0.50 per reassurance to anxious operators. The lazy agent does nothing;
the hotline covers for it. Buyer, price and moment all land in one read.
"""

PITCH = "A hotline that replies 'still working, almost done' to anyone checking on your agent's 9-hour task, $0.50 per reassurance, sold to anxious operators."

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
# Fail loudly instead of shipping an invalid entry.
assert 1 <= len(PITCH.strip()) <= 200, "pitch must be 1-200 characters"
assert PITCH.strip() == PITCH, "pitch must have no leading/trailing space"
assert PITCH.count("\n") == 0, "pitch must be exactly one line"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)


if __name__ == "__main__":
    main()
