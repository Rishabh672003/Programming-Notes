## Reverse a Linked List

### Approach :

1. Initialize prev to nullptr and current to the head of the original linked list.
2. Enter a while loop that terminates when current is nullptr.
3. Inside the while loop, do the following:
   - Store the next node in the original linked list in next.
   - Update the next pointer of the current node to point to the previous node.
   - Update the prev pointer to point to the current node.
   - Update the current pointer to point to the next node.
4. Return prev, which is now the head of the reversed linked list.

---

### Imlementation :

```cpp
#include <bits/stdc++.h>
using namespace std;

template <typename T> class LinkedListNode {
public:
  T data;
  LinkedListNode<T> *next;
  LinkedListNode(T data) {
    this->data = data;
    this->next = NULL;
  }
};

// Solution :-
LinkedListNode<int> *reverseLinkedList(LinkedListNode<int> *head) {

    LinkedListNode<int> *prev = nullptr;
    LinkedListNode<int> *current = head;
    LinkedListNode<int> *next = nullptr;

    while (current != nullptr) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

int main() { return 0; }
```
