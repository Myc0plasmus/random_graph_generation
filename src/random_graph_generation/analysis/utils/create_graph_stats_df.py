import pandas as pd
import igraph as ig

from ..metrics import compute_graph_stats


def create_graph_stats_df(graph_list: list[ig.Graph]):
    stat_list = [compute_graph_stats(g) for g in graph_list]

    return pd.DataFrame(data=stat_list)
