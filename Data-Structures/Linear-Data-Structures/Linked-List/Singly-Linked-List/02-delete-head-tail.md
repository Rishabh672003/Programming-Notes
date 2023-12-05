## Delete the head and tail of a Linked List

### Algorithm

**Delete head :**

1. Check if the head is not NULL.
2. Create a temp pointer and point it to head.
3. Point the head to its adjacent node.
4. Free the previous head node.

**Delete tail :**

1. Check if head isn't NULL or a singleton LL.
2. Create a temp pointer, point it to head.
3. Traverse till the second last node. (a second last node will be a node whose next->next is a NULL)
4. Once reached the second last node, free the next node (tail).
5. Point second last node to NULL

---

### Implementation

```cpp
Node* deleteHead(Node* head){
    if (head == NULL) return head; // edge case
    Node* temp = head;
    head = head->next;
    delete temp; // c++ lacks garbage collection
    return head;
}

Node* deleteTail(Node* head){
    // either empty or singleton
    if (head == NULL || head->next == NULL) {
        return NULL;
    }
    Node* temp = head;
    while(temp->next->next != NULL) {
        temp = temp->next;
    }
    delete temp->next;
    temp->next = nullptr;
    return head;
}
```
