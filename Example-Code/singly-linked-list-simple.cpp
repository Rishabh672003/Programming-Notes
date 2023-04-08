#include <iostream>
using namespace std;

// we create a class called Node which has two variables data and next
// the data variable is used to store the data and the next variable is used to
// store the address of the next node
class Node {
  public:
    int data;
    Node *next;
};

int main() {
    // We created three nodes head, second and third and point them to NULL
    // because we don't have any nodes yet
    Node *head = NULL;
    Node *second = NULL;
    Node *third = NULL;

    // then we allocate the nodes in the heap memory
    head = new Node();
    second = new Node();
    third = new Node();

    // then we put the data in the nodes
    head->data = 1;
    // then we create a current node and point it to the head node
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL;

    Node *current = head;

    // then we print the data of the current node and then we point the current
    // node to the next node we do this until the current node is not equal to
    // NULL
    while (current != NULL) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
    return 0;
}
