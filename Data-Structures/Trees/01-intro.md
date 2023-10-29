## Tress - A hierarchical Data Structure

Trees are hierarchical data structures consisting of nodes.

A tree consists of root node, parent nodes, children nodes, leaf-nodes, sub-tree and ancestors.

```
          1   <-- root node
        /   \
       2     3 <-- Child node
      / \   / \
     4   5 6   7
        /     / \
       8     9  10 <-- Leaf node
```

---

### Binary Search Tree

A Binary tree is a type of tree where each parent node consists of at **max 2** child nodes.

**Types of Binary tree :**

1. **Fully Binary tree :** Every node will either have 0 or 2 children nodes.

2. **Complete Binary Tree :** All levels of tree should be completely filled. If not completely filled, then the last level should have all nodes as left as possible.

3. **Perfect Binary Tree :** All leaf nodes are at same level.

4. **Blnced Binary Tree :** The tree can at max have a height of **Log<sub>2</sub>(n)**, where n is number of nodes.

5. **Degenerate Tree :** When every node only have a single child or parent node. This type resembles to a Linked List.
