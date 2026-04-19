import os
import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "images")


def _draw_nodes(ax, positions, labels=None):
    for node, (x, y) in positions.items():
        ax.scatter(x, y, s=650, color="#d9e8fb", edgecolors="#1f4e79", linewidth=1.8, zorder=3)
        label = str(node) if labels is None else labels.get(node, str(node))
        ax.text(x, y, label, ha="center", va="center", fontsize=11, fontweight="bold", zorder=4)


def _draw_edges(ax, positions, edges, directed=False, weight_color="#444"):
    for edge in edges:
        if len(edge) == 2:
            u, v = edge
            w = None
        else:
            u, v, w = edge

        x1, y1 = positions[u]
        x2, y2 = positions[v]

        if directed:
            ax.annotate(
                "",
                xy=(x2, y2),
                xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.8, color="#2f2f2f", shrinkA=20, shrinkB=20),
                zorder=2,
            )
        else:
            ax.plot([x1, x2], [y1, y2], color="#2f2f2f", linewidth=1.8, zorder=2)

        if w is not None:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mx, my, str(w), color=weight_color, fontsize=10, fontweight="bold")


def _finish_plot(ax, title):
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.axis("off")


def create_task1_graph():
    fig, ax = plt.subplots(figsize=(8, 5))
    pos = {0: (0, 1), 1: (2, 2), 2: (2, 0), 3: (4, 2), 4: (4, 0), 5: (6, 0)}
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]
    _draw_edges(ax, pos, edges, directed=False)
    _draw_nodes(ax, pos)
    _finish_plot(ax, "Task 1/2 Graph: Representation + BFS/DFS")
    fig.savefig(os.path.join(IMAGES_DIR, "task1_task2_graph.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def create_task3_graph():
    fig, ax = plt.subplots(figsize=(8, 5))
    pos = {5: (0, 3), 4: (0, 1), 2: (2, 3), 0: (4, 2), 3: (4, 3), 1: (6, 2)}
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    _draw_edges(ax, pos, edges, directed=True)
    _draw_nodes(ax, pos)
    _finish_plot(ax, "Task 3 Graph: Topological Sorting (DAG)")
    fig.savefig(os.path.join(IMAGES_DIR, "task3_topological_graph.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def create_task4_graph():
    fig, ax = plt.subplots(figsize=(8, 5))
    pos = {0: (0, 2), 1: (2, 3), 2: (2, 1), 3: (4, 2), 4: (6, 2)}
    edges = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, 5),
        (1, 4, -4),
        (2, 3, -3),
        (2, 4, 9),
        (3, 1, -2),
        (4, 3, 7),
        (4, 0, 2),
    ]
    _draw_edges(ax, pos, edges, directed=True, weight_color="#7a1f1f")
    _draw_nodes(ax, pos)
    _finish_plot(ax, "Task 4 Graph: Shortest Paths (Weighted Directed)")
    fig.savefig(os.path.join(IMAGES_DIR, "task4_shortest_path_graph.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def create_task5_graphs():
    pos = {0: (0, 2), 1: (2, 3), 2: (2, 1), 3: (4, 2), 4: (6, 2), 5: (8, 2)}

    full_edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 2),
        (4, 5, 6),
    ]

    mst_edges = [
        (0, 2, 3),
        (2, 1, 1),
        (1, 3, 2),
        (3, 4, 2),
        (4, 5, 6),
    ]

    fig, ax = plt.subplots(figsize=(9, 5))
    _draw_edges(ax, pos, full_edges, directed=False)
    _draw_nodes(ax, pos)
    _finish_plot(ax, "Task 5 Graph: Input Weighted Undirected Graph")
    fig.savefig(os.path.join(IMAGES_DIR, "task5_input_graph.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    _draw_edges(ax, pos, mst_edges, directed=False, weight_color="#0f5132")
    _draw_nodes(ax, pos)
    _finish_plot(ax, "Task 5 Graph: MST Result")
    fig.savefig(os.path.join(IMAGES_DIR, "task5_mst_graph.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    create_task1_graph()
    create_task3_graph()
    create_task4_graph()
    create_task5_graphs()
    print("PNG files generated in:", IMAGES_DIR)


if __name__ == "__main__":
    main()
