from graph_utils import Graph


def run_task():
    print("=== Task 2: BFS and DFS Traversal ===")
    graph = Graph(vertices=6, directed=False)
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]

    for u, v in edges:
        graph.add_edge(u, v)

    print("BFS from node 0:", graph.bfs(0))
    print("DFS from node 0:", graph.dfs(0))


if __name__ == "__main__":
    run_task()
