## Delete Nth Node from Back in a LL

Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Expected TC : O(N), SC : O(1)**

### Algorithm

**Brute Force (Two passes)**

Two reach the node to be deleted from back, we can first traverse the entire LL to know the size (using a counter) and then traverse again till `count - n`th node.

By this, we can reach the previous node of `n`th node and then we can easily remove the next node (technically `n`th node).

**TC : O(Length + Length-N) ~ O(2N) _unacceptable_, SC : O(1)**

```cpp
Node* removeNthFromEnd(Node* head, int n) {
    Node* temp = head;
    int cnt = 0;
    while(temp != nullptr){
        cnt++;
        temp = temp->next;
    }
    temp = head;
    int res = cnt - n;

    // Check if the node to be deleted is the head
    if (res == 0) {
        Node* newHead = head->next;
        delete head;
        return newHead;
    }

    // Move to the node before the one to be deleted
    while (temp != nullptr){
        res--;
        if (res == 0){
            break;
        }
        temp = temp->next;
    }

    if (temp->next != nullptr) {
        Node* deleteNode = temp->next;
        temp->next = temp->next->next;
        delete deleteNode;
    }
    return head;
}
```

---

**Optimal Solution (Two pointer)**

1. We'll take help of two pointers, `fast` and `slow` both initially pointing to head.
2. The fast pointer will move `n` steps and once it reaches, the slow pointer will start moving simultaneously unless the fast pointer reaches the last node.
3. Once the fast point reaches the last node, the slow node will be at the previous node of `n`th node.
4. Now we can easily remove the next node (technically `n`th node).

```cpp
Node* removeNthFromEnd(Node* head, int n){
    Node* fast = head;
    Node* slow = head;
    for (int i = 0; i < n; i++) fast = fast->next;
    if (fast == nullptr) return head->next;
    while (fast->next != nullptr){
        slow = slow->next;
        fast = fast->next;
    }
    Node* delNode = slow->next;
    slow->next = delNode->next;
    delete delNode;
    return head;
}
```
