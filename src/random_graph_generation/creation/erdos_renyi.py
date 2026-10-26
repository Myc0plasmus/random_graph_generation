import igraph as ig
import random
from math import comb
from tqdm import tqdm
from multiprocessing import Pool
import pandas as pd
from random_graph_generation.utils import nth_combination

def erdos_renyi(n_vertices: int, p: float) -> ig.Graph:
    graph = ig.Graph()
    vertices = range(n_vertices)
    graph.add_vertices(vertices)
    possible_edges = comb(n_vertices,2)

    for i in range(possible_edges):
        if random.random() < p :
            edge = nth_combination(list(vertices), 2, i)
            source = edge[0]
            end = edge[1]
            graph.add_edge(source, end)
    return graph


