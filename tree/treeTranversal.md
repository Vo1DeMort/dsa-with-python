
# 🌳 Tree Traversal Algorithms

## 📊 Comparison Table

| Traversal     | Order                | Data Structure | Use Case                            |
|---------------|----------------------|----------------|-------------------------------------|
| In-Order      | Left → Root → Right  | Recursion/Stack| Sorted output (for BSTs)            |
| Pre-Order     | Root → Left → Right  | Recursion/Stack| Tree serialization, copying         |
| Post-Order    | Left → Right → Root  | Recursion/Stack| Tree deletion, expression evaluation|
| Level-Order   | Level-by-Level       | Queue          | Shortest path, BFS-like tasks       |

## ✅ Notes
- **In-Order**: Produces sorted output for Binary Search Trees.
- **Pre-Order**: Useful for saving the structure of the tree (e.g. serialization).
- **Post-Order**: Ideal when you need to delete or evaluate a tree structure.
- **Level-Order**: Implemented using a queue, not recursion. Good for BFS-like logic.


