# Data Structures & Algorithms

A personal repository for implementing, studying, and revisiting **data structures and algorithms** in code.

This repository is not intended to contain every data structure or algorithm that exists. Instead, it serves as a growing collection of implementations and examples that I find useful while developing my understanding of computer science.

> **Understand the structure. Understand the algorithm. Then write the code.**

---

## 📂 Repository Structure

The repository is organized by topic so that each concept can be studied independently.

```text
data-structures-and-algorithms/
│
├── data-structures/
│   ├── arrays/
│   ├── linked-lists/
│   ├── stacks/
│   ├── queues/
│   ├── hash-tables/
│   ├── trees/
│   ├── heaps/
│   └── graphs/
│
├── algorithms/
│   ├── searching/
│   ├── sorting/
│   ├── recursion/
│   ├── graph-algorithms/
│   ├── tree-algorithms/
│   └── dynamic-programming/
│
└── README.md
```

The structure may evolve as the repository grows.

---

## 🧠 What This Repository Contains

### Data Structures

Implementations and experiments involving structures such as:

* Arrays
* Linked Lists
* Stacks
* Queues
* Hash Tables
* Trees
* Binary Search Trees
* Heaps
* Graphs
* Tries
* and others

### Algorithms

Implementations covering areas such as:

* Searching
* Sorting
* Recursion
* Tree traversal
* Graph traversal
* Graph algorithms
* Dynamic programming
* Greedy algorithms
* and other fundamental techniques

The goal is **breadth with understanding**, not simply collecting implementations.

---

## 🔍 Learning Approach

Each implementation is written to make the underlying idea understandable rather than treating the code as something to memorize.

For example, a linked list is not just:

```python
node.next = new_node
```

The important question is **why that creates a connection between two objects**.

I use these implementations to understand:

* How data is represented in memory
* How structures are connected
* How algorithms manipulate data
* Why certain approaches are efficient
* Where time and space complexity come from
* What trade-offs different approaches introduce

---

## ⚙️ Complexity

Where appropriate, implementations will include analysis of:

| Complexity     | Meaning           |
| -------------- | ----------------- |
| **O(1)**       | Constant time     |
| **O(log n)**   | Logarithmic time  |
| **O(n)**       | Linear time       |
| **O(n log n)** | Linearithmic time |
| **O(n²)**      | Quadratic time    |
| **O(2ⁿ)**      | Exponential time  |

Both **time complexity** and **space complexity** are considered where they meaningfully apply.

---

## ⏱️ Complexity Reference

Big-O notation describes how the time or space requirements of an operation grow as the input size `n` increases.

### Data Structures

| Data Structure               |    Access |    Search | Insertion |  Deletion |    Space |
| ---------------------------- | --------: | --------: | --------: | --------: | -------: |
| **Array**                    |      O(1) |      O(n) |      O(n) |      O(n) |     O(n) |
| **Dynamic Array**            |      O(1) |      O(n) |      O(n) |      O(n) |     O(n) |
| **Singly Linked List**       |      O(n) |      O(n) |     O(1)  |     O(1)  |     O(n) |
| **Doubly Linked List**       |      O(n) |      O(n) |     O(1)  |     O(1)  |     O(n) |
| **Stack**                    |     O(n)  |     O(n)  |      O(1) |      O(1) |     O(n) |
| **Queue**                    |     O(n)  |     O(n)  |      O(1) |      O(1) |     O(n) |
| **Hash Table**               |         — |     O(1)  |     O(1)  |     O(1)  |     O(n) |
| **Binary Search Tree**       | O(log n)  | O(log n)  | O(log n)  | O(log n)  |     O(n) |
| **Heap**                     |         — |      O(n) |  O(log n) |  O(log n) |     O(n) |
| **Trie**                     |         — |      O(m) |      O(m) |      O(m) |   O(n·m) |
| **Graph — Adjacency List**   |         — |  O(V + E) |     O(1)  |     O(1)  | O(V + E) |
| **Graph — Adjacency Matrix** |      O(1) |     O(V²) |     O(V²) |     O(V²) |    O(V²) |

* When the position/node is already known. Finding the position first can take O(n).

---

### Searching Algorithms

| Algorithm                      | Best Case | Average Case | Worst Case | Space |
| ------------------------------ | --------: | -----------: | ---------: | ----: |
| **Linear Search**              |      O(1) |         O(n) |       O(n) |  O(1) |
| **Binary Search**              |      O(1) |     O(log n) |   O(log n) | O(1)  |
| **Depth-First Search (DFS)**   |  O(V + E) |     O(V + E) |   O(V + E) |  O(V) |
| **Breadth-First Search (BFS)** |  O(V + E) |     O(V + E) |   O(V + E) |  O(V) |

