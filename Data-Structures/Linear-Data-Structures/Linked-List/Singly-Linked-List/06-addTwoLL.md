## Add two Non-Zero Linked Lists

We are given two non-empty linked lists representing two non-negative integers.
The digits are stored in **reverse order**, and each of their nodes contains a single digit.
Add the two numbers and **return the sum as a linked list**.
We may assume the two numbers do not contain any leading zero, except the number 0 itself.

(Don't get panic by looking at reverse order, cause even with usual addition, we always start from unit's place.)

---

### Algorithm

Let's break this problem down into 5 parts, **initial setup, traversal, calculation, building sum LL, The Last carry.**

1. Initial setup :
   - We are provided with two heads of LLs, So we will create 2 temporary pointers `t1` and `t2` pointing at respective head nodes.
   - We'll create a `dummyNode` with some random value to track the head of newly formed LL. Also we'll maintain a `curr` pointer to track current sum LL nodes.
   - We'll create a variable to store carry.
2. Traversal:
   - Inorder to add each node, we'll need to traverse both the LLs unless we reach `NULL`.
3. Calculation :
   - For each node, we'll create a new `sum` variable which is initially assigned with `carry`.
   - If any of the `t1` or `t2` is a valid node, we'll add their vules into `sum` variable.
   - To store the sum in a LL node, we'll then create a new Node and store the (%10) of sum. By this, we'll be able to seperate the unit's digit of our sum if it is >10.
   - Then we'll extract the carry from the sum by dividing sum by 10.
4. Builing the sum LL :
   - Once we've a node ready which holds the sum, we'll now append this node to `dummyNode`. With the help of `curr` pointer, we'll build the LL.
   - Once we've added the `sumNode`, we'll now move ahead in both the LLs.
5. Check for carry :
   - Once we are done adding the LLs, still we need to check if we've some value in our carry variable, if so, create a new node for carry and append it in the sum LL.

In the end, return `dummyNode`'s next as a head for new sum LL.

---

### Implementation

```cpp
Node* addTwoNumbers(Node* h1, Node* h2){
    // setup
    Node* t1 = h1;
    Node* t2 = h2;
    Node* dummyNode = new Node(-1);
    Node* curr = dummyNode;
    int carry = 0;

    // traveral
    while (t1 || t2) {
        // calculation
        int sum = carry;
        if (t1) sum += t1->data;
        if (t2) sum += t2->data;
        Node* sumNode = new Node(sum%10);
        carry = sum/10;

        // build the new LL
        curr->next = sumNode;
        curr = sumNode;
        // move ahead
        t1 = (t1 != nullptr) ? t1->next : nullptr;
        t2 = (t2 != nullptr) ? t2->next : nullptr;
    }
    // append left over carry
    if (carry) {
        Node* carryNode = new Node(carry);
        curr->next = carryNode;
    }

    // return new head
    return dummyNode->next;
}
```
