import os
import time
import random
import matplotlib.pyplot as plt
import sys
from memory_profiler import memory_usage

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(SCRIPT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

sys.setrecursionlimit(2000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def run_experiment():
    input_sizes = [500, 1000, 2000, 3000, 4000]
    time_bubble = []
    time_merge = []
    time_quick = []

    for size in input_sizes:
        # Generate random array
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        # Test Bubble Sort
        arr_copy = arr.copy()
        start_time = time.perf_counter()
        bubble_sort(arr_copy)
        time_bubble.append(time.perf_counter() - start_time)

        # Test Merge Sort
        arr_copy = arr.copy()
        start_time = time.perf_counter()
        merge_sort(arr_copy)
        time_merge.append(time.perf_counter() - start_time)

        # Test Quick Sort
        arr_copy = arr.copy()
        start_time = time.perf_counter()
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
        time_quick.append(time.perf_counter() - start_time)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(input_sizes, time_bubble, label='Bubble Sort O(n^2)', marker='o')
    plt.plot(input_sizes, time_merge, label='Merge Sort O(n log n)', marker='s')
    plt.plot(input_sizes, time_quick, label='Quick Sort O(n log n)', marker='^')

    plt.title('Sorting Algorithm Performance Comparison')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(IMAGES_DIR, 'task2_sorting_plot.png'))
    plt.close()

if __name__ == "__main__":
    print("Running Task 2: Sorting Performance Comparison...")
    run_experiment()
    print("Task 2 complete! Plot saved to images/task2_sorting_plot.png")
