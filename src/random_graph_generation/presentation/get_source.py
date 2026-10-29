import importlib
from pathlib import Path


def get_source(module_path: str) -> str:
    """Return the source file contents for an importable Python module."""
    module = importlib.import_module(module_path)

    if not hasattr(module, "__file__") or module.__file__ is None:
        raise ValueError(f"Module {module_path!r} has no source file.")

    source_path = Path(module.__file__)

    if source_path.suffix != ".py":
        raise ValueError(
            f"Module {module_path!r} does not point to a Python source file: "
            f"{source_path}"
        )

    return source_path.read_text(encoding="utf-8")
