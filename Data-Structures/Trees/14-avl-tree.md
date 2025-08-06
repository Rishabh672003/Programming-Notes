# AVL Tree

An **AVL tree** (named after inventors Adelson-Velsky and Landis) is a self-balancing binary search tree (BST) that
maintains optimal height for efficient operations. In an AVL tree, the heights of the two child subtrees of any node
differ by at most one. If this balance is disrupted during insertions or deletions, rotations are performed to restore
equilibrium.

---

## Key Concepts

### Purpose

- Maintain BST property while ensuring tree remains balanced
- Guarantee O(log n) time complexity for search, insert, and delete operations
- Automatically rebalance after modifications
- Prevent BST degeneration into linked list in worst-case scenarios

### Balance Factor

- For each node, **balance factor** = height(left subtree) - height(right subtree)
- Valid balance factors: -1, 0, 1
- If |balance factor| > 1, rotations are performed to rebalance

---

## Properties

1. **BST Property**:
   - Left child < Parent < Right child
   - In-order traversal produces sorted sequence

2. **Balance Property**:
   - For every node, |balance factor| ≤ 1
   - Height is always O(log n) for n nodes

3. **Height Balance**:
   - Height h < 1.44 log₂(n + 2) - 0.328 (theoretical bound)
   - Ensures worst-case efficiency

---

## Rotations

When balance factor violates [-1, 0, 1] range, rotations restore balance:

### 1. Left Rotation (LL Case)

```
    z                                y
   / \                             /   \
  T1  y     Left Rotate(z)        z      x
      / \   --------------->     / \    / \
     T2 x                       T1 T2 T3 T4
        / \
       T3 T4
```

### 2. Right Rotation (RR Case)

```
      z                            y
     / \                         /   \
    y  T4   Right Rotate(z)     x      z
   / \      -------------->    / \    / \
  x  T3                      T1 T2 T3 T4
 / \
T1 T2
```

### 3. Left-Right Rotation (LR Case)

```
     z                         z                           x
    / \                       / \                        /   \
   y  T4  Left Rotate(y)     x  T4  Right Rotate(z)    y       z
  / \     --------------->  / \      -------------->  / \     / \
T1  x                     y   T3                    T1 T2   T3 T4
    / \                   / \
   T2 T3                T1 T2
```

### 4. Right-Left Rotation (RL Case)

```
   z                       z                           x
  / \                     / \                        /   \
T1  y   Right Rotate(y) T1  x   Left Rotate(z)     z       y
    / \  -------------->     / \   ------------->  / \     / \
   x  T4                   T2  y                 T1 T2   T3 T4
  / \                         / \
 T2 T3                      T3 T4
```

---

## Operations

### 1. Insertion

1. Perform standard BST insertion
2. Update heights of ancestor nodes
3. Check balance factor for each ancestor
4. If unbalanced (balance factor = ±2), perform appropriate rotation:
   - Left-Left: Right rotation
   - Right-Right: Left rotation
   - Left-Right: Left then right rotation
   - Right-Left: Right then left rotation

### 2. Deletion

1. Perform standard BST deletion
2. Update heights of ancestor nodes
3. Check balance factor for each ancestor
4. If unbalanced, perform rotations as in insertion

### 3. Search

- Same as BST: O(log n) due to height balance

---

## Python Implementation

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        self.update_height(z)
        self.update_height(y)
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, root, key):
        # Standard BST insertion
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height
        self.update_height(root)

        # Check balance
        balance = self.balance_factor(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        # Standard BST delete
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Update height
        self.update_height(root)

        # Check balance
        balance = self.balance_factor(root)

        # Left Left Case
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # Utility function for inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)
```

---

## Time Complexities

| Operation     | Time Complexity |
| ------------- | --------------- |
| **Search**    | O(log n)        |
| **Insert**    | O(log n)        |
| **Delete**    | O(log n)        |
| **Rotations** | O(1)            |
| **Space**     | O(n)            |

---

## Advantages vs. Disadvantages

**Advantages**:

- Guaranteed O(log n) performance for all operations
- Efficient for search-intensive applications
- Prevents worst-case BST scenarios
- Better balance than Red-Black trees for search operations

**Disadvantages**:

- Higher overhead for insertions/deletions due to rotations
- More complex implementation than standard BST
- Requires storing height/balance factor for each node
- Slightly slower insertions/deletions than Red-Black trees

---

## Comparison with Other Trees

| Structure     | Search     | Insert     | Delete     | Balancing       | Height       |
| ------------- | ---------- | ---------- | ---------- | --------------- | ------------ |
| **AVL Tree**  | O(log n)   | O(log n)   | O(log n)   | Strict (height) | ≤ 1.44 log n |
| **Red-Black** | O(log n)   | O(log n)   | O(log n)   | Color-based     | ≤ 2 log n    |
| **BST**       | O(n) worst | O(n) worst | O(n) worst | None            | O(n) worst   |
| **B-Tree**    | O(log n)   | O(log n)   | O(log n)   | Degree-based    | O(log n)     |

---

## Use Cases

1. **Database indexing** where search time is critical
2. **Implementations of ordered maps/sets** in standard libraries
3. **Applications requiring frequent lookups** with occasional updates
4. **Real-time systems** with strict performance guarantees
5. **Priority queues** requiring efficient min/max operations
6. **Geometric algorithms** requiring balanced trees

---

```python
# Example usage
avl = AVLTree()
root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl.insert(root, key)

print("Inorder traversal:")
avl.inorder(root)  # 10 20 25 30 40 50

root = avl.delete(root, 30)
print("\nAfter deleting 30:")
avl.inorder(root)  # 10 20 25 40 50

print("\nSearch 25:", avl.search(root, 25) is not None)  # True
```

---

## Visualizing Balance

**Valid AVL Tree**:

```
       30 (BF: 0)
      /  \
(BF:0)20  40 (BF: -1)
    /      \
  10       50 (BF: 0)
```

**Invalid AVL Tree** (before rebalancing):

```
    30 (BF: -2)
   /
  20 (BF: -1)
   \
    25 (BF: 0)
```

After rotation (Right-Left case):

```
    25 (BF: 0)
   /  \
  20   30 (BF: 0)
```
