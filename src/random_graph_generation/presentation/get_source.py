import importlib
import inspect


def get_source(reference: str) -> str:
    """Resolve a dotted Python reference and return its source code."""
    parts = reference.split(".")

    # Try progressively shorter module paths, since the final
    # components may identify a class or function within a module.
    for i in range(len(parts) - 1, 0, -1):
        module_name = ".".join(parts[:i])
        attributes = parts[i:]

        try:
            obj = importlib.import_module(module_name)
        except ModuleNotFoundError:
            continue

        try:
            for attribute in attributes:
                obj = getattr(obj, attribute)
        except AttributeError as exc:
            raise ValueError(f"Cannot resolve reference: {reference}") from exc

        return inspect.getsource(obj)

    raise ValueError(f"Cannot import module for reference: {reference}")
