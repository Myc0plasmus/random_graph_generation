
Imię|Nazwisko|nr. indeksu
-|-|-
Natan|Jabłoński|155621

# Zaimplementowane algorytmy do generowania grafów

## Erdos Rényi
```python
@multiprocess_wrapper
def erdos_renyi(config: ErdosRenyiSchema) -> ig.Graph:
    """Generate an Erdős–Rényi random graph.

    Create a random graph where each possible edge is included
    independently with probability ``p``.

    :param config: Configuration containing the number of vertices
        and the edge probability.
    :type config: ErdosRenyiSchema
    :return: The generated random graph.
    :rtype: ig.Graph
    :raises ValueError: If the configuration contains invalid parameters.
    """
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

```




