import os
import time
import math
import itertools
import matplotlib.pyplot as plt
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(SCRIPT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def tsp_brute_force(cities):
    n = len(cities)
    if n <= 1:
        return 0, []
        
    # Precompute distances
    dist_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = calculate_distance(cities[i], cities[j])
            
    all_indices = list(range(n))
    min_path = float('inf')
    best_route = []
    
    # Generate all permutations (n! permutations)
    for perm in itertools.permutations(all_indices):
        current_path_dist = 0.0
        
        for i in range(n - 1):
            current_path_dist += dist_matrix[perm[i]][perm[i+1]]
        current_path_dist += dist_matrix[perm[n-1]][perm[0]] # Return to origin
        
        if current_path_dist < min_path:
            min_path = current_path_dist
            best_route = perm
            
    return min_path, best_route

def run_experiment():
    print("Running Task 5: Travelling Salesman Problem (Brute Force)...")
    
    # We will measure the time for N = 3 up to N = 10 
    # (Going beyond 10 with O(n!) takes too long)
    N_values = list(range(3, 11))
    times = []
    
    for n in N_values:
        random.seed(42)
        # Generate n random cities
        cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
        
        start_time = time.perf_counter()
        min_dist, _ = tsp_brute_force(cities)
        end_time = time.perf_counter()
        
        elapsed = end_time - start_time
        times.append(elapsed)
        print(f"N = {n}, Time = {elapsed:.6f} sec, Min Dist = {min_dist:.2f}")
        
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(N_values, times, marker='o', color='purple', linewidth=2)
    
    plt.title('TSP Brute Force: Demonstrating Exponential O(n!) Growth')
    plt.xlabel('Number of Cities (N)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    
    # Adding observation text inside the plot
    plt.text(N_values[0], max(times)*0.8, 
             "Observe the stark exponential curve as N approaches 10.", 
             fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
             
    plt.savefig(os.path.join(IMAGES_DIR, 'task5_tsp_plot.png'))
    plt.close()
    
    print("\nObservations on exponential growth:")
    print("As the number of cities (N) increases, the number of permutations is N!")
    print("This makes the brute force approach extremely impractical for N > 12.")
    print("For instance, 10! = 3,628,800 paths checked.")
    print("Task 5 complete! Plot saved to images/task5_tsp_plot.png")

if __name__ == "__main__":
    run_experiment()
