# Lab Experiment 2 – Task Statements

## 2.1 Real World Problem Context

In real-world systems, decision-making and optimization problems arise across domains such as logistics, finance, healthcare, e-commerce, and network design. For example, delivery companies must determine optimal routes to minimize travel time, online platforms must efficiently sort large datasets, businesses must allocate limited resources to maximize profit, and scheduling systems must assign tasks in a way that minimizes overall cost or delay.

Different algorithmic strategies are suited to different types of problems:
- **Divide and Conquer** techniques are used in large-scale data processing and sorting systems.
- **Greedy algorithms** are widely applied in scheduling, network routing, and resource allocation where locally optimal choices can lead to efficient solutions.
- **Dynamic Programming** is essential in problems involving overlapping subproblems and optimal substructure, such as inventory management, sequence alignment, and shortest path computations.
- However, certain problems like the **Travelling Salesman Problem** demonstrate exponential growth in complexity, highlighting the limitations of exact solutions for large inputs.

This experiment enables students to implement these algorithmic paradigms, compare their efficiency and scalability, and understand how theoretical complexity translates into practical performance in real-world problem-solving scenarios.

---

## 2.2 Learning Objectives

By completing this project, you will:
1. Implement core algorithms based on Divide and Conquer, Greedy, and Dynamic Programming paradigms using a programming language.
2. Analyze and compare algorithm performance by measuring execution time and observing scalability with increasing input sizes.
3. Apply greedy and dynamic programming techniques to solve optimization problems such as knapsack, scheduling, and shortest-path–style problems.
4. Identify appropriate algorithmic strategies for different problem types based on efficiency, optimality, and problem structure.
5. Develop well-structured and documented programs that demonstrate correct logic, modular design, and good coding practices.

---

## 2.3 Prerequisites

### Theoretical
- Unit 1 & Unit 2 from ADA syllabus.

### Technical Skills
- Python programming (loops, functions, recursion)
- Git & GitHub (commits, repo structure)

### Environment Checklist
- Python ≥ 3.10 with venv
- Git ≥ 2.40
- Libraries: `matplotlib`, `numpy`, `memory_profiler`, `time`

---

## Task 1: Divide and Conquer Algorithms

**Suggested Time:** 1 hour

### Problem Statement
Implement the **Maximum Subarray Problem** using two approaches:
1. **Brute Force** – Check all possible subarrays and find the one with the maximum sum. Time complexity: O(n²).
2. **Divide and Conquer** – Recursively split the array, find the max subarray in the left half, right half, and crossing the midpoint. Time complexity: O(n log n).

### Deliverables
- Timing results comparing both approaches across increasing input sizes.
- Performance plot saved to `images/task1_plot.png`.
- Memory profiling output printed to console.

### Complexity Analysis
| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Divide & Conquer | O(n log n) | O(log n) (recursion stack) |

---

## Task 2: Sorting Performance Comparison

**Suggested Time:** 1 hour

### Problem Statement
Implement and compare the performance of three sorting algorithms:
1. **Bubble Sort** – Simple comparison-based sort. Time complexity: O(n²).
2. **Merge Sort** – Divide and conquer sort. Time complexity: O(n log n).
3. **Quick Sort** – Partition-based divide and conquer sort. Time complexity: O(n log n) average.

Run each algorithm on the same random arrays of increasing sizes and measure execution time.

### Deliverables
- Comparison plot saved to `images/task2_sorting_plot.png`.
- Observations on the quadratic vs linearithmic growth printed in console comments.

### Complexity Analysis
| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

---

## Task 3: Greedy Algorithms

**Suggested Time:** 1.5 hours

### Problem Statement
Implement the **Fractional Knapsack Problem** using a Greedy strategy:
- Given a set of items, each with a value and weight, and a knapsack with a maximum capacity.
- Items can be broken into fractions.
- Sort items by their value-to-weight ratio in descending order.
- Greedily pick items (or fractions of items) until the knapsack is full.

### Deliverables
- Console output showing available items, their ratios, selected items (with fractions), and the optimal total value.

### Complexity Analysis
| Step | Complexity |
|---|---|
| Sorting by ratio | O(n log n) |
| Greedy selection | O(n) |
| **Total** | **O(n log n)** |

---

## Task 4: Dynamic Programming Fundamentals

**Suggested Time:** 1.5 hours

### Problem Statement
Implement the **0/1 Knapsack Problem** using two approaches:
1. **Recursive (Brute Force)** – Explore all subsets. Time complexity: O(2ⁿ).
2. **Dynamic Programming (Bottom-Up)** – Build a DP table to avoid recomputation. Time complexity: O(nW) where W is capacity.

### Deliverables
- DP table printed to console for a small example.
- Execution time comparison plot saved to `images/task4_dp_plot.png` (log scale).
- Observations on exponential vs polynomial growth.

### Complexity Analysis
| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Recursive | O(2ⁿ) | O(n) (recursion stack) |
| DP (Bottom-Up) | O(nW) | O(nW) |

---

## Task 5: Travelling Salesman Problem (TSP)

**Suggested Time:** 1 hour

### Problem Statement
Implement the **Travelling Salesman Problem** using **Brute Force**:
- Given N cities with random (x, y) coordinates, find the shortest route that visits all cities exactly once and returns to the starting city.
- Generate all N! permutations and compute the total distance for each.
- Measure execution time for N = 3, 4, 5, ..., 10 to demonstrate factorial growth.

### Deliverables
- TSP implementation with timing output per city count.
- Plot showing exponential O(n!) growth saved to `images/task5_tsp_plot.png`.
- Observations on why brute force becomes impractical for large N.

### Complexity Analysis
| Metric | Value |
|---|---|
| Time Complexity | O(n!) |
| Space Complexity | O(n²) (distance matrix) |
| 10 cities → permutations | 3,628,800 |
| 15 cities → permutations | 1,307,674,368,000 |

---

## 2.6 Reflection & Discussion

### Trade-off Analysis
- **Which problem benefited most from its chosen strategy and why?**
  The 0/1 Knapsack problem benefits most dramatically from Dynamic Programming. The recursive solution has O(2ⁿ) complexity, making it impractical beyond ~25 items. DP reduces this to O(nW) by storing intermediate results, trading space for massive time savings.

### Real-world Suitability
- Greedy algorithms excel when local optimality leads to global optimality (e.g., Fractional Knapsack, Huffman Coding).
- DP is essential when problems have overlapping subproblems (e.g., shortest paths, sequence alignment).
- Divide and Conquer is ideal for parallelizable problems (e.g., merge sort across distributed systems).

### Recursion Depth
- Deep recursion in algorithms like Quick Sort and the recursive Knapsack can hit Python's default recursion limit (~1000). Using `sys.setrecursionlimit()` or iterative/DP alternatives is necessary for large inputs.

---

## 2.7 Assessment Criteria – 10 Marks

| Criteria | Marks | Description |
|---|---|---|
| 1. Correct Implementation | 3 | All algorithms correctly implemented |
| 2. Performance Measurement | 2 | Proper timing and scalability tests |
| 3. Graphs & Visualization | 2 | Clear, labeled, meaningful plots |
| 4. Algorithm Comparison & Observations | 2 | Logical insights and conclusions |
| 5. Code Quality & Documentation | 1 | Clean, modular, commented code |

---

## References
- Cormen, Leiserson, Rivest, Stein – *Introduction to Algorithms (3rd/4th Edition)*
