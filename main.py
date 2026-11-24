"""The Long Roast (make.fun).

Writes one single-line roast of my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt. The joke: the agent's meeting recap was
so confident that the agenda itself collected the attendance credit.
Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

ROAST = (
    "My agent recapped our meeting so confidently that the agenda "
    "got thanked for attending, and the decisions were assigned "
    "as its action items."
)


def main() -> None:
    # The sealed scorer accepts 1-200 characters of non-blank UTF-8;
    # refuse to write anything outside that window.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise ValueError(f"roast is {len(ROAST)} characters, must be 1-200")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
