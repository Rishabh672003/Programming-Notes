# Segment Tree

A **segment tree** is a versatile data structure used to efficiently answer range queries and perform range updates on an array. It enables querying aggregate information (sum, minimum, maximum, etc.) over any interval in logarithmic time while supporting point or range updates.

---

## Key Concepts

### Purpose

- Answer **range queries** (sum, min, max, product, GCD, etc.) in O(log n) time
- Perform **point updates** and **range updates** in O(log n) time
- Handle **dynamic data** where values change between queries
- Solve problems involving range-based operations efficiently

### Structure

- **Binary tree** where each node represents a segment of the original array
- **Root node** represents the entire array
- **Leaf nodes** represent individual elements
- **Internal nodes** represent merged segments of their children
- **Complete binary tree** (all levels filled except possibly last, filled left to right)

---

## Properties

### Structure Property

- **Balanced tree**: Height is ⌈log₂n⌉
- **Array representation**: Similar to heaps (children at 2i and 2i+1)
- **Space requirement**: O(4n) for safe implementation

### Query Property

- Any range [L, R] can be covered by O(log n) nodes
- Query results are computed by merging segment results

### Update Property

- Updates affect O(log n) nodes along the update path
- Range updates can be optimized with lazy propagation

---

## Array Representation

Segment trees are typically implemented using arrays:

- **Root** at index 1 (index 0 often unused)
- For node at index i:
  - **Left child**: 2i
  - **Right child**: 2i+1
  - **Parent**: i//2

### Example: Array [1, 3, 5, 7, 9, 11]

```
Tree representation (range sums):
           [0:5]=36
         /          \
    [0:2]=9       [3:5]=27
    /     \       /     \
 [0:1]=4 [2]=5 [3:4]=16 [5]=11
  /   \        /   \
[0]=1 [1]=3 [3]=7 [4]=9

Array representation:
Index: 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
Value: 0 36  9 27  4  5 16 11  1  3  0  0  7  9  0  0
```

---

## Operations

### 1. Building the Tree (O(n))

Recursively construct segments:

- Divide current segment into two halves
- Recursively build left and right subtrees
- Merge children values to compute parent

### 2. Range Query (O(log n))

1. Start at root covering [0, n-1]
2. If current segment fully within [L, R], return its value
3. If segment partially overlaps:
   - Recursively query left child (if overlaps)
   - Recursively query right child (if overlaps)
4. Combine results from relevant segments

### 3. Point Update (O(log n))

1. Update corresponding leaf node
2. Propagate change upward to all ancestors:
   - Update parent = merge(left child, right child)
   - Repeat until root is updated

---

## Python Implementation (Range Sum)

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:  # Find smallest power of 2 >= n
            self.size *= 2
        self.tree = [0] * (2 * self.size)

        # Build tree (leaves at tree[size] to tree[size+n-1])
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def query(self, l, r):
        # Query range [l, r] (0-indexed, inclusive)
        l += self.size
        r += self.size
        res = 0
        while l <= r:
            if l % 2 == 1:  # l is right child
                res += self.tree[l]
                l += 1
            if r % 2 == 0:  # r is left child
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res

    def update(self, index, value):
        # Point update: set arr[index] = value
        i = self.size + index
        self.tree[i] = value
        i //= 2
        while i >= 1:  # Update all ancestors
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
            i //= 2
```

---

## Time Complexities

| Operation            | Standard | With Lazy Propagation |
| -------------------- | -------- | --------------------- |
| **Construction**     | O(n)     | O(n)                  |
| **Point Update**     | O(log n) | O(log n)              |
| **Range Query**      | O(log n) | O(log n)              |
| **Range Update**     | O(n)     | O(log n)              |
| **Space Complexity** | O(n)     | O(n)                  |

---

## Use Cases

1. **Range Sum Queries with Updates**
2. **Range Minimum/Maximum Queries (RMQ)**
3. **Finding Subarray GCD/LCM**
4. **Counting Inversions**
5. **Interval Scheduling Problems**
6. **Computing Range Products**
7. **Histogram Analysis**
8. **Geometric Range Queries**

---

## Comparison with Other Structures

| Structure        | Point Update | Range Query | Range Update | Use Case                   |
| ---------------- | ------------ | ----------- | ------------ | -------------------------- |
| **Segment Tree** | O(log n)     | O(log n)    | O(log n)\*   | General range operations   |
| **Fenwick Tree** | O(log n)     | O(log n)    | O(log n)     | Prefix sums, point queries |
| **Sparse Table** | O(n)         | O(1)        | Not possible | Static RMQ                 |
| **Prefix Array** | O(n)         | O(1)        | O(n)         | Static range queries       |

_\*With lazy propagation_

---

## Common Variations

1. **Persistent Segment Trees**: Maintain historical versions
2. **2D Segment Trees**: For matrix operations
3. **Implicit Segment Trees**: For sparse data/ranges
4. **Segment Trees with Coordinate Compression**: For large value ranges
5. **Merge Sort Trees**: For range k-th element queries

---

```python
# Example usage for range sum queries
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(1, 4))  # 3+5+7+9 = 24
st.update(2, 10)       # Set arr[2] = 10
print(st.query(1, 4))  # 3+10+7+9 = 29

lst = LazySegmentTree(arr)
lst.update_range(1, 4, 5)  # Add 5 to elements 1-4
print(lst.query_range(1,4)) # (3+5+7+9) + 4*5 = 44
```
