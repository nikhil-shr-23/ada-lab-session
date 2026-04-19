import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
from scheduling import backtracking_scheduling, branch_and_bound_scheduling
from string_matching import naive_string_matching, kmp_string_matching
import random

def generate_flights(n):
    """Generates a list of n flights with random non-overlapping intervals."""
    flights = []
    current_time = 0
    for i in range(1, n + 1):
        duration = random.randint(1, 3)
        flights.append((f'F{i}', current_time, current_time + duration))
        current_time += duration + random.randint(0, 2)
    return flights

def profile_scheduling():
    print("\n--- Profiling Crew Scheduling ---")
    crew_members = ['C1', 'C2', 'C3']
    
    n_values = list(range(4, 11))
    bt_times = []
    bb_times = []
    bt_memory = []
    bb_memory = []
    
    for n in n_values:
        flights = generate_flights(n)
        
        # Profile Backtracking
        start_time = time.time()
        mem_usage_bt = memory_usage((backtracking_scheduling, (flights, crew_members)), multiprocess=False)
        bt_times.append(time.time() - start_time)
        bt_memory.append(max(mem_usage_bt) - min(mem_usage_bt))
        
        # Profile Branch & Bound
        start_time = time.time()
        mem_usage_bb = memory_usage((branch_and_bound_scheduling, (flights, crew_members)), multiprocess=False)
        bb_times.append(time.time() - start_time)
        bb_memory.append(max(mem_usage_bb) - min(mem_usage_bb))

    # Plotting Scheduling Times
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, bt_times, label='Backtracking', marker='o')
    plt.plot(n_values, bb_times, label='Branch & Bound', marker='o')
    plt.title('Execution Time: Backtracking vs Branch & Bound')
    plt.xlabel('Number of Flights')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('images/scheduling_time.png')
    print("Saved execution time plot to images/scheduling_time.png")
    plt.close()

def profile_string_matching():
    print("\n--- Profiling String Matching ---")
    
    text_sizes = [1000, 5000, 10000, 20000, 50000]
    pattern = "GATTACA"
    naive_times = []
    kmp_times = []
    naive_comps = []
    kmp_comps = []
    
    for size in text_sizes:
        # Generate random text
        text = ''.join(random.choices("ACGT", k=size))
        # Ensure pattern exists at the end
        text = text[:-len(pattern)] + pattern
        
        # Naive
        start_time = time.time()
        _, comps_n = naive_string_matching(text, pattern)
        naive_times.append(time.time() - start_time)
        naive_comps.append(comps_n)
        
        # KMP
        start_time = time.time()
        _, comps_k = kmp_string_matching(text, pattern)
        kmp_times.append(time.time() - start_time)
        kmp_comps.append(comps_k)

    # Plotting comparisons
    plt.figure(figsize=(10, 5))
    plt.plot(text_sizes, naive_comps, label='Naive Comparisons', marker='o')
    plt.plot(text_sizes, kmp_comps, label='KMP Comparisons', marker='o')
    plt.title('Comparisons: Naive vs KMP (Pattern: GATTACA)')
    plt.xlabel('Text Size')
    plt.ylabel('Number of Comparisons')
    plt.legend()
    plt.grid(True)
    plt.savefig('images/string_comparisons.png')
    print("Saved comparisons plot to images/string_comparisons.png")
    plt.close()
    
    # Print results
    print(f"Naive Comparisons: {naive_comps}")
    print(f"KMP Comparisons: {kmp_comps}")

def main():
    print("Starting Experiments...")
    
    # 1. Backtracking Test
    flights = [('F1', 9, 11), ('F2', 10, 12), ('F3', 11, 13), ('F4', 12, 14), ('F5', 13, 15)]
    crew_members = ['C1', 'C2', 'C3']
    print("\n--- Backtracking Sample Run ---")
    schedule_bt = backtracking_scheduling(flights, crew_members)
    print("Feasible Schedule:", schedule_bt)
    
    # 2. Branch and Bound Test
    print("\n--- Branch & Bound Sample Run ---")
    schedule_bb = branch_and_bound_scheduling(flights, crew_members)
    print("Optimal Load-Balanced Schedule:", schedule_bb)

    # 3. String Matching Profiling
    profile_string_matching()

    # 4. Scheduling Profiling
    profile_scheduling()

    print("\nAll tasks completed successfully!")

if __name__ == "__main__":
    main()
