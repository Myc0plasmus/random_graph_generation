import numpy as np
import igraph as ig
from matplotlib import pyplot as plt


def graphVisualization(name:str, graph: ig.Graph):

    fig, ax = plt.subplots(figsize=(16, 16))

    layout = graph.layout_fruchterman_reingold(
        niter=400,   # default ~1000 (too slow)
        # grid=True
    )  # or lgl/fr
    print("create layout")
    coords = np.asarray(layout.coords)

    bins = [0.1 * i for i in range(1, 10)]
    sizes = (np.digitize(immuneNet.proportions, bins) + 3)**1.5

    # ---- FAST EDGE DRAWING ----
    edge_coords = coords[edges]  # (E, 2, 2)
    lc = LineCollection(edge_coords, linewidths=0.3, alpha=0.3)
    ax.add_collection(lc)

    # ---- nodes ----
    ax.scatter(coords[:,0], coords[:,1], s=sizes)

    ax.axis("off")
    
    ax.set_title(name)

    plt.show()

