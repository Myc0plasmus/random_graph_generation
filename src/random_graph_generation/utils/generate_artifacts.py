from pathlib import Path


def generate_artifacts():
    """Create the project's output directories if they don't exist."""
    project_root = Path.cwd()

    dirs = [
        "artifacts",
        "artifacts/graphs",
        "artifacts/tables",
        "artifacts/figures",
    ]

    for directory in dirs:
        (project_root / directory).mkdir(parents=True, exist_ok=True)
