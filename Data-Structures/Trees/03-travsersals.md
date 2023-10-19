## Traversing in a Tree

There are two ways to traverse in a Binary search tree :

1. **Depth-First-Search [DFS] :**
   In this method, the tree is traversed through it's entire height / length.

   There are 3 types of DFS :-

a. _In-order Traversal_ (left-**root**-right) : Start form the root, if there exists a left, go left, if no further left, print left, go back, print the root and now look for right, if right exists, apply the same logic.

```
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
        /     / \
       8     9  10
```

In above BST, if we apply In-order traversal, we get :

```
4 2 8 5 1 6 3 9 7 10
```

---

b. _Pre-Order-Traversal_ (**root**-left-right) : Start from the root, print root, if left exists, go left & print left, if no further left, go back, check for right, if right exists, apply the same logic.

In above BST, if we apply Pre-order traversal, we get :

```
1 2 4 5 8 3 6 7 9 10
```

---

c. _Post-Order-Traversal_ (left-right-**root**) : Start from the root, if left exists, go to left, print left, if no further left, go back, check if right exists, if exists print right, go back and print root.

In above BST, if we apply Pre-order traversal, we get :

```
4 5 8 2 6 7 9 10 7 3 1
```

---

2. **Breadth-first-Search [BFS] :** In this method, we traverse the tree level by level, through it's entire breadth.

```
        -->  1
           /   \
      --> 2     3
         / \   / \
    --> 4   5 6   7
           /     / \
      --> 8     9  10
```

**BFS in Above Tree :**

```
1 2 3 4 5 6 7 8 9 10
```
