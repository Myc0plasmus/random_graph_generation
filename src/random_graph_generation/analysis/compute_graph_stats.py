import igraph as ig
import numpy as np


from collections import Counter


def compute_graph_stats(
    g: ig.Graph,
) -> dict:
    """Append one row of graph statistics to a DataFrame and return it."""

    n = g.vcount()
    m = g.ecount()
    degrees = g.degree()

    components = g.connected_components(mode="weak" if g.is_directed() else "strong")
    component_sizes = components.sizes()

    stats = {
        # Basic statistics
        "directed": g.is_directed(),
        "n_vertices": n,
        "n_edges": m,
        "density": g.density(),
        "mean_degree": float(np.mean(degrees)) if n else 0.0,
        "min_degree": min(degrees, default=0),
        "max_degree": max(degrees, default=0),
        "is_connected": len(components) == 1 if n else False,
        # Component statistics
        "n_components": len(components),
        "largest_component_size": max(component_sizes, default=0),
        "component_size_distribution": dict(sorted(Counter(component_sizes).items())),
        # Degree centrality summaries
        "mean_degree_centrality": (float(np.mean(degrees)) / (n - 1) if n > 1 else 0.0),
        # Clustering
        "global_transitivity": (
            g.transitivity_undirected() if not g.is_directed() and n > 0 else np.nan
        ),
    }

    return stats
