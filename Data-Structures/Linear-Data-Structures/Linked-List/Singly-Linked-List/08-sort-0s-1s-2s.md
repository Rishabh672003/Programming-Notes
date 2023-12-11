## Sort the 0s, 1s and 2s in the given LL

Given a LL of N nodes, where each node has an integer value that can be 0, 1, or 2. You need to sort the linked list in non-decreasing order and the return the head of the sorted list.

**Expected TC O(N), SC O(1)**

---

### Algorithm

**Brute Force (Data replacement)**

1. Create 3 variables to keep the count of 0s, 1s and 2s in the LL.
2. Traverse through the LL, increase the count of those 3 variables as you found them in LL.
3. Once traversed the LL entirely, come back to head and start another traversal.
4. In this traversal, re-assign each node's data based on the availability of 0s, 1s and 2s.
5. Return the head.

- **TC O(2N), SC O(1)**

**Implementation**

```cpp
// Brute force
Node* sort012(Node* head) {
    int cont0 = 0, count1 = 0, count2 = 0;
    Node* temp = head;
    while(temp != nullptr){
        if(temp->data == 0) count0++;
        else if(temp->data == 1) count1++;
        else count2++;
        temp = temp->next;
    }
    temp = head;
    while(temp != nullptr){
        if (count0) {
            temp->data = 0;
            count0--;
        }
        else if (count1) {
            temp->data = 1;
            count1--;
        }
        else {
            temp->data = 2;
            count2--;
        }
        temp = temp->next;
    }
    return head;
}
```

---

**Optimal Solution (Dutch National Flag algorithm)**

1. Initialize three dummy nodes and pointers for each category (0, 1, 2). Let `zeroHead`, `oneHead`, and `twoHead` be dummy nodes. Create `zero`, `one`, and `two` pointers to the last nodes for 0s, 1s, and 2s.
2. Traverse the original linked list using a temporary pointer `temp`.
3. For each traversal :

   Check the value of `temp->data`.

   If it's 0, append temp to the end of the 0s list by pointing zero's next to temp and update the zero pointer.

   If it's 1, append temp to the end of the 1s list by pointing one's next to temp and update the one pointer.

   If it's 2, append temp to the end of the 2s list by pointing two's next to temp and update the two pointer.

4. After the traversal, connect the three LLs. **To connect 0s with 1s, first check if 1s exist, else connect with 2s.**
5. Update the head of new sorted list and delete all the dummy nodes.
6. Return new head.

**Implementation**

```cpp
// optimal
Node* sortList(Node* head) {
    Node* zeroHead = new Node(-1);
    Node* oneHead = new Node(-1);
    Node* twoHead = new Node(-1);

    Node* zero = zeroHead;
    Node* one = oneHead;
    Node* two = twoHead;

    Node* temp = head;

    while (temp != nullptr) {
        if (temp->data == 0) {
            zero->next = temp;
            zero = temp;
        } else if (temp->data == 1) {
            one->next = temp;
            one = temp;
        } else {
            two->next = temp;
            two = temp;
        }
        temp = temp->next;
    }

    zero->next = oneHead->next ? oneHead->next : twoHead->next;
    one->next = twoHead->next;
    two->next = nullptr;

    Node* newHead = zeroHead->next;
    delete zeroHead;  // Free the dummy nodes
    delete oneHead;
    delete twoHead;

    return newHead;
}
```
