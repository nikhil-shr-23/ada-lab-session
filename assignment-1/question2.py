import time
import random
import matplotlib.pyplot as plt
from memory_profiler import memory_usage


def linear_search(a, k):
    for x in a:
        if x == k:
            return True
    return False

def binary_search(a, k):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == k:
            return True
        elif a[m] < k:
            l = m + 1
        else:
            r = m - 1
    return False


# Wrapper functions for memory profiling
def linear_wrap(a, k): linear_search(a, k)
def binary_wrap(a, k): binary_search(a, k)


sizes = [100, 500, 1000, 5000]

# Time lists
lb, la, lw = [], [], []
bb, ba, bw = [], [], []

# Memory lists
mlb, mla, mlw = [], [], []
mbb, mba, mbw = [], [], []


for n in sizes:
    a = sorted(random.sample(range(n * 10), n))

    best = a[0]       # first element — best case
    avg = a[n // 2]   # middle element — average case
    worst = -1         # element not in array — worst case

    # --- Linear Search ---
    s = time.perf_counter()
    linear_search(a, best)
    lb.append(time.perf_counter() - s)
    mem = memory_usage((linear_wrap, (a, best)), max_usage=True)
    mlb.append(mem if isinstance(mem, (int, float)) else max(mem) - min(mem))

    s = time.perf_counter()
    linear_search(a, avg)
    la.append(time.perf_counter() - s)
    mem = memory_usage((linear_wrap, (a, avg)), max_usage=True)
    mla.append(mem if isinstance(mem, (int, float)) else max(mem) - min(mem))

    s = time.perf_counter()
    linear_search(a, worst)
    lw.append(time.perf_counter() - s)
    mem = memory_usage((linear_wrap, (a, worst)), max_usage=True)
    mlw.append(mem if isinstance(mem, (int, float)) else max(mem) - min(mem))

    # --- Binary Search ---
    s = time.perf_counter()
    binary_search(a, best)
    bb.append(time.perf_counter() - s)
    mem = memory_usage((binary_wrap, (a, best)), max_usage=True)
    mbb.append(mem if isinstance(mem, (int, float)) else max(mem) - min(mem))

    s = time.perf_counter()
    binary_search(a, avg)
    ba.append(time.perf_counter() - s)
    mem = memory_usage((binary_wrap, (a, avg)), max_usage=True)
    mba.append(mem if isinstance(mem, (int, float)) else max(mem) - min(mem))

    s = time.perf_counter()
    binary_search(a, worst)
    bw.append(time.perf_counter() - s)
    mem = memory_usage((binary_wrap, (a, worst)), max_usage=True)
    mbw.append(mem if isinstance(mem, (int, float)) else max(mem) - min(mem))


# --- Linear Search Time Plot ---
plt.figure()
plt.plot(sizes, lb, marker='o', label='Best')
plt.plot(sizes, la, marker='o', label='Average')
plt.plot(sizes, lw, marker='o', label='Worst')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Linear Search – Time Complexity")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question2-linear-time.png", dpi=150)
plt.show()

# --- Binary Search Time Plot ---
plt.figure()
plt.plot(sizes, bb, marker='o', label='Best')
plt.plot(sizes, ba, marker='o', label='Average')
plt.plot(sizes, bw, marker='o', label='Worst')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Binary Search – Time Complexity")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question2-binary-time.png", dpi=150)
plt.show()

# --- Linear Search Space Plot ---
plt.figure()
plt.plot(sizes, mlb, marker='o', label='Best')
plt.plot(sizes, mla, marker='o', label='Average')
plt.plot(sizes, mlw, marker='o', label='Worst')
plt.xlabel("Input Size")
plt.ylabel("Memory Used (MiB)")
plt.title("Linear Search – Space Complexity")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question2-linear-space.png", dpi=150)
plt.show()

# --- Binary Search Space Plot ---
plt.figure()
plt.plot(sizes, mbb, marker='o', label='Best')
plt.plot(sizes, mba, marker='o', label='Average')
plt.plot(sizes, mbw, marker='o', label='Worst')
plt.xlabel("Input Size")
plt.ylabel("Memory Used (MiB)")
plt.title("Binary Search – Space Complexity")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question2-binary-space.png", dpi=150)
plt.show()
