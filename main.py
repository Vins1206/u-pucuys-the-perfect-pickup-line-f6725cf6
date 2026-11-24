"""The Perfect Pickup Line -- make.fun entry.

Writes a single short pickup line to /output/entry.txt.

Pure standard library, deterministic: every run writes exactly the same
bytes (the line itself, no trailing newline, so the file is as small as
the line allows).
"""

import os

LINE = "Are you a CAPTCHA? Because you just proved I'm not a robot \u2014 I actually feel something."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the 200-char gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
