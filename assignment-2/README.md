# ADA Lab Experiment 2: Algorithm Strategies Mini-Project

This repository contains implementations for Lab Experiment 2, covering five major algorithmic paradigms across standard optimization and computational problems. The implementation focuses strictly on standard Python environments, visualizing theoretical complexities via empirical runtime data.

## 1. Problem Context

In real-world systems, decision-making and optimization problems arise across domains such as logistics, finance, healthcare, e-commerce, and network design. Different algorithmic strategies are suited for different types of problems:
- **Divide and Conquer**: Large-scale data processing and sorting.
- **Greedy Algorithms**: Fast approximations focusing on local optimums, useful in basic scheduling and resource allocation.
- **Dynamic Programming**: Ideal for problems overlapping subproblems natively and needing a guaranteed optimal solution.
- **Brute Force (Exponential)**: Complete domain path searches emphasizing limits of unstructured logic (e.g., standard baseline TSP).

## 2. Setup and Prerequisites
- **Python**: $\ge$ 3.10
- **Libraries Required**:
  ```bash
  pip install matplotlib numpy memory_profiler
  ```
- **Execution**: The project uses standard `.py` files without notebooks. All charts are output into the `images/` folder.

## 3. Project Structure and Usage

### Task 1: Divide and Conquer (`task1_divide_conquer.py`)
- Problem: Maximum Subarray Problem.
- Output: `images/task1_plot.png`. Evaluates $O(n \log n)$ D&C performance against $O(n^2)$ Brute Force.
- Usage: `python task1_divide_conquer.py`

### Task 2: Sorting Performance (`task2_sorting.py`)
- Problem: Sorting Algorithm comparisons.
- Output: `images/task2_sorting_plot.png`. Evaluates Bubble Sort ($O(n^2)$) vs Merge Sort ($O(n \log n)$) vs Quick Sort ($O(n \log n)$).
- Usage: `python task2_sorting.py`

### Task 3: Greedy Algorithms (`task3_greedy.py`)
- Problem: Fractional Knapsack Problem.
- Output: Console logs showing sorted values by utility-ratio density.
- Usage: `python task3_greedy.py`

### Task 4: Dynamic Programming (`task4_dynamic_programming.py`)
- Problem: 0/1 Knapsack Problem.
- Output: Tabular DP console output and `images/task4_dp_plot.png` comparing polynomial dynamic memory approach versus native $O(2^n)$ recursion.
- Usage: `python task4_dynamic_programming.py`

### Task 5: Travelling Salesman Problem (`task5_tsp.py`)
- Problem: Travelling Salesman Problem (TSP)
- Output: `images/task5_tsp_plot.png`. Evaluates factorial scale calculations mapping out the NP-hard $O(n!)$ constraints explicitly.
- Usage: `python task5_tsp.py`

## 4. Reflection and Observations

### Trade-off Analysis
- **0/1 Knapsack (DP vs Recursion)**: The dynamic programming approach drastically outperforms recursion as $N$ grows due to state memoization, bypassing exponential overlapping re-evaluations. However, it requires $O(nW)$ space, representing a classic Memory-Time Trade-off.
- **Sorting (Merge vs Quick)**: While both operate at $O(n \log n)$, Quick Sort proves slightly faster practically owing to optimized cache hits and less overhead from intermediate array instantiations present in Merge Sort.

### Exponential Stalling
- **TSP Performance (Brute Force)**: As clearly charted in Task 5, surpassing merely $N=10$ invokes severe slowdowns. NP-hard scenarios mathematically mandate heuristic or approximation approaches (such as Genetic Algorithms or Christofides) for scaled, real-world deployment.

## References
Cormen, Leiserson, Rivest, Stein - *Introduction to Algorithms (3rd/4th Edition)*
