import time
import pandas as pd
import matplotlib.pyplot as plt
from memory_profiler import memory_usage

# --- Factorial (Recursive) ---
fact_calls = 0
def factorial(n):
    global fact_calls
    fact_calls += 1
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# --- Fibonacci (Naive Recursive) ---
fib_calls = 0
def fib_naive(n):
    global fib_calls
    fib_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# --- Fibonacci (DP / Memoization) ---
fib_dp_calls = 0
def fib_dp(n, memo):
    global fib_dp_calls
    fib_dp_calls += 1
    if n in memo:
        return memo[n]
    memo[n] = fib_dp(n - 1, memo) + fib_dp(n - 2, memo)
    return memo[n]


# Wrapper functions for memory profiling
def fact_wrap(n): factorial(n)
def fib_wrap(n): fib_naive(n)
def fib_dp_wrap(n): fib_dp(n, {0: 0, 1: 1})


inputs = [5, 10, 15, 20]
result = []

fact_t, fib_t, fibdp_t = [], [], []
fact_m, fib_m, fibdp_m = [], [], []

for n in inputs:
    # Factorial
    fact_calls = 0
    s = time.perf_counter()
    factorial(n)
    fact_time = time.perf_counter() - s
    fact_calls_n = fact_calls  # save before wrapper resets it

    mem = memory_usage((fact_wrap, (n,)), max_usage=True)
    fact_mem = mem if isinstance(mem, (int, float)) else max(mem) - min(mem)

    # Fibonacci Naive
    fib_calls = 0
    s = time.perf_counter()
    fib_naive(n)
    fib_time = time.perf_counter() - s
    fib_calls_n = fib_calls

    mem = memory_usage((fib_wrap, (n,)), max_usage=True)
    fib_mem = mem if isinstance(mem, (int, float)) else max(mem) - min(mem)

    # Fibonacci DP
    fib_dp_calls = 0
    s = time.perf_counter()
    fib_dp(n, {0: 0, 1: 1})
    fib_dp_time = time.perf_counter() - s
    fib_dp_calls_n = fib_dp_calls

    mem = memory_usage((fib_dp_wrap, (n,)), max_usage=True)
    fib_dp_mem = mem if isinstance(mem, (int, float)) else max(mem) - min(mem)

    fact_t.append(fact_time)
    fib_t.append(fib_time)
    fibdp_t.append(fib_dp_time)

    fact_m.append(fact_mem)
    fib_m.append(fib_mem)
    fibdp_m.append(fib_dp_mem)

    result.append([
        n,
        fact_time, fact_calls_n,
        fib_time, fib_calls_n,
        fib_dp_time, fib_dp_calls_n
    ])

df = pd.DataFrame(
    result,
    columns=[
        "n",
        "Factorial Time", "Factorial Calls",
        "Fibonacci Naive Time", "Fibonacci Naive Calls",
        "Fibonacci DP Time", "Fibonacci DP Calls"
    ]
)

print(df.to_string(index=False))

# --- Time Complexity Plot ---
plt.figure()
plt.plot(inputs, fact_t, marker='o', label='Factorial O(n)')
plt.plot(inputs, fib_t, marker='o', label='Fibonacci Naive O(2^n)')
plt.plot(inputs, fibdp_t, marker='o', label='Fibonacci DP O(n)')
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Time Complexity Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question3-time.png", dpi=150)
plt.show()

# --- Space Complexity Plot ---
plt.figure()
plt.plot(inputs, fact_m, marker='o', label='Factorial O(n)')
plt.plot(inputs, fib_m, marker='o', label='Fibonacci Naive O(n)')
plt.plot(inputs, fibdp_m, marker='o', label='Fibonacci DP O(n)')
plt.xlabel("n")
plt.ylabel("Memory Used (MiB)")
plt.title("Space Complexity using Memory Profiler")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("question3-space.png", dpi=150)
plt.show()
