# Queues

### Basic Definition

A queue is a linear data structure that allows operations to be performed in a
First In First Out (FIFO) order. This means that the element that is first
inserted into the queue is the first one to be removed. It can be visualized
as a line of people waiting for a service, where the person who arrives first
gets served first.

Adding items to the queue is known as **enqueue**, and removing items from the queue is known as **dequeue**.

### Why use Queues?

Queues are often used in scenarios where data doesn't need to be processed
immediately but in a FIFO order. For example, in disk scheduling, asynchronous
data transfer, semaphores, print spooling, or input device buffers.

### Working of Queues

In a queue, all additions are made at one end (known as the rear), and all
deletions are made at the other end (known as the front).

When implemented using an array, the queue uses two variables, 'front' and
'rear'. The 'front' variable points to the index where the first element is
stored, while the 'rear' variable points to the index where the last element is
stored.

## Implementations

### Implementation in C++

```cpp
#include <iostream>
#define SIZE 5

int items[SIZE];
int front = -1;
int rear = -1;

bool isFull() {
    if (front == 0 && rear == SIZE - 1) {
        return true;
    }
    return false;
}

bool isEmpty() {
    if (front == -1) {
        return true;
    }
    return false;
}

void enqueue(int element) {
    if (isFull()) {
        std::cout << "Queue is full\n";
    } else {
        if (front == -1)
            front = 0;
        rear++;
        items[rear] = element;
        std::cout << "Inserted " << element << "\n";
    }
}

int dequeue() {
    int element;
    if (isEmpty()) {
        std::cout << "Queue is empty\n";
        return (-1);
    } else {
        element = items[front];
        if (front >= rear) {
            front = -1;
            rear = -1;
        } /* Q has only one element, so we reset the
           queue after dequeing it. */
        else {
            front++;
        }
        std::cout << "Deleted -> " << element << "\n";

        return (element);
    }
}

void display() {
    /* Function to display status of Circular Queue */
    int i;
    if (isEmpty()) {
        std::cout << "Empty Queue" << std::endl;
    } else {
        std::cout << "Front -> " << front;
        std::cout << "Items -> ";
        for (i = front; i <= rear; i++)
            std::cout << items[i] << " ";
        std::cout << " Rear -> " << rear << std::endl;
    }
}

int main() {
    // Dequeuing an empty queue
    dequeue();

    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);

    // This fails to enqueue because the queue is full
    enqueue(6);

    display();
    dequeue();

    // Fails to dequeue because queue is empty
    dequeue();

    return 0;
}
```

### Implementation in Java

```java
public class Queue {
    private int maxSize;
    private int front;
    private int rear;
    private int currentSize;
    private int array[];

    public Queue(int size) {
        this.maxSize = size;
        front = 0;
        rear = -1;
        currentSize = 0;
        array = new int[maxSize];
    }

    public boolean isFull() {
        return (currentSize == maxSize);
    }

    public boolean isEmpty() {
        return (currentSize == 0);
    }

    public void enqueue(int item) {
        if (isFull()) {
            System.out.println("Queue is full!");
            return;
        }
        rear = (rear + 1) % maxSize;
        array[rear] = item;
        currentSize++;
        System.out.println("Added to queue" + item);
    }

    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return -1;
        }
        int temp = front;
        front = (front + 1) % maxSize;
        currentSize--;
        System.out.println("Removed from queue" + array[temp]);
        return array[temp];
    }

    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty!");
            return;
        }
        int temp = front;
        while (temp != rear) {
            System.out.println(array[temp]);
            temp = (temp + 1) % maxSize;
        }
        System.out.println(array[rear]);
    }

    public static void main(String[] args) {
        Queue queue = new Queue(5);
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);
        queue.dequeue();
        queue.enqueue(5);
        queue.display();
    }
}
```

### Implementation in python

```py
class Stack:
    def __init__(self):
        self.stack = []

    # Use list append method to add element
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use list pop method to remove an element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

# Initialize a stack object
MyStack = Stack()

# add elements to the stack
MyStack.add("Mon")
MyStack.add("Tue")

# print the stack contents
print(MyStack.stack)

# remove an element from the stack
print(MyStack.remove())
```
