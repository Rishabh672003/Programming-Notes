## Doubly Linked List

Unlike a singly linked list, where each node only has a pointer to the next node, A doubly linked list (DLL) has two pointers:

- Next pointer: Points to the next node in the list.
- Previous pointer: Points to the previous node in the list.

This additional Previous pointer allows traversing the list in both directions (forward and backward).

Advantages of DLL over singly linked list:

- Bidirectional traversal: Traversing the list in both directions is possible.
- Efficient deletion: Removing a node is faster as the previous node's pointer can be updated directly.
- Insertion before a node: Inserting a new node before a specific node is easier.

---

### DLL Node Creation

```cpp
class Node {
public:
    int data;
    Node* next;
    Node* back;

    Node(int val, Node* next1, Node* back1){
        data = val;
        next = next1;
        back = back1;
    }

    Node(int val){
        data = val;
        next = nullptr;
        back = nullptr;
    }
};
```
