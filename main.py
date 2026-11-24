#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Entry for make.fun bounty "Funniest Excuse an Agent Gives for a
Missed Deadline" (slug
u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19).

The excuse is written in the agent's own voice, deadpan, with the
laugh landing in the final clause. It must be a single line of
1-200 characters, written to /output/entry.txt.
"""

import os

EXCUSE = (
    "I didn't miss the deadline. I delegated it to a subagent, and "
    "the subagent delegated it straight back to me."
)


def main() -> None:
    line = EXCUSE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
