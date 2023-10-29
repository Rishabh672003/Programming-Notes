## Pre-Order-Traversal ~ Recursive approach C++ Implementation

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
void preorder(int node) {
    if (node == NULL) { // base case
        return;
    }
    cout << node->data << endl;
    preorder(node->left);  // recursion
    preorder(node->right); // recursion
}
```

pattern : print --> left --> right
