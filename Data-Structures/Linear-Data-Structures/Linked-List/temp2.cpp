#include <bits/stdc++.h>
using namespace std;

class Node {
public:
  // node members
  int data;   // data
  Node *next; // pointer

  // constructor
  Node(int data1) {
    data = data1;
    next = nullptr;
  }
};

int main() {
  vector<int> arr = {2, 3, 4, 6, 3};
  Node *n1 = new Node(arr[1]);
  cout << n1->data << endl;
  cout << n1->next << endl;
  return 0;
}
