import time
import pandas as pd
import matplotlib.pyplot as plt
from memory_profiler import memory_usage

# --- Recurrence 1: T(n) = T(n/2) + n ---
c1 = 0
def rec1(n):
    global c1
    c1 += 1
    if n <= 1:
        return 1
    return rec1(n // 2) + n

# --- Recurrence 2: T(n) = 2T(n/2) + n ---
c2 = 0
def rec2(n):
    global c2
    c2 += 1
    if n <= 1:
        return 1
    return rec2(n // 2) + rec2(n // 2) + n


# Wrappers for memory profiling
def rec1_wrap(n): rec1(n)
def rec2_wrap(n): rec2(n)


sizes = [8, 16, 32, 64, 128]
rows = []

t1_list, t2_list = [], []
m1_list, m2_list = [], []

for n in sizes:
    # Recurrence 1
    c1 = 0
    s = time.perf_counter()
    rec1(n)
    t1 = time.perf_counter() - s
    c1_saved = c1  # save before wrapper resets it

    mem = memory_usage((rec1_wrap, (n,)), max_usage=True)
    m1 = mem if isinstance(mem, (int, float)) else max(mem) - min(mem)

    # Recurrence 2
    c2 = 0
    s = time.perf_counter()
    rec2(n)
    t2 = time.perf_counter() - s
    c2_saved = c2

    mem = memory_usage((rec2_wrap, (n,)), max_usage=True)
    m2 = mem if isinstance(mem, (int, float)) else max(mem) - min(mem)

    t1_list.append(t1)
    t2_list.append(t2)
    m1_list.append(m1)
    m2_list.append(m2)

    rows.append([
        n,
        t1, c1_saved,
        t2, c2_saved
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "n",
        "T(n)=T(n/2)+n Time", "Calls",
        "T(n)=2T(n/2)+n Time", "Calls"
    ]
)

print(df.to_string(index=False))

# --- Time Complexity Plot ---
plt.figure()
plt.plot(sizes, t1_list, marker='o', label='T(n)=T(n/2)+n  →  O(n)')
plt.plot(sizes, t2_list, marker='o', label='T(n)=2T(n/2)+n  →  O(n log n)')
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Time Complexity – Recurrence Relations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question4-time.png", dpi=150)
plt.show()

# --- Space Complexity Plot ---
plt.figure()
plt.plot(sizes, m1_list, marker='o', label='T(n)=T(n/2)+n  →  O(log n)')
plt.plot(sizes, m2_list, marker='o', label='T(n)=2T(n/2)+n  →  O(n)')
plt.xlabel("n")
plt.ylabel("Memory Used (MiB)")
plt.title("Space Complexity using Memory Profiler")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question4-space.png", dpi=150)
plt.show()
