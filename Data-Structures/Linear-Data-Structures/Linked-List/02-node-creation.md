## Creating a Node in Linked List

The self defined data type to create a node could be a struct or a class.

### C++ Implementation :

```cpp
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
  // node members
  int data;   // data
  Node *next; // pointer

  // constructor
  Node(int val) {
    data = val;
    next = nullptr;
  }
};

int main() {
  vector<int> arr = {2, 3, 4, 6, 3};
  Node *n1 = new Node(arr[1]); // creating a new node
  cout << n1->data << endl; // print 3
  cout << n1->next << endl; // prints Null address
  return 0;
}
```

The line `Node *n1 = new Node(arr[1]);` of code is allocating memory for a new object of the class named `Node` on the heap and assigning the address of the object to a pointer variable named `next`.
