import os
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from memory_profiler import memory_usage

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(SCRIPT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

def max_subarray_brute_force(arr):
    n = len(arr)
    if n == 0:
        return 0, -1, -1
    
    max_sum = float('-inf')
    start_idx = -1
    end_idx = -1
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_idx = i
                end_idx = j
                
    return max_sum, start_idx, end_idx

def max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i
            
    right_sum = float('-inf')
    total = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j
            
    return left_sum + right_sum, max_left, max_right

def max_subarray_divide_conquer(arr, low, high):
    if low == high:
        return arr[low], low, high
        
    mid = (low + high) // 2
    
    left_sum, left_low, left_high = max_subarray_divide_conquer(arr, low, mid)
    right_sum, right_low, right_high = max_subarray_divide_conquer(arr, mid + 1, high)
    cross_sum, cross_low, cross_high = max_crossing_subarray(arr, low, mid, high)
    
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_low, left_high
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_low, right_high
    else:
        return cross_sum, cross_low, cross_high

def run_experiment():
    input_sizes = [50, 100, 200, 400, 800, 1600]
    time_brute = []
    time_dc = []
    
    for size in input_sizes:
        arr = [random.randint(-100, 100) for _ in range(size)]
        
        # Test Brute Force
        start_time = time.perf_counter()
        max_subarray_brute_force(arr)
        time_brute.append(time.perf_counter() - start_time)
        
        # Test Divide & Conquer
        start_time = time.perf_counter()
        max_subarray_divide_conquer(arr, 0, len(arr)-1)
        time_dc.append(time.perf_counter() - start_time)
        
    # Plotting Timing
    plt.figure(figsize=(10, 5))
    plt.plot(input_sizes, time_brute, label='Brute Force O(n^2)', marker='o')
    plt.plot(input_sizes, time_dc, label='Divide & Conquer O(n log n)', marker='s')
    
    plt.title('Max Subarray Performance: Brute Force vs Divide & Conquer')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(IMAGES_DIR, 'task1_plot.png'))
    plt.close()

if __name__ == "__main__":
    print("Running Task 1: Divide and Conquer Algorithms (Max Subarray)...")
    
    # Memory profiling sample run
    arr_sample = [random.randint(-100, 100) for _ in range(500)]
    mem_usage_dc = memory_usage((max_subarray_divide_conquer, (arr_sample, 0, len(arr_sample)-1)))
    print(f"Memory used by D&C on size 500: {max(mem_usage_dc) - min(mem_usage_dc):.4f} MB")
    
    run_experiment()
    print("Task 1 complete! Plot saved to images/task1_plot.png")
