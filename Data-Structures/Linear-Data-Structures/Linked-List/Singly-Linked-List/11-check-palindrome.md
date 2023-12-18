## Check if the LL is palindrome

Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.

**Expected TC : O(N), SC : O(1)**

---

### Algorithm

**1. Brute Force (Stack method)**

**TC O(2N), SC O(N)**

```cpp
bool isPalindrome(Node* head) {
    stack<int> st;
    Node* temp = head;
    while (temp != nullptr){
        st.push(temp->val);
        temp = temp->next;
    }
    temp = head;
    while (temp != nullptr){
        if (temp->val != st.top()){
            return false;
            break;
        }
        temp = temp->next;
        st.pop();
    }
    return true;
}
```

---

**2. Optimal Solution (Reverse half LL)**

Three Steps to follow :

1. Find the middle of LL (hare & tortoise method).
2. Reverse one half (obviously the second half).
3. Compare first half with another one.

**TC O(2N), SC O(1)**

```cpp
Node* reverse(Node* head){
    // recursion
    if (head == nullptr || head->next == nullptr){
        return head;
    }
    Node* newHead = reverse(head->next);
    Node* front = head->next;
    front->next = head;
    head->next = nullptr;
    return newHead;
}

bool isPalindrome(Node* head) {
    if (head == nullptr || head->next != nullptr){
        return true;
    }

    // 1. find middle
    Node* slow = head;
    Node* fast = head;
    while (fast->next != nullptr && fast->next->next != nullptr) { // O(N/2)
        slow = slow->next;
        fast = fast->next->next;
    }

    // 2. Reverse
    slow->next = reverse(slow->next);

    // compare
    slow = slow->next;
    ListNode* dummy = head;

    while(slow!=NULL) {
        if(dummy->val != slow->val) return false;
        dummy = dummy->next;
        slow = slow->next;
    }
    return true;
}
```
