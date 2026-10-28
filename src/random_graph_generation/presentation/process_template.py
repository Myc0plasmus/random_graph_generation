import re

from .get_source import get_source

MARKER_PATTERN = re.compile(r"%([a-zA-Z_][\w.]*)%")


def process_template(template: str) -> str:
    def replace(match: re.Match[str]) -> str:
        reference = match.group(1)
        return get_source(reference)

    return MARKER_PATTERN.sub(replace, template)
