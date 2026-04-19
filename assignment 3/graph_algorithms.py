from collections import defaultdict, deque
import heapq
import math


class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.adj_list = defaultdict(list)
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w=1):
        self.adj_list[u].append((v, w))
        self.matrix[u][v] = w
        if not self.directed:
            self.adj_list[v].append((u, w))
            self.matrix[v][u] = w

    def bfs(self, start):
        visited = [False] * self.vertices
        order = []
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        visited = [False] * self.vertices
        order = []

        def _dfs(node):
            visited[node] = True
            order.append(node)
            for neighbor, _ in self.adj_list[node]:
                if not visited[neighbor]:
                    _dfs(neighbor)

        _dfs(start)
        return order

    def topological_sort(self):
        if not self.directed:
            raise ValueError("Topological sort requires a directed graph.")

        indegree = [0] * self.vertices
        for u in range(self.vertices):
            for v, _ in self.adj_list[u]:
                indegree[v] += 1

        queue = deque([i for i in range(self.vertices) if indegree[i] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor, _ in self.adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != self.vertices:
            raise ValueError("Graph contains a cycle; topological sort not possible.")

        return topo_order

    def dijkstra(self, source):
        dist = [math.inf] * self.vertices
        dist[source] = 0
        min_heap = [(0, source)]

        while min_heap:
            current_dist, node = heapq.heappop(min_heap)
            if current_dist > dist[node]:
                continue

            for neighbor, weight in self.adj_list[node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

        return dist

    def bellman_ford(self, source):
        dist = [math.inf] * self.vertices
        dist[source] = 0

        edges = []
        for u in range(self.vertices):
            for v, w in self.adj_list[u]:
                edges.append((u, v, w))

        for _ in range(self.vertices - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != math.inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break

        for u, v, w in edges:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                raise ValueError("Negative weight cycle detected.")

        return dist

    def prim_mst(self):
        if self.directed:
            raise ValueError("Prim MST is for undirected graphs.")

        visited = [False] * self.vertices
        min_heap = [(0, 0, -1)]
        mst_edges = []
        total_weight = 0

        while min_heap and len(mst_edges) < self.vertices:
            weight, node, parent = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True
            total_weight += weight
            if parent != -1:
                mst_edges.append((parent, node, weight))

            for neighbor, w in self.adj_list[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (w, neighbor, node))

        if not all(visited):
            raise ValueError("Graph is disconnected; MST not possible.")

        return mst_edges, total_weight

    def kruskal_mst(self):
        if self.directed:
            raise ValueError("Kruskal MST is for undirected graphs.")

        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True

        edge_set = set()
        edges = []
        for u in range(self.vertices):
            for v, w in self.adj_list[u]:
                key = tuple(sorted((u, v)))
                if key not in edge_set:
                    edge_set.add(key)
                    edges.append((w, u, v))

        edges.sort()
        mst_edges = []
        total_weight = 0

        for w, u, v in edges:
            if union(u, v):
                mst_edges.append((u, v, w))
                total_weight += w
                if len(mst_edges) == self.vertices - 1:
                    break

        if len(mst_edges) != self.vertices - 1:
            raise ValueError("Graph is disconnected; MST not possible.")

        return mst_edges, total_weight


def main():
    print("=== Task 1 and 2: Graph Representation + BFS/DFS ===")
    social_graph = Graph(vertices=6, directed=False)
    social_edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]
    for u, v in social_edges:
        social_graph.add_edge(u, v)

    print("Adjacency List:", dict(social_graph.adj_list))
    print("Adjacency Matrix:")
    for row in social_graph.matrix:
        print(row)
    print("BFS from 0:", social_graph.bfs(0))
    print("DFS from 0:", social_graph.dfs(0))

    print("\n=== Task 3: Topological Sorting ===")
    project_graph = Graph(vertices=6, directed=True)
    dependency_edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    for u, v in dependency_edges:
        project_graph.add_edge(u, v)
    print("Topological Order:", project_graph.topological_sort())

    print("\n=== Task 4: Shortest Paths (Dijkstra + Bellman-Ford) ===")
    road_graph = Graph(vertices=5, directed=True)
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
    for u, v, w in weighted_edges:
        road_graph.add_edge(u, v, w)

    # Dijkstra is valid only for non-negative weights.
    non_negative_graph = Graph(vertices=5, directed=True)
    for u, v, w in weighted_edges:
        if w >= 0:
            non_negative_graph.add_edge(u, v, w)
    print("Dijkstra distances from 0 (non-negative graph):", non_negative_graph.dijkstra(0))
    print("Bellman-Ford distances from 0:", road_graph.bellman_ford(0))

    print("\n=== Task 5: Minimum Spanning Tree (Prim + Kruskal) ===")
    network_graph = Graph(vertices=6, directed=False)
    network_edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4),
        (3, 4, 2),
        (4, 5, 6),
    ]
    for u, v, w in network_edges:
        network_graph.add_edge(u, v, w)

    prim_edges, prim_weight = network_graph.prim_mst()
    kruskal_edges, kruskal_weight = network_graph.kruskal_mst()
    print("Prim MST edges:", prim_edges, "Total weight:", prim_weight)
    print("Kruskal MST edges:", kruskal_edges, "Total weight:", kruskal_weight)


if __name__ == "__main__":
    main()
