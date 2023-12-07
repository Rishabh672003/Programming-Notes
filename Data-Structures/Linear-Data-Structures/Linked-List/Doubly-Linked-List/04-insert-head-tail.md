## Insert a Node before Head and Tail of a DLL

```cpp
Node* insertBeforeHead(Node* head, int val){
    if (head == NULL){
        Node* newHead = new Node(val);
        return newHead;
    }
    Node* newHead = new Node(val, head, nullptr);
    head->back = newHead;
    return newHead;
}

Node* insertBeforeTail(Node* head, int val){
    if (head == NULL){
        Node* newHead = new Node(val);
        return newHead;
    }
    
    if (head->next == NULL && head->back == NULL) {
        insertBeforeHead(head, val);
    }

    Node* temp = head;
    while(temp->next->next != NULL){
        temp = temp->next;
    }
    Node* front = temp->next;
    Node* newNode = new Node(val, front, temp);
    temp->next = front->back = newNode;
    return head;
}
```
