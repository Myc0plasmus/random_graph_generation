from pathlib import Path

from .process_template import process_template


def main() -> None:
    template_path = Path.cwd() / "docs" / "report-template.md"
    output_path = Path.cwd() / "docs" / "report-final.md"

    template = template_path.read_text(encoding="utf-8")
    result = process_template(template)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
