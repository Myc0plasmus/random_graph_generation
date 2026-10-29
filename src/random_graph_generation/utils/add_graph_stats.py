from collections import Counter
from rich.console import Console

import igraph as ig
import numpy as np
import pandas as pd
import pickle as pkl

from random_graph_generation.utils import get_graphs_path, get_tables_path


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


def add_graph_stats(df: pd.DataFrame, g: ig.Graph):
    stats = compute_graph_stats(g)

    new_row = pd.DataFrame([stats])
    new_df = pd.concat([df, new_row], ignore_index=True)

    # TODO: compute columns stats

    return new_df


def create_graph_stats_df(graph_list: list[ig.Graph]):
    stat_list = [compute_graph_stats(g) for g in graph_list]

    return pd.DataFrame(data=stat_list)


def process_graph_list(method_name: str):
    console = Console()
    with console.status(f"[bold green]Loading {method_name} graphs..."):
        graphs_filename = f"{method_name}_graphs.pkl"
        graphs_path = get_graphs_path(graphs_filename)
        with open(graphs_path, "rb") as f:
            graph_list = pkl.load(f)
        df = create_graph_stats_df(graph_list)
        table_filename = f"{method_name}_table.csv"
        table_path = get_tables_path(table_filename)
        df.to_csv(table_path)
    console.print(f"Loading {method_name} graphs: [green]completed")
