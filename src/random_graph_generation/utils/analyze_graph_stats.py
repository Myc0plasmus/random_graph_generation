import math

import matplotlib.pyplot as plt
import pandas as pd



def analyze_graph_stats(
    df: pd.DataFrame,
    columns: list[str] | None = None,
    ncols: int = 3,
    figsize_per_plot: tuple[float, float] = (5, 4),
) -> None:
    """
    Plot boxplots for numerical graph statistics across generated graphs.

    Parameters
    ----------
    df : pd.DataFrame
        One row per graph.
    columns : list[str] | None
        Specific numerical columns to plot. If None, automatically
        selects numerical columns, excluding booleans.
    ncols : int
        Number of subplot columns.
    figsize_per_plot : tuple[float, float]
        Width and height allocated to each subplot.
    """
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    if columns is None:
        columns = df.select_dtypes(include="number").columns.tolist()
        columns = [
            col for col in columns
            if not pd.api.types.is_bool_dtype(df[col])
        ]
    else:
        missing = [col for col in columns if col not in df.columns]
        if missing:
            raise ValueError(f"Columns not found: {missing}")

        non_numeric = [
            col for col in columns
            if not pd.api.types.is_numeric_dtype(df[col])
            or pd.api.types.is_bool_dtype(df[col])
        ]
        if non_numeric:
            raise ValueError(
                f"Columns must be numerical (not boolean): {non_numeric}"
            )

    # Drop columns with no usable numerical observations.
    columns = [
        col for col in columns
        if df[col].notna().any()
    ]

    if not columns:
        raise ValueError("No usable numerical columns to plot.")

    nrows = math.ceil(len(columns) / ncols)
    width, height = figsize_per_plot

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(width * ncols, height * nrows),
        squeeze=False,
    )

    for ax, col in zip(axes.flat, columns):
        values = df[col].dropna()

        ax.boxplot(values, vert=True)
        ax.set_title(col.replace("_", " ").title())
        ax.set_ylabel("Value")
        ax.set_xticks([])
        ax.grid(axis="y", alpha=0.3)

        # Show the number of observations used.
        ax.text(
            0.98,
            0.98,
            f"n = {len(values)}",
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=9,
        )

    # Hide unused subplot slots.
    for ax in axes.flat[len(columns):]:
        ax.set_visible(False)

    fig.suptitle("Distribution of Graph Statistics", fontsize=16)
    fig.tight_layout()
    plt.show()

