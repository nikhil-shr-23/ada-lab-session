from graph_utils import Graph


def run_task():
    print("=== Task 3: Topological Sorting ===")
    graph = Graph(vertices=6, directed=True)
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

    for u, v in edges:
        graph.add_edge(u, v)

    print("Topological Order:", graph.topological_sort())


if __name__ == "__main__":
    run_task()
