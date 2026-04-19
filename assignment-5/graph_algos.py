# Graph Algorithms & TSP

import itertools
import networkx as nx

def dijkstra_shortest_paths(network, start_node=0):
    """
    Task 5: Dijkstra's to find shortest distances to all nodes from a source.
    """
    distances = {i: float('inf') for i in network.locations}
    distances[start_node] = 0
    visited = set()
    
    unvisited = network.locations.copy()
    
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)
        visited.add(current)
        
        for neighbor in network.locations:
            if neighbor == current or neighbor in visited:
                continue
                
            weight = network.get_distance(current, neighbor)
            if distances[current] + weight < distances[neighbor]:
                distances[neighbor] = distances[current] + weight
                
    return distances

def build_mst_kruskal(network):
    """
    Build Minimum Spanning Tree using Kruskal's Algorithm.
    """
    edges = []
    for i in network.locations:
        for j in network.locations:
            if i < j:
                edges.append((network.get_distance(i, j), i, j))
                
    edges.sort()
    
    parent = {i: i for i in network.locations}
    def find(i):
        if parent[i] == i:
            return i
        return find(parent[i])
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            
    mst_edges = []
    mst_cost = 0
    
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))
            mst_cost += weight
            
    return mst_edges, mst_cost

def tsp_brute_force(network, locations_to_visit):
    """
    Task 6: Exact TSP Implementation via Permutations
    """
    nodes = list(locations_to_visit)
    min_cost = float('inf')
    best_route = None
    
    for perm in itertools.permutations(nodes):
        route = [0] + list(perm) + [0]
        cost = sum(network.get_distance(route[i], route[i+1]) for i in range(len(route)-1))
        
        if cost < min_cost:
            min_cost = cost
            best_route = route
            
    return best_route, min_cost

if __name__ == "__main__":
    from models import DeliveryNetwork
    net = DeliveryNetwork()
    
    print("Dijkstra distances from 0:", dijkstra_shortest_paths(net))
    print("MST:", build_mst_kruskal(net))
    print("TSP Exact:", tsp_brute_force(net, [1, 2, 3, 4]))
