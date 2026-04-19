# Assignment 3 - Graph Algorithms (Problem Statements)

## Context
Many real-world systems such as road networks, computer networks, social media platforms, and project scheduling systems can be modeled using graphs, where nodes represent entities and edges represent relationships.

Graph algorithms like BFS and DFS help explore connectivity, topological sorting assists in managing task dependencies, shortest path algorithms support navigation and routing, and minimum spanning tree algorithms are used to design cost-efficient networks.

This assignment focuses on implementing these algorithms and understanding how graph theory solves practical problems efficiently.

## Learning Objectives
1. Represent graphs using adjacency matrix and adjacency list based on problem requirements.
2. Implement and apply graph traversal algorithms such as Breadth First Search (BFS) and Depth First Search (DFS).
3. Use graph algorithms to solve ordering and dependency problems, including topological sorting.
4. Compute shortest paths and minimum spanning trees using standard graph algorithms.
5. Develop correct and well-structured programs that demonstrate practical understanding of graph-based problem solving.

## Prerequisites
- Theoretical:
  - Topics from Units 1, 2 and 3 of ADA (Graph traversal, shortest path, spanning tree)
- Technical Skills:
  - Python (data structures, functions, recursion, loops)
  - Git basics (commit, push, branching)
- Environment Checklist:
  - Python >= 3.10 with venv
  - Git >= 2.40
  - Libraries: matplotlib, memory_profiler, jupyterlab, time
  - (Optional) networkx for graph representation

## Experiment Tasks and Deliverables
1. **Graph Representation**
   - Deliverable: Graph and matrix representation
2. **Graph Traversal Algorithms**
   - Deliverable: BFS and DFS implementations
3. **Topological Sorting**
   - Deliverable: Topological sort implementation
4. **Shortest Path Algorithms**
   - Deliverable:
     - Represent graph using adjacency list/matrix as appropriate
     - Display shortest path distances
     - Compare time complexity behavior for small graphs
5. **Minimum Spanning Tree Algorithms**
   - Deliverable: MST implementations

## Core Implementation Problems
Implement the following 4 real-world inspired graph problems:
1. BFS/DFS for friend suggestion or connectivity exploration.
2. Bellman-Ford for negative edge route finding.
3. Dijkstra for emergency shortest path.
4. Prim/Kruskal for minimum spanning tree (cabling/network design).

## Step-by-Step Procedure
1. **Repo Setup**
   - Create private GitHub repo: `graph-algo-mini-project-<yourname>`
   - Add files/folders: `README.md`, `.gitignore`, `notebooks/`, `images/`, `docs/`, `requirements.txt`
2. **Environment Initialization**
   - Create virtual environment: `python -m venv .venv`
   - Install packages: `pip install matplotlib memory_profiler jupyterlab`
   - Launch JupyterLab and test basic graph imports
3. **Graph Problem Implementation**
   - Implement all 4 problems with input, algorithm, output, and complexity analysis
4. **Profiling and Visualization**
   - Use `memory_profiler` and `time` to capture performance
   - Optional: plot time vs number of nodes/edges
   - Add observations and insights
5. **Documentation and Finalization**
   - Add comparison table and reflections
   - Finalize `README.md` with setup, usage, references
   - Commit and tag final version: `v1.0-submission`
6. **Submission**
   - Upload repo link to LMS portal

## Reflection and Discussion Prompts
1. Which real-life problem benefited most from its algorithm and why?
2. How do BFS/DFS perform on sparse vs dense networks? What about Bellman-Ford for large graphs?
3. In MST, how might Kruskal vs Prim affect final cabling cost or complexity?
4. What challenges arise with negative weight cycles in route planning, and how are they handled?
5. Suggest one additional real-world graph problem and the best suited algorithm.

## Assessment Criteria (10 Marks)
1. Correct Graph Representation - 2 marks
2. Traversal and Topological Sorting - 2 marks
3. Shortest Path Algorithms - 2.5 marks
4. Minimum Spanning Tree Algorithms - 2 marks
5. Code Quality and Documentation - 1.5 marks

## Submission Checklist
- Push all work to a private GitHub repo named `graph-algo-mini-project-<yourname>`
- Ensure repository includes:
  - `README.md` (objective, setup, problem summary, references)
  - `graph_realworld.ipynb` (if notebook format is used)
  - `requirements.txt` (packages)
  - `.gitignore` (exclude environment files)
  - `images/` (optional plots)
- Tag final commit as `v1.0-submission`
- Submit GitHub repository URL via LMS
