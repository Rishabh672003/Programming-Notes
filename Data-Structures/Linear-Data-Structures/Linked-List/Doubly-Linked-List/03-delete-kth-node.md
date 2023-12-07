## Delete Kth Node of a DLL.

### Algorithm

1. Check if the DLL is empty, if so return NULL.
2. Create a pointer (here kNode) which will track the kth node to be deleted and initially point it to head.
3. Travers the DLL with the help of a counter and reach the kth node to be deleted.
4. Once reached, create 2 pointers, one pointing kNode's previous node and other pointing the just next node respectively.
5. Check if the kNode is a head or tail node with appropriate conditions and delete head or tail accordingly.
6. If not, point prev's next to front and front's back to prev, disconnecting both of them with kNode.
7. Still, kNode is conneted to prev and front so disconnect it as well.
8. Free up the kNode and return head.

---

### Implementation

```cpp
Node* deleteKthNode(Node* head, int k){
    if (head == NULL) return NULL;

    int cnt = 0;
    Node* kNode = head; // a pointer to the node to be deleted.
    while (kNode != NULL) {
        cnt++;
        if (cnt == k) break;
        kNode = kNode->next;
    }

    Node* prev = kNode->back;
    Node* front = kNode->next;

    if (prev == NULL && front == NULL){
        return NULL;
    }
    else if (prev == NULL) {
        deleteHeadDLL(head);
    }
    else if (front == NULL){
        deleteTailDLL(head)
    }

    prev->next = front;
    front->back = prev;
    kNode->next = kNode->back = NULL;
    delete kNode;
    return head;
}


Node* deleteHeadDLL(Node* head){
    if (head == NULL || head->next == NULL){
        return NULL;
    }

    Node* prev = head;
    head = head->next;
    head->back = NULL;
    prev->next = NULL;

    delete prev;
    return head;
}

Node* deleteTailDLL(Node* head){
    if (head == NULL || head->next == NULL){
        return NULL;
    }
    Node* tail = head;
    while(tail->next != NULL){
        tail = tail->next;
    }
    Node* newTail = tail->back;
    tail->back = NULL:
    newTail->next = NULL;

    delete tail
    return head;
}

```

```cpp
// delete given node :
void deleteNode(Node* temp){
    Node* prev = temp->back;
    Node* front = temp-> next;

    if (front = NULL){
        prev->next = NULL;
        temp->back = NULL;
        free(temp);
        return;
    }
    prev->next = front;
    front->back = prev;

    temp->next = temp->back = NULL;
}
```
