from graph_utils import Graph


def run_task():
    print("=== Task 4: Shortest Path Algorithms ===")

    weighted_edges = [
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

    bellman_graph = Graph(vertices=5, directed=True)
    for u, v, w in weighted_edges:
        bellman_graph.add_edge(u, v, w)

    dijkstra_graph = Graph(vertices=5, directed=True)
    for u, v, w in weighted_edges:
        if w >= 0:
            dijkstra_graph.add_edge(u, v, w)

    print("Dijkstra distances from 0 (non-negative graph):", dijkstra_graph.dijkstra(0))
    print("Bellman-Ford distances from 0:", bellman_graph.bellman_ford(0))


if __name__ == "__main__":
    run_task()
