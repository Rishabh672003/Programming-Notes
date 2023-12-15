## Reverse the given LL

Given the head of a singly linked list, reverse the list, and return the reversed list.

### Algorithm

**Brute force (Data replacement)**

1. The most simple way to reverse a LL is to replace the data in it.
2. Create a LIFO data structure (Stack), Traverse the LL, and push all elements in the stack.
3. Traverse the LL again and re-assign the Node data with stack's top elements.
4. The LL would be reversed, return the head.

**TC : O(2N), SC : O(N)**

```cpp
Node* reverseList(Node* head) {
    Node* temp = head;
    stack<int> st;
    while(temp != nullptr){
        st.push(temp->data);
        temp = temp->next;
    }
    temp = head;
    while(temp != nullptr){
        temp->data = st.top();
        st.pop();
        temp = temp->next;
    }
    return head;
}
```

---

**Optimal Solution (Pointer swapping)**

1. `Currrent` is a pointer to keep track of current nodes. Set it to head. `prev` is a pointer to keep track of previous nodes. Set it to NULL. `next` is a pointer to keep track of the next nodes.

2. Set `next` to point next node to node pointed by current.
   Change link between nodes pointed by `current` and `prev`.
   Update `prev` to `current` and `current` pointer to `next`.

- Perform STEP 2 until current reaches the end of the list.

3. Set head as `prev`. This makes the head point at the last node.

**TC : O(N) SC : O(1)**

```cpp
Node* reverseList(Node* head) {
    Node* prev = nullptr;
    Node* current = head;
    while(current != nullptr){
        Node* front = current->next;
        current->next = prev;
        prev = current;
        current = front;
    }
    return prev;
}
```
