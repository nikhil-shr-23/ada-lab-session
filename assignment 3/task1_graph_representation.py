from graph_utils import Graph


def run_task():
    print("=== Task 1: Graph Representation ===")
    graph = Graph(vertices=6, directed=False)
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]

    for u, v in edges:
        graph.add_edge(u, v)

    print("Adjacency List:", dict(graph.adj_list))
    print("Adjacency Matrix:")
    for row in graph.matrix:
        print(row)


if __name__ == "__main__":
    run_task()
