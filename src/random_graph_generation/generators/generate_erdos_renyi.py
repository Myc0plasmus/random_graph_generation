from random_graph_generation.creation import erdos_renyi
from random_graph_generation.schemas import ErdosRenyiSchema
from random_graph_generation.parallel_generation import generate_graphs_parallel


def main() -> None:
    erdos_renyi_schema = ErdosRenyiSchema(n=1000, p=0.05)
    n_graphs = 100
    worker_args = [erdos_renyi_schema] * n_graphs

    generate_graphs_parallel(erdos_renyi, worker_args)


if __name__ == "__main__":
    main()
