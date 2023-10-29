## Post-Order-Traversal ~ Recursive approach C++ Implementation

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
void postorder(int node) {
    if (node == NULL) { // base case
        return;
    }
    postorder(node->left);  // recursion
    postorder(node->right); // recursion
    cout << node->data << endl;
}
```

pattern : left --> right --> print
