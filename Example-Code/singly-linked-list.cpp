#include <iostream>
using namespace std;

class Node {
  public:
    int data;
    Node *next;

    Node(int val) {
        data = val;
        next = NULL;
    }
};

class LinkedList {
  public:
    Node *head;

    LinkedList() { head = NULL; }

    void insert(int val) {
        Node *newNode = new Node(val);

        if (head == NULL) {
            head = newNode;
        } else {
            Node *curr = head;
            while (curr->next != NULL) {
                curr = curr->next;
            }
            curr->next = newNode;
        }
    }

    void display() {
        if (head == NULL) {
            cout << "List is empty" << endl;
        } else {
            Node *curr = head;
            while (curr != NULL) {
                cout << curr->data << " -> ";
                curr = curr->next;
            }
            cout << "NULL" << endl;
        }
    }
};

int main() {
    LinkedList myList;
    myList.insert(5);
    myList.insert(10);
    myList.insert(15);
    myList.display();
}
