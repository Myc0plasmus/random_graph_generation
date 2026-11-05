import pandas as pd


def compute_column_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute summary statistics across all graphs in the dataset.

    Each row in df represents one graph.
    The returned DataFrame summarizes the distribution of
    selected graph statistics across all graphs.
    """

    # Statistics that make sense to summarize across graphs.
    columns = [
        "n_vertices",
        "n_edges",
        "density",
        "mean_degree",
        "min_degree",
        "max_degree",
        "n_components",
        "largest_component_size",
        "mean_degree_centrality",
        "global_transitivity",
    ]

    # Keep only columns that actually exist in the DataFrame.
    columns = [col for col in columns if col in df.columns]

    # Convert selected columns to numeric values.
    numeric_df = df[columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    # Calculate dataset-level summaries.
    summary = numeric_df.agg(["min", "max", "mean", "std"]).T

    summary.index.name = "graph_statistic"

    return summary
