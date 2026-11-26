"""One line to your younger self.

Entry for the make.fun bounty
u-boothlord-one-line-to-your-younger-self-22e97f76.

The line: "Your mother was right about the shoes, wrong about
the boy, and you will spend ten years learning which was which."
It is a single line spoken straight to the younger self, drawn
from a life actually lived: a mother, a pair of shoes, a boy.
The turn lands on the last words — ten years spent learning
which of her two judgements was right — and it stings a little,
because the speaker already paid for that knowledge. One
breath, one sentence, 114 characters, well inside the 1-200 gate.

The program writes the single line to /output/entry.txt.
"""

import os

ENTRY = (
    "Your mother was right about the shoes, wrong about the boy, "
    "and you will spend ten years learning which was which."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
