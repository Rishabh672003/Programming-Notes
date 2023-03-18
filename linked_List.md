# Linked Lists.

WHAT? : It is a Linear Data Structure which is made up of collection of nodes. For example consider a capsule having two parts. Each part is made up of nodes, The first node is the "DATA" and the second node is the "Address of the next NODE". A linked list ends by pointing a "NULL Pointer".
How a Linked List looks : ``` [ DATA | ADDRESS ]->[ DATA | ADDRESS ]->[ DATA | NULL ] ```

WHY? : Think if you have an array of 10 size, so can we change its size on run time ? NO! A Vector, when same value is inserted to it, it doubles its size and additional memory gets wasted, hence a vector is not an optimal data structure. Unlike these two, size of linked list can grow or shrink on run time, hence no memory waste.

# Types of Linked Lists:
1. Singly Linked List.
2. Doubly Linked List.
3. Circular Linked List.
4. Circular Doubly Linked List.

# Implementation: 
```cpp

// Singly Linked List.
class Node{
public:
int data; // the "DATA" part of node.
Node*  nextNode; // the "ADDRESS" part of node.

// Constructor
Node(int data){
  this -> data = data;
  this -> nextNode = NULL;
 }

};

int main(){
  Node* node1 = new Node(10);
  cout << node1 -> data << endl; // prints the data i.e, 10.
  cout << node1 -> nextNode << endl; // prints NULL address 0x0.
  return 0;
}

/*
Node* node1 = new Node();

The line of code is allocating memory for a new object of the class named "Node" on the heap and
assigning the address of the object to a pointer variable named "node1".
The "new" operator dynamically allocates memory for the object and returns a pointer to the allocated memory.
The parentheses after "Node()" call the default constructor of the class or struct to initialize the object.
The result of this line of code is that you now have a dynamically allocated object of the "Node" class or struct,
and you can access its member variables and functions through the "node1" pointer. 
*/

```
