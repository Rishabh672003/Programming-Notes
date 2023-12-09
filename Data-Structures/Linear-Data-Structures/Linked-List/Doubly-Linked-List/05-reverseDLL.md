## Reverse the given DLL

### Brute Force (Stack Method) :

1. Create a temp pointer, point it to head.
2. Create a stack of type `int`.
3. Traverse through the DLL, push the current node's data into stack.
4. Once traversed, reassign temp to head and start traversing again.
5. In this traversal, assign the temp's data to stack's top and then pop the stack's top element.
6. In the end, return head of the revrsed DLL.

**Time Complexity : O(2N)**

**Space Complexity : O(N)**

```cpp
Node* reverseDLL(Node* head){
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

### Optimal approach (Pointer Swap) :

In this approach, we'll use a swaping method to swap `prev` and `next` pointers. This idea comes from generic two number swap equation, which is, temp = a, a = b, b = temp.

1. Check if the DLL is null or a singleton, in that case return the head itself.
2. Create a current pointer which points to head and a prev pointer which will point to null.
3. Start travering the DLL, For each current node :
   - Bring the prev pointer to it's back.
   - Point the current's back to current's next.
   - Point the current's next to back.
   - Move the current ahead.
4. Return prev's back, as current goes to null.

**Time Complexity : O(N)**

**Space Complexity : O(1)**

```cpp
Node* reverseDLL(Node* head){
    if (head == nullptr || head->next == nullptr){
        return head;
    }
    Node* current = head;
    Node* prev = nullptr;

    while(current != nullptr){
        prev = current->back;
        curreent->back = current->next;
        current->next = prev;
        current = current->back;
    }
    return prev->back;
}
```
