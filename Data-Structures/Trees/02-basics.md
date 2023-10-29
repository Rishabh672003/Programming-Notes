## Representation of a Tree in C++

```
                        1 <-- data
     left pointer --> /   \ <-- right pointer
                     2     3
                    /       \
                   4       NULL
```

---

### Implementation :

```cpp
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
    // constructor
    Node(int value){
        data = value;
        left = right = NULL; // initially pointing to null
    }
}

// Tree Creation
int main() {
    // calling constructor and passing root's value.
    struct Node *root = new Node(1);

    root->left = new Node(2);
    root->right = new Node(3);

    root->left->left = new Node(4);

    return 0;
}
```
