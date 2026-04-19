# Recurrence-based Route Cost Function
# Task 3: Recursive function to evaluate absolute minimum topological cost visiting all nodes once.

from models import DeliveryNetwork

def recursive_route_cost(network, current_node, unvisited, current_time=0):
    """
    Recursive function to calculate the minimum cost to visit all remaining unvisited nodes and return to base.
    Base Case: unvisited is empty -> cost is distance back to 0.
    Recursive Case: minimize (distance to next + cost of remaining)
    """
    if not unvisited:
        return network.get_distance(current_node, 0)
        
    min_cost = float('inf')
    
    for next_node in unvisited:
        travel_cost = network.get_distance(current_node, next_node)
        
        # Recurse
        remaining = unvisited.copy()
        remaining.remove(next_node)
        
        cost = travel_cost + recursive_route_cost(network, next_node, remaining, current_time + travel_cost)
        
        if cost < min_cost:
            min_cost = cost
            
    return min_cost

if __name__ == "__main__":
    net = DeliveryNetwork()
    locations_to_visit = set([1, 2, 3, 4])
    optimal_cost = recursive_route_cost(net, 0, locations_to_visit)
    print("Optimal recursive distance to visit all and return:", optimal_cost)
