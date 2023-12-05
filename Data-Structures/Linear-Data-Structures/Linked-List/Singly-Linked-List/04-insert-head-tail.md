## Insert a new Node at Head and Tail of a Linked List

### Algorithm

**Insertion at head**

1. Check if LL is empty, incase create new Node with new value.
2. Create a new node and assign the data to it.
3. Set the `next` pointer of the new node to the current head of the list.
4. Update the head of the list to the new node.

---

**Insert at tail**

1. Check if LL is empty, incase create new Node with new value.
2. Create a temp node, point it to head.
3. Iterate through the LL unless reach the tail node.
4. Create a new node, assign it the new value.
5. Make the tail node point the temp node.

---

### Implementation

```cpp
Node* insertAtHead(Node* head, int newVal){
    if (head == nullptr) {
        return new Node(val);
    }
    /* assuming the constructor only accepts
    value and not pointer with it */
    Node* temp = new Node(val);
    temp->next = head;
    temp = head;
}

Node* insertAtTail(Node* head, int newVal){
    if (head == nullptr) {
        return new Node(newVal);
    }
    Node* temp = head;
    while (temp->next != nullptr){
        temp = temp->next;
    }
    Node* newTail = new Node(newVal);
    temp->next = newTail;
}
```
