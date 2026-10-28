from dataclasses import dataclass


@dataclass
class ErdosRenyiSchema:
    """Configuration for generating an Erdős–Rényi random graph.

    :param n: Number of vertices in the graph.
    :param p: Probability of an edge between each pair of vertices,
        in the interval from 0 to 1.
    """

    n: int
    p: float
