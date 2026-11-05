import pickle as pkl

from rich.console import Console

from random_graph_generation.utils import get_graphs_path, get_tables_path
from .utils import create_graph_stats_df


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
