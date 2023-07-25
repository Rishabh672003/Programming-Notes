# Stacks

### Basic definition

A stack is a linear data structure that follows the principle of Last In First
Out (LIFO). This means the last element inserted inside the stack is removed
first. A real-life example of a stack is a pile of plates stacked on top of
another. If you want the plate at the bottom, you must first remove all the
plates on top.

### Working of stack

A stack uses a pointer called TOP to keep track of the top element in the stack.
When initializing the stack, its value is set to -1 so that we can check if the
stack is empty by comparing TOP == -1. On pushing an element, we increase the
value of TOP and place the new element in the position pointed to by TOP. On
popping an element, we return the element pointed to by TOP and reduce its value.

### Advantages and uses of Stacks

Stacks are very powerful despite their simplicity. They are used to reverse a
word, in compilers to calculate the value of expressions, and in browsers to
manage the history of URLs visited. Each time you visit a new page, it is added
on top of the stack. When you press the back button, the current URL is removed
from the stack, and the previous URL is accessed. For the array-based
implementation of a stack, the push and pop operations take constant time, i.e.
O(1)

## Implementations

### Implementation in C++

```cpp
#include <iostream>
#define MAX_SIZE 100

// Function to push an element into the stack
void push(int stack[], int &top, int value) {
    if (top == MAX_SIZE - 1) {
        std::cout << "Stack Overflow!\n";
    } else {
        top++;
        stack[top] = value;
        std::cout << "Element " << value << " pushed successfully!\n";
    }
}

// Function to pop an element from the stack
void pop(int stack[], int &top) {
    if (top == -1) {
        std::cout << "Stack Underflow!\n";
    } else {
        int value = stack[top];
        top--;
        std::cout << "Element " << value << " popped successfully!\n";
    }
}

// Function to get the top element of the stack
int top(int stack[], int top) {
    if (top == -1) {
        std::cout << "Stack is empty!\n";
        return -1; // assuming -1 represents an empty stack
    } else {
        return stack[top];
    }
}

// Function to check if the stack is empty
bool isEmpty(int top) { return top == -1; }

// Function to check if the stack is full
bool isFull(int top) { return top == MAX_SIZE - 1; }

int main() {
    int stack[MAX_SIZE];
    int topIndex = -1;

    push(stack, topIndex, 5);  // pushing element 5
    push(stack, topIndex, 10); // pushing element 10
    push(stack, topIndex, 15); // pushing element 15

    std::cout << "Top element of the stack: " << top(stack, topIndex) << "\n";

    pop(stack, topIndex); // popping an element

    std::cout << "Top element of the stack: " << top(stack, topIndex) << "\n";

    return 0;
}
```

### Implementation in Java

```java
import java.util.EmptyStackException;

public class CombinedStack {
    private int[] stackArray;
    private int top;
    private int maxSize;

    public CombinedStack(int maxSize) {
        this.maxSize = maxSize;
        stackArray = new int[maxSize];
        top = -1;
    }

    public void push(int value) {
        if (top == maxSize - 1) {
            throw new StackOverflowError("Stack is full");
        }
        top++;
        stackArray[top] = value;
    }

    public int pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        int value = stackArray[top];
        top--;
        return value;
    }

    public int peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return stackArray[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == maxSize - 1;
    }

    public static void main(String[] args) {
        CombinedStack stack = new CombinedStack(5);
        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Top element: " + stack.peek());

        int poppedElement = stack.pop();
        System.out.println("Popped element: " + poppedElement);

        System.out.println("Is stack empty? " + stack.isEmpty());
        System.out.println("Is stack full? " + stack.isFull());
    }
}
```

### Implementation in python

```py
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())

popped_element = stack.pop()
print("Popped element:", popped_element)

print("Is stack empty?", stack.is_empty())
print("Stack size:", stack.size())

```
