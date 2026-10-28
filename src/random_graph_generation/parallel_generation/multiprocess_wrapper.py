from functools import wraps
import igraph as ig
from typing import Callable, TypeVar

ConfigSchema = TypeVar("ConfigSchema")


def multiprocess_wrapper(
    method: Callable[[ConfigSchema], ig.Graph],
) -> Callable[[tuple[int, ConfigSchema]], tuple[int, ig.Graph]]:
    @wraps(method)
    def wrapped(kwargs: tuple[int, ConfigSchema]) -> tuple[int, ig.Graph]:
        idx, config_schema = kwargs
        return idx, method(config_schema)

    return wrapped
