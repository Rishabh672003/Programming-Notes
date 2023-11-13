## In-Order-Traversal ~ Recursive approach C++ Implementation

```
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
        /     / \
       8     9  10
```

### Implementation :

```cpp
void inorder(int node) {
    if (node == NULL) { // base case
        return;
    }
    inorder(node->left); // recursion
    cout << node->data << endl;
    inorder(node->right); // recursion
}
```

pattern : left --> print --> right
