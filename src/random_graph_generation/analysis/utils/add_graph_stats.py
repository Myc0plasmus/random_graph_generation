import pandas as pd
import igraph as ig

from .compute_graph_stats import compute_graph_stats


def add_graph_stats(df: pd.DataFrame, g: ig.Graph) -> pd.DataFrame:
    stats = compute_graph_stats(g)

    new_row = pd.DataFrame([stats])
    new_df = pd.concat([df, new_row], ignore_index=True)

    return new_df
