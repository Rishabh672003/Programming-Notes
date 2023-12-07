## Delete head and tail of a DLL

### Algorithm :

**Delete Head :**

1. If DLL is empty or is a singleton, return NULL.
2. Else, make a `prev` pointer and point to head to keep a trck of head.
3. Move the current head pointer to the next node.
4. Point new head's back to NULL and prev's next to NULL to disconnect the first node.
5. Free up the memory by deleting the prev node.
6. Return new head.

**Delete tail :**

1. If DLL is empty or is a singleton, return NULL.
2. Else, create a temporary tail pointer and point it to head.
3. Start traversing the DLL unless we reach the actual tail node.
4. Tail's previous node becomes our new tail by pointing actual tail's back to the previous node. This will help us to track the new tail node.
5. Now point actual tail's back and new tail's next to NULL so it gets disconnected from the DLL.
6. Free up the memory by deleting the actual tree.
7. Return head.

---

```cpp
Node* deleteHeadDLL(Node* head){
    if (head == NULL || head->next == NULL){
        return NULL;
    }

    Node* prev = head;
    head = head->next;
    head->back = NULL;
    prev->next = NULL;

    delete prev;
    return head;
}

Node* deleteHeadDLL(Node* head){
    if (head == NULL || head->next == NULL){
        return NULL;
    }
    Node* tail = head;
    while(tail->next != NULL){
        tail = tail->next;
    }
    Node* newTail = tail->back;
    tail->back = NULL:
    newTail->next = NULL;

    delete tail
    return head;
}
```
