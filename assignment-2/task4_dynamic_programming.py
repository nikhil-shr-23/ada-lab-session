import os
import time
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(SCRIPT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

def knapsack_recursive(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
        
    if wt[n-1] > W:
        return knapsack_recursive(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapsack_recursive(W-wt[n-1], wt, val, n-1),
            knapsack_recursive(W, wt, val, n-1)
        )

def knapsack_dp(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
                
    return K[n][W], K

def print_dp_table(K, W, n):
    print("\nDP Table (Rows: Items 0 to n, Columns: Capacity 0 to W):")
    
    # Print header
    header = "    "
    for w in range(W + 1):
        header += f"{w:4}"
    print(header)
    print("-" * len(header))
    
    # Print rows
    for i in range(n + 1):
        row_str = f"{i:2} |"
        for w in range(W + 1):
            row_str += f"{K[i][w]:4}"
        print(row_str)

def run_experiment():
    print("Running Task 4: Dynamic Programming Fundamentals (0/1 Knapsack)...")
    
    # Sample run to print DP table
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    
    print(f"Sample Items Values: {val}")
    print(f"Sample Items Weights: {wt}")
    print(f"Knapsack Capacity: {W}")
    
    max_val_dp, K_table = knapsack_dp(W, wt, val, n)
    print(f"\nMax value using DP: {max_val_dp}")
    print_dp_table(K_table, W, n)
    
    # Performance comparison
    print("\nRunning performance comparison (Recursive vs DP)...")
    input_sizes = list(range(10, 25, 2))
    time_rec = []
    time_dp = []
    
    for size in input_sizes:
        import random
        # Create larger sample sizes
        random.seed(42)  # For consistent timing evaluation
        cur_val = [random.randint(10, 100) for _ in range(size)]
        cur_wt = [random.randint(1, 20) for _ in range(size)]
        cur_W = 50
        
        # Test DP
        start_time = time.perf_counter()
        knapsack_dp(cur_W, cur_wt, cur_val, size)
        time_dp.append(time.perf_counter() - start_time)
        
        # Test Recursive
        start_time = time.perf_counter()
        knapsack_recursive(cur_W, cur_wt, cur_val, size)
        time_rec.append(time.perf_counter() - start_time)
        
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(input_sizes, time_rec, label='Recursive O(2^n)', marker='o', color='red')
    plt.plot(input_sizes, time_dp, label='Dynamic Programming O(nW)', marker='s', color='blue')
    
    plt.title('0/1 Knapsack: Recursive vs DP Execution Time')
    plt.xlabel('Number of Items (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.yscale('log') # Log scale helps visualize exponential vs polynomial difference clearly
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(IMAGES_DIR, 'task4_dp_plot.png'))
    plt.close()
    print("Task 4 complete! Plot saved to images/task4_dp_plot.png")

if __name__ == "__main__":
    run_experiment()
