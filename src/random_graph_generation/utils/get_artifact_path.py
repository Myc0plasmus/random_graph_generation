from pathlib import Path

from .generate_artifacts import generate_artifacts


def get_figure_path(filename: str):
    generate_artifacts()
    return Path.cwd() / "artifacts" / "figures" / filename


def get_graphs_path(filename: str):
    generate_artifacts()
    return Path.cwd() / "artifacts" / "graphs" / filename


def get_tables_path(filename: str):
    generate_artifacts()
    return Path.cwd() / "artifacts" / "tables" / filename
