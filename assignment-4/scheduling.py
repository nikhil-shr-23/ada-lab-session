import copy

def is_valid_assignment(flight, assigned_flights):
    """
    Check if a flight can be assigned to a crew member given their already assigned flights.
    Constraints:
    - No overlap
    - At least 1 hour of rest time between flights
    
    flight: (id, start_time, end_time)
    assigned_flights: list of flights already assigned to this crew member
    """
    start_time, end_time = flight[1], flight[2]
    for assigned in assigned_flights:
        a_start, a_end = assigned[1], assigned[2]
        
        # Check overlap and rest time. 
        # For rest time of 1, the new flight must start at least 1 hour after the assigned ends, 
        # or end at least 1 hour before the assigned starts.
        if not (start_time >= a_end + 1 or end_time <= a_start - 1):
            return False
            
    return True

def backtracking_scheduling(flights, crew_members, index=0, schedule=None):
    """
    Task 1: Basic backtracking to find the first feasible schedule.
    Returns a dictionary mapping crew member -> list of assigned flights, or None if no schedule is possible.
    """
    if schedule is None:
        schedule = {crew: [] for crew in crew_members}
        
    if index == len(flights):
        return copy.deepcopy(schedule)
        
    current_flight = flights[index]
    
    for crew in crew_members:
        if is_valid_assignment(current_flight, schedule[crew]):
            # Assign
            schedule[crew].append(current_flight)
            
            # Recurse
            result = backtracking_scheduling(flights, crew_members, index + 1, schedule)
            if result:
                return result
                
            # Backtrack
            schedule[crew].pop()
            
    return None

def calculate_max_load(schedule):
    """Calculate the maximum number of flights assigned to a single crew member."""
    if not schedule:
        return float('inf')
    return max(len(flights) for flights in schedule.values())

def branch_and_bound_scheduling(flights, crew_members, index=0, schedule=None, current_best=None):
    """
    Task 2: Branch and Bound scheduling to find a schedule that balances the load (minimizes max flights per crew member).
    """
    if schedule is None:
        schedule = {crew: [] for crew in crew_members}
        current_best = {'schedule': None, 'max_load': float('inf')}
        
    # Bounding condition: if the current maximum load is already >= our best known max load, 
    # then adding more flights won't improve it, but wait: since we want to MINIMIZE the max load, 
    if current_best['max_load'] != float('inf'):
        # If the partial schedule already has someone with max_load >= current best, prune.
        current_max = max((len(f) for f in schedule.values()), default=0)
        # Even if we hit the current max_load, we might just tie it. We only prune if it's strictly > current_best['max_load']
        # Or if it's equal, we could still find a tie. Let's prune if current_max >= current_best['max_load']
        if current_max >= current_best['max_load']:
            return current_best['schedule']

    if index == len(flights):
        current_max = calculate_max_load(schedule)
        if current_max < current_best['max_load']:
            current_best['max_load'] = current_max
            current_best['schedule'] = copy.deepcopy(schedule)
        return current_best['schedule']
        
    current_flight = flights[index]
    
    for crew in crew_members:
        if is_valid_assignment(current_flight, schedule[crew]):
            schedule[crew].append(current_flight)
            branch_and_bound_scheduling(flights, crew_members, index + 1, schedule, current_best)
            schedule[crew].pop()
            
    return current_best['schedule']