* Iterative binary search. A recursive implementation typically uses O(log n) call-stack space.

---

### Sorting Algorithms

| Algorithm          |  Best Case | Average Case | Worst Case |     Space |
| ------------------ | ---------: | -----------: | ---------: | --------: |
| **Bubble Sort**    |       O(n) |        O(n²) |      O(n²) |      O(1) |
| **Selection Sort** |      O(n²) |        O(n²) |      O(n²) |      O(1) |
| **Insertion Sort** |       O(n) |        O(n²) |      O(n²) |      O(1) |
| **Merge Sort**     | O(n log n) |   O(n log n) | O(n log n) |      O(n) |
| **Quick Sort**     | O(n log n) |   O(n log n) |      O(n²) | O(log n)  |
| **Heap Sort**      | O(n log n) |   O(n log n) | O(n log n) |      O(1) |
| **Counting Sort**  |   O(n + k) |     O(n + k) |   O(n + k) |  O(n + k) |
| **Radix Sort**     |      O(nk) |        O(nk) |      O(nk) |  O(n + k) |

* Average recursion-stack space with a good pivot strategy; worst-case recursion depth can reach O(n).

---

### Graph Algorithms

| Algorithm                |   Time Complexity | Space Complexity |
| ------------------------ | ----------------: | ---------------: |
| **DFS**                  |          O(V + E) |             O(V) |
| **BFS**                  |          O(V + E) |             O(V) |
| **Dijkstra's Algorithm** | O((V + E) log V)  |         O(V + E) |
| **Bellman-Ford**         |             O(VE) |             O(V) |
| **Floyd-Warshall**       |             O(V³) |            O(V²) |
| **Kruskal's Algorithm**  |        O(E log E) |         O(V + E) |
| **Prim's Algorithm**     | O((V + E) log V)  |         O(V + E) |
| **Topological Sort**     |          O(V + E) |             O(V) |

* Using a binary heap and adjacency lists.

---

### Tree Algorithms

| Algorithm                 | Time Complexity | Space Complexity |
| ------------------------- | --------------: | ---------------: |
| **Tree Traversal — DFS**  |            O(n) |             O(h) |
| **In-order Traversal**    |            O(n) |             O(h) |
| **Pre-order Traversal**   |            O(n) |             O(h) |
| **Post-order Traversal**  |            O(n) |             O(h) |
| **Level-order Traversal** |            O(n) |             O(n) |
| **BST Search**            |       O(log n)  |             O(h) |
| **BST Insertion**         |       O(log n)  |             O(h) |
| **BST Deletion**          |       O(log n)  |             O(h) |

* For a balanced BST. In the worst case, an unbalanced BST can degrade to O(n).

Where:

* `n` = number of elements
* `V` = number of vertices
* `E` = number of edges
* `h` = height of a tree
* `m` = length of the searched/inserted string
* `k` = range of values or another algorithm-specific parameter

---

### Big-O Growth

From generally more scalable to less scalable:

**O(1)** → **O(log n)** → **O(n)** → **O(n log n)** → **O(n²)** → **O(2ⁿ)**

The purpose of this table is to provide a quick reference alongside the implementations in this repository. Individual implementations may have different complexities depending on the exact algorithm, underlying representation, and assumptions being made.

## 🛠️ Languages

The repository primarily focuses on **Python** for now.

Additional languages may be introduced later when they provide useful insight into how the same structures or algorithms are implemented differently.

---

## 🎯 Purpose

This repository serves three purposes:

**1. Learn**

Understand fundamental data structures and algorithms by implementing them.

**2. Practice**

Turn theoretical concepts into working programs.

**3. Reference**

Maintain a collection of implementations that can be revisited when a concept needs to be refreshed.

---

## 📈 Progress

This is a **living repository**.

New implementations will be added as I encounter, study, and understand new concepts.

It is intentionally incomplete.
---

## 📚 Topics

As the repository develops, the following areas may be expanded:

* [ ] Arrays
* [ ] Linked Lists
* [ ] Stacks
* [ ] Queues
* [ ] Hash Tables
* [ ] Recursion
* [ ] Searching
* [ ] Sorting
* [ ] Trees
* [ ] Heaps
* [ ] Graphs
* [ ] Graph Traversal
* [ ] Dynamic Programming
* [ ] Greedy Algorithms
* [ ] Backtracking
* [ ] Advanced Data Structures
* [ ] Advanced Algorithms

This checklist is intentionally flexible and does not represent a fixed curriculum.

---

## 📝 Notes

The code in this repository is primarily for **learning and reference**.

Implementations may favor clarity over production-level optimization. Some implementations may also evolve as my understanding of the underlying concepts improves.

If an implementation looks unnecessarily complicated, that may be because it is exploring the concept rather than trying to provide the shortest possible solution.
