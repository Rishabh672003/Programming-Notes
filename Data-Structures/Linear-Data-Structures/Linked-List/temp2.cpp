#include <iostream>
#include <vector>

using std::cout, std::endl, std::vector;

class Node {
  public:
    // node members
    int data;   // data
    Node* next; // pointer

    // constructor
    Node(int data1) {
        data = data1;
        next = nullptr;
    }
};

int main() {
    vector<int> arr = {2, 3, 4, 6, 3};
    const Node* n1 = new Node(arr[1]);
    cout << n1->data << endl;
    cout << n1->next << endl;
    return 0;
}
