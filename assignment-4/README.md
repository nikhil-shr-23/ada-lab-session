# Crew Scheduling Mini-Project

## Problem Context

Many real-world decision-making problems involve exploring multiple possible combinations under strict constraints, where the goal is to find an optimal or feasible solution efficiently. Examples include airline crew scheduling, where constraints like non-overlapping assignments and rest periods apply. String matching is equally relevant for information retrieval. This project explores combinations with Backtracking and Pruning (Branch & Bound) and exact string matching via Naive and Knuth-Morris-Pratt (KMP) algorithms.

## Setup Instructions

1. Clone the repository and navigate into the `crew-scheduling-mini-project-nikhil` directory.
2. Initialize virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the project:
   ```bash
   python main.py
   ```
   This will execute the Backtracking and Branch & Bound assignments, profile both memory and time dimensions, and generate plots inside the `images/` directory.

## File Structure

- `scheduling.py`: Implements `backtracking_scheduling` and `branch_and_bound_scheduling`.
- `string_matching.py`: Implements `naive_string_matching` and `kmp_string_matching`.
- `main.py`: Runner that generates plots and executes constraints.
- `requirements.txt`: Python package requirements.
- `images/`: Stores `.png` charts of empirical complexity profiling.
- `README.md`: Project logic and reflections.

## Reflection & Discussion

- **Complexity Awareness**: Backtracking fails to scale beyond ~10-15 flights because the search space grows exponentially. For $n$ flights and $k$ crew members, the worst-case time complexity is $\mathcal{O}(k^n)$. Branch & bound prunes some space but remains constrained by exponential worst cases.
- **Constraint Handling**: In algorithms, enforcing the overlap was simpler than enforcing rest-time correctly since rest time is a variable function offset. However, with consistent bounds and sorted inputs, verifying $start_time \ge assigned\_end + rest\_time$ was programmatic.
- **Heuristics & Optimization**: To further optimize this scheduling, applying dynamic programming (for some sub-problems), Constraint Programming (CP-SAT), Mixed Integer Linear Programming (MILP), or heuristic methods like Genetic Algorithms could scale up.
- **Visualization Usefulness**: Tracking execution time relative to input constraints clearly exhibited exponential curves, corroborating theoretical limits. The string matching plot highlighted that KMP maintains a much flatter (linear) comparison profile against escalating lengths compared to the naive bounding logic.
- **Extendability**: Adding realistic constraint types—financial crew base costs, seniority requirements, destination-to-origin relocation routing, and specific flight qualifications—would model modern commercial airline realities more robustly.

## NP Architecture and Algorithmic Complexities

The NP-hard nature ensures that constraint satisfaction (CSP) problems like these are typically bounded by heuristic decisions when scale extends beyond trivial sizes.
