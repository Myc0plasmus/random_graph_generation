import igraph as ig
import random
from math import comb
from random_graph_generation.utils import nth_combination
from random_graph_generation.schemas import ErdosRenyiSchema
from random_graph_generation.parallel_generation import multiprocess_wrapper


@multiprocess_wrapper
def erdos_renyi(config: ErdosRenyiSchema) -> ig.Graph:
    graph = ig.Graph()
    vertices = range(config.n)
    graph.add_vertices(vertices)
    possible_edges = comb(config.n, 2)

    for i in range(possible_edges):
        if random.random() < config.p:
            edge = nth_combination(list(vertices), 2, i)
            source = edge[0]
            end = edge[1]
            graph.add_edge(source, end)
    return graph
