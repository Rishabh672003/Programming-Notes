## Insert a new node kth position

### Algorithm

1. Check if LL is empty, incase create new Node with new value.
2. If k is equal to 1, use insertAtHead logic.
3. Create a counter to keep track of just behind node of `k`th node.
4. Create a temp node and point to head.
5. Traverse thorugh the LL and check the following :
   - For each node, increase the counter and likewise move the temp ahead.
   - If it is `k-1`th node, create new Node with new value.
   - Point the new node's next to temp's next.
   - Point temp's next to new node and break the loop.
6. Return head.

---

### Implementation

```cpp
Node* insertAtK(Node* head, int k, int newVal){
    if (head == nullptr) {
        if (k == 1) return new Node(newVal);
    }

    if (k == 1) {
        Node* newNode = new Node(newVal);
        newNode->next = head;
        return newNode;
    }

    int cnt = 0;
    Node* temp = head;
    while (temp != nullptr){
        cnt++;
        if (cnt == (k-1)){
            Node* x = new Node(newVal);
            x->next = temp->next;
            temp->next = x;
            break;
        }
        temp = temp->next;
    }
    return head;
}
```
