# Delivery Route Optimization Mini-Project

## Problem Context

E-commerce delivery routing blends spatial logic constraints with capacity and time limits. This project demonstrates mathematical optimization over delivery constraints by building heuristic, recurrence, greedy, DP (Dynamic Programming), and TSP (Traveling Salesman) boundaries. We model constraints mathematically to evaluate empirical intractabilities linked to real-world logistics.

## Setup Instructions

The environment requires `matplotlib`, `memory_profiler`, and `networkx`.

1. Navigate into the repository:
   ```bash
   cd assignment-5
   ```
2. Set up environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Execute the experiments:
   ```bash
   python3 main.py
   ```
   Plots generated are saved to the `/images` folder, detailing scalability, value mapping, and graphical trees.

## File Hierarchy

- `models.py`: Initializes Graph distance arrays, node layouts, and parcel values.
- `recurrence.py`: Base-level unoptimized depth-first recursion finding a loop path cost.
- `greedy_dp.py`: Maps fractional parcel value and validates traversal logic DP arrays against time schedules.
- `graph_algos.py`: Core routing—includes Dijkstra shortest routes, Kruskal's MST algorithm, and Brute-force optimal TSP routing.
- `main.py`: Runner aggregating computations with profiling output.
- `/images`: Contains execution plots for metric verifications.

## Reflection & Discussion

- **Optimization vs Realism**: The optimal topological TSP route is rarely the realistic route. In our test sequence, the minimum topological cost (TSP) route `[0, 1, 3, 4, 2, 0]` failed the sequential Time Window (DP) alignment checks because adhering strictly to topology without accounting for scheduling bounds causes delays that invalidate actual commitments.
- **Algorithm Trade-offs**:
  - **Fastest**: Greedy (knapsack mapping) and Kruskal's MST ran globally the fastest with complexity bounded strictly.
  - **Scalability Issues**: True TSP brute force quickly exploded (measurably scaling $\mathcal{O}(n!)$) in our `profile_scalability` plot limit. Recurrence scaling is similar but with limited parameters.
- **NP-hard Challenge**: The brute-force TSP methodology became strictly infeasible to evaluate swiftly on our simple machine layout past `n = 10` locations due to $\approx 3.6$ million permutations extending execution into macroscopic limits without heuristic pruning or Held-Karp bounds constraints ($\mathcal{O}(n^2 2^n)$).
- **Visualization Insight**: Graph execution via `networkx` mapping makes hierarchical cluster centers obvious (like the structure of MST edges bypassing expensive peripheral node crosses). TSP scalability curves validated our theoretical runtime assumptions, while the greedy profit weight mapping immediately showed fractional superiority logic.
- **Feature Suggestion**: Integrating multiple vehicles (Vehicle Routing Problem -> VRP) natively splits node responsibilities mathematically. Additionally, injecting variables like physical traffic limits, fuel limitations per gradient altitude, and prioritized routing for perishables would emulate enterprise logistics perfectly.
