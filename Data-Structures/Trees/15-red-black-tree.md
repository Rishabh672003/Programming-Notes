# Red-Black Tree

A **Red-Black Tree** is a self-balancing binary search tree (BST) that maintains approximately balanced structure
through node coloring and rotation operations. It offers efficient worst-case performance for search, insert, and delete
operations while being more insertion/deletion-friendly than AVL trees.

---

## Key Concepts

### Purpose
- Maintain BST property with automatic rebalancing
- Guarantee O(log n) time for search, insert, and delete
- More efficient insertions/deletions than AVL trees
- Widely used in system libraries (Java's TreeMap, C++'s std::map)

### Properties
Every Red-Black Tree satisfies:
1. **Node Color**: Each node is either **red** or **black**
2. **Root Property**: The root is always **black**
3. **Leaf Property**: All leaves (NIL nodes) are **black**
4. **Red Property**: No two adjacent red nodes (red node cannot have red parent/child)
5. **Black Height**: Every path from node to descendant leaf contains same number of black nodes

---

## Node Structure

```python
class RBNode:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color  # 'RED' or 'BLACK'
        self.left = None    # Left child (NIL for leaves)
        self.right = None   # Right child
        self.parent = None  # Parent reference
```

---

## Rotations

Rotations maintain BST properties while fixing color violations:

### 1. Left Rotation
```
    x                                y
   / \                             /   \
  a   y     Left Rotate(x)        x     c
      / \   --------------->     / \
     b   c                      a   b
```

### 2. Right Rotation
```
      y                            x
     / \                         /   \
    x   c   Right Rotate(y)     a     y
   / \      -------------->         / \
  a   b                           b   c
```

---

## Operations

### 1. Insertion
1. Perform standard BST insertion
2. Color new node **RED**
3. Fix violations with:
   - Recolorings
   - Rotations (based on uncle's color)

**Fixup Cases**:
- **Case 1**: Uncle is RED -> Recolor
- **Case 2**: Uncle is BLACK (triangle) -> Rotate
- **Case 3**: Uncle is BLACK (line) -> Rotate & recolor

### 2. Deletion
1. Perform standard BST deletion
2. Fix "double black" violations:
   - Sibling is RED -> Rotate & recolor
   - Sibling is BLACK with BLACK children -> Recolor
   - Sibling is BLACK with RED child -> Rotate & recolor

### 3. Search
- Standard BST search: O(log n)

---

## Python Implementation

```python
RED = 'RED'
BLACK = 'BLACK'
NIL = None  # Sentinel for leaf nodes

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, BLACK)  # Sentinel leaf node
        self.root = self.NIL
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
    
    def insert(self, key):
        node = RBNode(key)
        node.parent = None
        node.left = self.NIL
        node.right = self.NIL
        node.color = RED
        
        # BST insertion
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        
        # Fix violations
        self._insert_fixup(node)
    
    def _insert_fixup(self, node):
        while node != self.root and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:  # Case 1: Uncle is RED
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # Case 2: Triangle
                        node = node.parent
                        self.left_rotate(node)
                    # Case 3: Line
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:  # Symmetric cases
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
        self.root.color = BLACK
    
    def delete(self, key):
        node = self.search(key)
        if node == self.NIL:
            return
        
        # Find replacement node
        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        
        if y_original_color == BLACK:
            self._delete_fixup(x)
    
    def _delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == RED:  # Case 1: Sibling red
                    s.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == BLACK and s.right.color == BLACK:  # Case 2
                    s.color = RED
                    x = x.parent
                else:
                    if s.right.color == BLACK:  # Case 3
                        s.left.color = BLACK
                        s.color = RED
                        self.right_rotate(s)
                        s = x.parent.right
                    # Case 4
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:  # Symmetric cases
                s = x.parent.left
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == BLACK and s.left.color == BLACK:
                    s.color = RED
                    x = x.parent
                else:
                    if s.left.color == BLACK:
                        s.right.color = BLACK
                        s.color = RED
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK
    
    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
    def search(self, key):
        node = self.root
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node
    
    # Utility function for inorder traversal
    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(f"{node.key}({node.color[0]})", end=" ")
            self.inorder(node.right)
```

---

## Time Complexities

| Operation | Time Complexity |
|-----------|-----------------|
| **Search** | O(log n)        |
| **Insert** | O(log n)        |
| **Delete** | O(log n)        |
| **Rotations** | O(1) per operation |
| **Space** | O(n)            |

---

## Advantages vs. Disadvantages

**Advantages**:
- Guaranteed O(log n) for all operations
- Fewer rotations than AVL trees during insertions/deletions
- Efficient for frequently modified datasets
- Widely used in system libraries

**Disadvantages**:
- More complex implementation than basic BST
- Slightly less balanced than AVL trees
- Requires storing color information per node
- Higher constant factors than simpler data structures

---

## Comparison with AVL Trees

| Factor          | AVL Tree                     | Red-Black Tree               |
|-----------------|------------------------------|------------------------------|
| **Balance**     | Strict (height-balanced)     | Approximate (color-balanced) |
| **Search**      | Faster (more strictly balanced)| Slightly slower             |
| **Insert/Delete**| Slower (more rotations)      | Faster (fewer rotations)     |
| **Rebalancing** | Immediate after operation    | May propagate up tree        |
| **Storage**     | Height/balance factor        | Color bit                    |
| **Use Cases**   | Search-intensive             | Mixed operations             |

---

## Use Cases

1. **System Libraries**: Java's TreeMap, C++'s std::map
2. **Database Indexing**: Efficient range queries
3. **Process Schedulers**: Linux kernel's Completely Fair Scheduler
4. **Kernel Data Structures**: File systems, memory management
5. **Network Algorithms**: Router tables
6. **Geometric Algorithms**: Range trees
7. **Blockchain**: Merkle tree implementations

---


```python
# Example usage
rbt = RedBlackTree()
keys = [7, 3, 18, 10, 22, 8, 11, 26]
for key in keys:
    rbt.insert(key)

print("Inorder traversal:")
rbt.inorder(rbt.root)  # 3(B) 7(R) 8(R) 10(B) 11(R) 18(B) 22(R) 26(R)

rbt.delete(18)
print("\nAfter deleting 18:")
rbt.inorder(rbt.root)  # 3(B) 7(R) 8(R) 10(B) 11(R) 22(B) 26(R)

print("\nSearch 11:", rbt.search(11) != rbt.NIL)  # True
```

---

## Visualizing Red-Black Properties

**Valid Red-Black Tree**:
```
         10(B)
        /    \
      7(R)    18(R)
     /  \     /   \
    3(B)8(B)11(B)22(B)
               \
               26(R)
```

**Violations Fixed During Insertion**:
- Case 1: Recoloring when uncle is red
- Case 2: Rotation for triangle configuration
- Case 3: Rotation for line configuration
