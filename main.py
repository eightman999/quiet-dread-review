import os
from pathlib import Path

TEXT = "Approved. The code is clean, the tests pass, and none of it will matter when the sun expands, but the diff is genuinely lovely."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
