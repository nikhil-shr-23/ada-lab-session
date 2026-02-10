import time
import matplotlib.pyplot as plt
from memory_profiler import memory_usage




# O(1)
def const_fn(a):
    return a[0]

# O(n)
def linear_fn(a):
    s = 0
    for x in a:
        s += x
    return s

# O(n^2)
def quad_fn(a):
    c = 0
    for i in a:
        for j in a:
            c += 1
    return c

# O(log n)
def log_fn(n):
    c = 0
    while n > 1:
        n //= 2
        c += 1
    return c



def const_wrap(a): const_fn(a)
def linear_wrap(a): linear_fn(a)
def quad_wrap(a): quad_fn(a)
def log_wrap(n): log_fn(n)



try:
    sizes = input("Enter input sizes eg- 10,100,500,1000: ")
    n = [int(i) for i in sizes.split(",")]
except:
    n = [10, 100, 500, 1000]


t1, t2, t3, t4 = [], [], [], []
m1, m2, m3, m4 = [], [], [], []


for x in n:
    a = list(range(x))

    # -O(1)
    start = time.perf_counter()
    const_fn(a)
    t1.append(time.perf_counter() - start)

    mem = memory_usage((const_wrap, (a,)))
    m1.append(max(mem) - min(mem))

    # - O(n)
    start = time.perf_counter()
    linear_fn(a)
    t2.append(time.perf_counter() - start)

    mem = memory_usage((linear_wrap, (a,)))
    m2.append(max(mem) - min(mem))

    # - O(n^2)
    start = time.perf_counter()
    quad_fn(a)
    t3.append(time.perf_counter() - start)

    mem = memory_usage((quad_wrap, (a,)))
    m3.append(max(mem) - min(mem))

    # - O(log n)
    start = time.perf_counter()
    log_fn(x)
    t4.append(time.perf_counter() - start)

    mem = memory_usage((log_wrap, (x,)))
    m4.append(max(mem) - min(mem))


plt.figure()
plt.plot(n, t1, marker='o', label='O(1)')
plt.plot(n, t2, marker='o', label='O(n)')
plt.plot(n, t3, marker='o', label='O(n²)')
plt.plot(n, t4, marker='o', label='O(log n)')
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Time Complexity Comparison")
plt.legend()
plt.show()



plt.figure()
plt.plot(n, m1, marker='o', label='O(1)')
plt.plot(n, m2, marker='o', label='O(n)')
plt.plot(n, m3, marker='o', label='O(n²)')
plt.plot(n, m4, marker='o', label='O(log n)')
plt.xlabel("Input Size")
plt.ylabel("Memory Used (MiB)")
plt.title("Space Complexity using Memory Profiler")
plt.legend()
plt.show()
