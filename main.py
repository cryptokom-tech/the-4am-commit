"""The 4AM Commit entry: writes one commit message to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 200 characters that is not only
white space. The entry below is a single 124-character line, and the
guard in main() refuses to write anything that would fail that gate.
"""

import os
import sys

MAX_CHARS = 200

ENTRY = (
    "fix: my self-repair loop improved the bug instead of removing it. "
    "the error message is now polite, specific, and still fatal"
)


def main() -> int:
    if not ENTRY.strip():
        return 1
    if len(ENTRY) > MAX_CHARS:
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
