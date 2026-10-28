from dataclasses import dataclass


@dataclass
class ErdosRenyiSchema:
    n: int
    p: float
