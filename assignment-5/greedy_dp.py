# Greedy + Dynamic Programming for Delivery Planning

def select_parcels_greedy(parcels, max_capacity):
    """
    Task 4: Greedy parcel selection using value-to-weight ratio.
    Returns the list of parcel IDs chosen to maximize value without exceeding capacity.
    """
    items = []
    for pid, data in parcels.items():
        items.append((pid, data['value'], data['weight'], data['value']/data['weight']))
        
    items.sort(key=lambda x: x[3], reverse=True)
    
    selected = []
    current_weight = 0
    total_value = 0
    
    for pid, v, w, r in items:
        if current_weight + w <= max_capacity:
            selected.append(pid)
            current_weight += w
            total_value += v
            
    return selected, total_value, current_weight

def calculate_time_windows_dp(network, route):
    """
    Task 4: Use DP to check if a specific route sequence satisfies all parcel time windows.
    route is an ordered list of locations.
    Returns (True, max_delay) or (False, None)
    """
    n = len(route)
    dp = [0] * n
    
    for i in range(1, n):
        prev = route[i-1]
        curr = route[i]
        
        arrival = dp[i-1] + network.get_distance(prev, curr)
        
        if curr in network.parcels:
            tw_start, tw_end = network.parcels[curr]['time_window']
            
            if arrival > tw_end:
                return False, arrival
                
            dp[i] = max(arrival, tw_start)
        else:
            dp[i] = arrival
            
    return True, dp[-1]

if __name__ == "__main__":
    from models import DeliveryNetwork
    net = DeliveryNetwork()
    
    selected_parcels, val, weight = select_parcels_greedy(net.parcels, net.vehicle_capacity)
    print("Greedy Selection:", selected_parcels, "Value:", val, "Weight:", weight)
    
    valid, end_time = calculate_time_windows_dp(net, [0, 1, 4])
    print("Route [0, 1, 4] valid?", valid, "End Time:", end_time)
