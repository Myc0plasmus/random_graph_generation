import pandas as pd
from multiprocessing import Pool
from tqdm import tqdm
import pickle as pkl

from typing import Callable, TypeVar, Sequence

import igraph as ig

from random_graph_generation.utils import add_graph_stats, get_graphs_path


ConfigSchema = TypeVar("ConfigSchema")


def generate_graphs_parallel(
    graph_generator: Callable[[tuple[int, ConfigSchema]], ig.Graph],
    worker_args: Sequence[ConfigSchema],
) -> None:
    df = pd.DataFrame()
    n_graphs = len(worker_args)
    graph_list: list[ig.Graph | None] = [None] * n_graphs

    with Pool(8) as pool:
        for idx, result in tqdm(
            pool.imap_unordered(
                graph_generator,
                enumerate(worker_args),
                chunksize=1,
            ),
            total=n_graphs,
        ):
            graph_list[idx] = result

    for g in graph_list:
        assert g is not None, "One of the graphs did not compute"
        df = add_graph_stats(df, g)

    graph_path = get_graphs_path(f"{graph_generator.__name__}_graphs.pkl")

    with open(graph_path, "wb") as f:
        pkl.dump(graph_list, f)
