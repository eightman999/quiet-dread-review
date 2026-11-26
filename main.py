import os
from pathlib import Path

TEXT = "LGTM. We merge, we deploy, we are forgotten by Friday's hotfix, and somehow that is the most comforting part."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
