import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import networkx as nx

from models import DeliveryNetwork
from recurrence import recursive_route_cost
from greedy_dp import select_parcels_greedy, calculate_time_windows_dp
from graph_algos import dijkstra_shortest_paths, build_mst_kruskal, tsp_brute_force

import networkx as nx
import random

def profile_scalability(network):
    """
    Profiles TSP execution times on dynamically grown networks to measure scalability.
    """
    print("\n--- Profiling TSP Scalability ---")
    
    n_values = range(3, 10)
    times = []
    
    for n in n_values:
        # Generate dummy distance matrices
        locations = list(range(n))
        net = DeliveryNetwork()
        net.locations = locations
        net.distance_matrix = [[abs(i-j)*10 for j in locations] for i in locations]
        
        start = time.time()
        tsp_brute_force(net, locations[1:])
        times.append(time.time() - start)
        
    plt.figure()
    plt.plot(list(n_values), times, marker='o', color='purple')
    plt.title('TSP Brute Force: Execution Time vs Locations')
    plt.xlabel('Number of Locations (n)')
    plt.ylabel('Execution Time (s)')
    plt.grid()
    plt.savefig('images/tsp_time_scalability.png')
    plt.close()
    print("Saved TSP Scalability plot.")

def profile_greedy(network):
    """
    Plots profit vs weight correlation of selected greedy elements vs overall.
    """
    all_parcels = list(network.parcels.values())
    w_all = [p['weight'] for p in all_parcels]
    v_all = [p['value'] for p in all_parcels]
    
    selected_ids, sel_value, sel_weight_total = select_parcels_greedy(network.parcels, network.vehicle_capacity)
    
    sel_w = [network.parcels[i]['weight'] for i in selected_ids]
    sel_v = [network.parcels[i]['value'] for i in selected_ids]

    plt.figure()
    plt.scatter(w_all, v_all, color='red', label='Unselected Parcels')
    plt.scatter(sel_w, sel_v, color='green', label='Selected Parcels (Greedy)')
    plt.title('Greedy Selection: Parcel Value vs Weight')
    plt.xlabel('Weight')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.savefig('images/greedy_profit_weight.png')
    plt.close()
    print("Saved Greedy Profit plot.")

def plot_mst_route(network):
    mst_edges, cost = build_mst_kruskal(network)
    
    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)
        
    pos = nx.spring_layout(G, seed=42)
    plt.figure()
    
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    nx.draw_networkx_edges(G, pos, width=2)
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Minimum Spanning Tree (Kruskal's)")
    plt.axis("off")
    plt.savefig('images/mst_networkx.png')
    plt.close()
    print("Saved MST NetworkX Map.")

def main():
    print("Starting Delivery Route Experiments...\n")
    net = DeliveryNetwork()

    # 1. Recurrence
    start = time.time()
    cost = recursive_route_cost(net, 0, set([1, 2, 3, 4]))
    print(f"1. Recurrence (Cost to visit all): {cost} [Took {time.time()-start:.6f}s]")

    # 2. Greedy Parcel Selection
    sel, v, w = select_parcels_greedy(net.parcels, net.vehicle_capacity)
    print(f"2. Greedy Selection: Items {sel} (Value: {v}, Weight: {w}/{net.vehicle_capacity})")

    # 3. Dijkstra Paths
    dists = dijkstra_shortest_paths(net, 0)
    print(f"3. Dijkstra Shortest Distances from Warehouse (0): {dists}")

    # 4. MST
    mst_edges, mst_cost = build_mst_kruskal(net)
    print(f"4. Minimum Spanning Tree: {mst_edges} (Cost: {mst_cost})")

    # 5. TSP
    best_route, tsp_cost = tsp_brute_force(net, [1, 2, 3, 4])
    print(f"5. Optimal TSP Route (Brute Force): {best_route} (Cost: {tsp_cost})")

    # 6. DP Time Window Validation for optimal route
    valid, arrival = calculate_time_windows_dp(net, best_route)
    print(f"6. DP Time window alignment for optimal route -> Valid? {valid} (Ending elapsed time: {arrival})")

    # Measurements & Plots
    profile_scalability(net)
    profile_greedy(net)
    plot_mst_route(net)

    print("\nAll operations completed and visualized successfully.")

if __name__ == "__main__":
    main()
