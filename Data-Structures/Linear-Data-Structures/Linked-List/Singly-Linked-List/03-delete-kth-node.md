## Delete Kth node of a Linked list

### Algorithm

1. Check if LL is empty.
2. Check if the `k`th node we've to delete is the head itslef.
3. Create a counter to keep a track of current position in LL.
4. Create a prev node to keep a sustain the `k-1`th node.
5. Iterate thorugh the LL and do the following steps :
   - Increase counter to record current position.
   - Bring the prev node to temp and move temp ahead.
   - If current position is equal to k :
     - Point the prev node to prev's next to next node (means skipping the `k`th node).
     - Free the temp node (`k`th node) as it is no longer needed.
     - Break the loop to avoid further iterations.

6. Return head of the LL

---

### Implementation

```cpp
Node* deleteK(Node* head, int k) {
    if (head == nullptr)
        return nullptr;
    if (k == 1) { // if head node
        Node* temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    int cnt = 0;
    Node* temp = head;
    Node* prev = nullptr;
    while (temp != nullptr) {
        cnt++;
        if (cnt == k) {
            prev->next = prev->next->next;
            free(temp);
            break;
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
}
```

---

The step to create a temp node and then deleting it, is a memory saving option. The head could be deleted by just pointing current head to its next and then just returning the new head, but then we waste memory worth one node.
