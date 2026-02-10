# Assignment-1 — Complexity Analysis

---

## Question 1: Basic Complexity Functions

Demonstrates four fundamental time complexities.

| Function       | Time Complexity | Space Complexity | Description                                                              |
| -------------- | --------------- | ---------------- | ------------------------------------------------------------------------ |
| `const_fn(a)`  | **O(1)**        | **O(1)**         | Accesses only the first element — constant time regardless of input size |
| `linear_fn(a)` | **O(n)**        | **O(1)**         | Single loop over all `n` elements to compute sum                         |
| `quad_fn(a)`   | **O(n²)**       | **O(1)**         | Nested loop — both iterate over `n` elements → n × n operations          |
| `log_fn(n)`    | **O(log n)**    | **O(1)**         | Halves `n` repeatedly until it reaches 1                                 |

---

## Question 2: Linear Search vs Binary Search

| Algorithm         | Case    | Time Complexity | Space Complexity |
| ----------------- | ------- | --------------- | ---------------- |
| **Linear Search** | Best    | **O(1)**        | **O(1)**         |
|                   | Average | **O(n)**        | **O(1)**         |
|                   | Worst   | **O(n)**        | **O(1)**         |
| **Binary Search** | Best    | **O(1)**        | **O(1)**         |
|                   | Average | **O(log n)**    | **O(1)**         |
|                   | Worst   | **O(log n)**    | **O(1)**         |

### Key Observations

- **Linear Search** scans elements one by one → grows linearly with input size.
- **Binary Search** requires a **sorted** array and halves the search space each step → logarithmic growth.
- Both are **iterative** implementations, so space is constant O(1).

---

## Question 3: Factorial & Fibonacci (Naive vs DP)

| Function       | Time Complexity | Space Complexity             | Recurrence / Notes                          |
| -------------- | --------------- | ---------------------------- | ------------------------------------------- |
| `factorial(n)` | **O(n)**        | **O(n)** (call stack)        | T(n) = T(n-1) + O(1) → linear               |
| `fib_naive(n)` | **O(2ⁿ)**       | **O(n)** (call stack depth)  | T(n) = T(n-1) + T(n-2) → exponential        |
| `fib_dp(n)`    | **O(n)**        | **O(n)** (memo dict + stack) | Each subproblem solved once via memoization |

### Key Observations

- **Naive Fibonacci** has exponential time because it recomputes the same subproblems.
- **DP Fibonacci** stores results in a dictionary → each value computed only once → O(n).
- **Factorial** makes exactly `n` recursive calls → O(n) time, O(n) stack space.

---

## Question 4: Recurrence Relations (Master Theorem)

| Recurrence         | Solved Complexity (Time) | Space Complexity           | Master Theorem Case                                     |
| ------------------ | ------------------------ | -------------------------- | ------------------------------------------------------- |
| T(n) = T(n/2) + n  | **O(n)**                 | **O(log n)** (stack depth) | Case 3: f(n) = n = Ω(n^(log₂1 + ε)) → dominated by f(n) |
| T(n) = 2T(n/2) + n | **O(n log n)**           | **O(log n)** (stack depth) | Case 2: f(n) = n = Θ(n^(log₂2)) → T(n) = Θ(n log n)     |

### Master Theorem Breakdown

**T(n) = T(n/2) + n** → a=1, b=2, f(n)=n

- n^(log_b(a)) = n^0 = 1
- f(n) = n ≫ 1 → **Case 3** → T(n) = Θ(n)

**T(n) = 2T(n/2) + n** → a=2, b=2, f(n)=n

- n^(log_b(a)) = n^1 = n
- f(n) = n = Θ(n) → **Case 2** → T(n) = Θ(n log n)

---

## Summary Table

| Question | Algorithm / Function  | Time       | Space    |
| -------- | --------------------- | ---------- | -------- |
| Q1       | Constant              | O(1)       | O(1)     |
| Q1       | Linear                | O(n)       | O(1)     |
| Q1       | Quadratic             | O(n²)      | O(1)     |
| Q1       | Logarithmic           | O(log n)   | O(1)     |
| Q2       | Linear Search (worst) | O(n)       | O(1)     |
| Q2       | Binary Search (worst) | O(log n)   | O(1)     |
| Q3       | Factorial             | O(n)       | O(n)     |
| Q3       | Fibonacci Naive       | O(2ⁿ)      | O(n)     |
| Q3       | Fibonacci DP          | O(n)       | O(n)     |
| Q4       | T(n)=T(n/2)+n         | O(n)       | O(log n) |
| Q4       | T(n)=2T(n/2)+n        | O(n log n) | O(log n) |
