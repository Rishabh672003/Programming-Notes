## Insertion in a Linked List.

### 1. Insertion at head

**Steps :**

1. Make a `void` function which accepts a reference to a head pointer and a data as parameter.
2. Make a new temporary Node which accepts the data parameter.
3. Then point the temp node's next pointer to the current head.
4. Finally temp becomes our new head pointer.

---

### 2. Insertion at tail

**Steps :**

1. Make a `void` function which accepts a reference to a tail pointer and a data as parameter.
2. Make a new temporary Node which accepts the data parameter.
3. Then point the tail node's next pointer to the temp node.
4. Finally temp becomes our new tail pointer.

---

### 2. Insertion at any position

**Steps :**

1. Make a `void` function which accepts a reference to head & tail pointer and a position & data as parameter.
2. Make a temp node which'll initially point to head.
3.
4.

---

### Implementation :

```cpp
#include <bits/stdc++.h>
#include <cstddef>
using namespace std;

class Node {
public:
  int data;
  Node *next;

  Node(int data) {
    this->data = data;
    this->next = NULL;
  }
};

void insertAtHead(Node *&head, int data) {
  Node *temp = new Node(data);
  temp->next = head;
  head = temp;
}

void insertAtTail(Node *&tail, int data) {
  Node *temp = new Node(data);
  tail->next = temp;
  tail = temp;
}

void insertAtPosition(Node *&head, Node *&tail, int pos, int data) {
  Node *temp = head;
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

  Node *nodeToInsert = new Node(data);
  nodeToInsert->next = temp->next;
  temp->next = nodeToInsert;
}

void printLinkedList(Node *&head) {
  Node *temp = head;
  while (temp != NULL) {
    cout << temp->data << " ";
    temp = temp->next;
  }
  cout << endl;
}

int main() {
  Node *node1 = new Node(10);

  // create head and tail pointer.
  Node *head = node1;
  Node *tail = node1;

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

```
Output :
Initial List : 10
List after insertion at head : 12 10
List after insertion at tail : 12 10 13
List after insertion at 3rd position : 12 10 14 13
```

---
