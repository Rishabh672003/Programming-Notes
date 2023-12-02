## Insertion in a Linked List.

### 1. Insertion at head

- Create a new node and assign the data to it.
- Set the `next` pointer of the new node to the current head of the list.
- Update the head of the list to the new node.

---

### 2. **Insertion at tail**

- Create a new node and assign the data to it.
- Set the `next` pointer of the current tail node to the new node.
- Update the tail of the list to the new node.

---

### 3. **Insertion at any position**

- If the position is 1, insert at the head.
- If the position is greater than the length of the list, insert at the tail.
- Otherwise, traverse the list to the desired position.
- Create a new node and assign the data to it.
- Set the `next` pointer of the new node to the node currently at the desired position.
- Update the `next` pointer of the node before the desired position to the new node.

---

### Implementation :

```cpp
#include <iostream>

using std::cout, std::cin, std::endl, std::string;

class Node {
  public:
    int data;
    Node* next;

    explicit Node(int data) {
        this->data = data;
        this->next = NULL;
    }
    virtual ~Node() {
        if (this->next != NULL) {
            delete next;
            this->next = NULL;
        }
    }
};

void insertAtHead(Node*& head, int data) {
    Node* temp = new Node(data);
    temp->next = head;
    head = temp;
}

void insertAtTail(Node*& tail, int data) {
    Node* temp = new Node(data);
    tail->next = temp;
    tail = temp;
}

void insertAtPosition(Node*& head, Node*& tail, int pos, int data) {
    Node* temp = head;
    int cnt = 1;

    // if inserting at first pos
    if (pos == 1) {
        insertAtHead(head, data);
        return;
    }

    // if inserting at last pos
    if (temp->next == NULL) {
        insertAtTail(tail, data);
        return;
    }

    while (cnt < pos - 1) {
        temp = temp->next;
        cnt++;
    }

    Node* nodeToInsert = new Node(data);
    nodeToInsert->next = temp->next;
    temp->next = nodeToInsert;
}

void printLinkedList(Node*& head) {
    Node* temp = head;
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    Node* node1 = new Node(10);

    // create head and tail pointer.
    Node* head = node1;
    Node* tail = node1;

    cout << "Initial List : ";
    printLinkedList(head);

    insertAtHead(head, 12);

    cout << "List after insertion at head : ";
    printLinkedList(head);

    insertAtTail(tail, 13);

    cout << "List after insertion at tail : ";
    printLinkedList(head);

    insertAtPosition(head, tail, 3, 14);

    cout << "List after insertion at 3rd position : ";
    printLinkedList(head);
    return 0;
}
```

**Output** :

```
Initial List : 10
List after insertion at head : 12 10
List after insertion at tail : 12 10 13
List after insertion at 3rd position : 12 10 14 13
```

---
