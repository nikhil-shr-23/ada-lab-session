from graph_utils import Graph


def run_task():
    print("=== Task 5: Minimum Spanning Tree Algorithms ===")
    graph = Graph(vertices=6, directed=False)
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 2),
        (4, 5, 6),
    ]

    for u, v, w in edges:
        graph.add_edge(u, v, w)

    prim_edges, prim_weight = graph.prim_mst()
    kruskal_edges, kruskal_weight = graph.kruskal_mst()

    print("Prim MST edges:", prim_edges, "Total weight:", prim_weight)
    print("Kruskal MST edges:", kruskal_edges, "Total weight:", kruskal_weight)


if __name__ == "__main__":
    run_task()
