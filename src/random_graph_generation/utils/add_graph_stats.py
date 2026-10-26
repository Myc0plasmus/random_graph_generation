from collections import Counter

import igraph as ig
import numpy as np
import pandas as pd


def add_graph_stats(
    df: pd.DataFrame,
    g: ig.Graph,
) -> pd.DataFrame:
    """Append one row of graph statistics to a DataFrame and return it."""

    n = g.vcount()
    m = g.ecount()
    degrees = g.degree()

    components = g.connected_components(
        mode="weak" if g.is_directed() else "strong"
    )
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
        "component_size_distribution": dict(
            sorted(Counter(component_sizes).items())
        ),

        # Degree centrality summaries
        "mean_degree_centrality": (
            float(np.mean(degrees)) / (n - 1) if n > 1 else 0.0
        ),

        # Clustering
        "global_transitivity": (
            g.transitivity_undirected()
            if not g.is_directed() and n > 0
            else np.nan
        ),
    }

    if n > 0:
        betweenness = g.betweenness()
        pagerank = g.pagerank()

        stats.update({
            "max_betweenness": max(betweenness, default=0.0),
            "mean_betweenness": float(np.mean(betweenness)),
            "max_pagerank": max(pagerank, default=0.0),
            "mean_pagerank": float(np.mean(pagerank)),
        })
    else:
        stats.update({
            "max_betweenness": np.nan,
            "mean_betweenness": np.nan,
            "max_pagerank": np.nan,
            "mean_pagerank": np.nan,
        })

    new_row = pd.DataFrame([stats])
    return pd.concat([df, new_row], ignore_index=True)

