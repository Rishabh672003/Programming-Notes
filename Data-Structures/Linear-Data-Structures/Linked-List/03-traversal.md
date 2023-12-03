## Traversing in a Linked List

### Algorithm :

1. Create a temporary node (temp) which points to head node.
2. Unless the temp points to a NULL node, do the following things repeatedly :
   - print current temp node's data.
   - move the temp node ahead by assigning the temp node to its next node.

```cpp
class Solution {
  public:
    void display(Node* head) {
        Node* temp = head;
        while (temp != NULL) {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
    }
};
```

---

### Depiction of traversal

![linked-list-1](https://github.com/amitsuthar69/assets/blob/main/linked-lists/linked-list-traversal.png?raw=true)
