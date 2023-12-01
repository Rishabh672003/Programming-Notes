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
           queue after dequeuing it. */
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
    int SIZE = 5;
    int items[] = new int[SIZE];
    int front, rear;

    Queue() {
        front = -1;
        rear = -1;
    }

    // check if the queue is full
    boolean isFull() {
        if (front == 0 && rear == SIZE - 1) {
            return true;
        }
        return false;
    }

    // check if the queue is empty
    boolean isEmpty() {
        if (front == -1)
            return true;
        else
            return false;
    }

    // insert elements to the queue
    void enqueue(int element) {
        if (isFull()) {
            System.out.println("Queue is full");
        }
        else {
            if (front == -1) {
                // mark front denote first element of queue
                front = 0;
            }
            rear++;
            // insert element at the rear
            items[rear] = element;
            System.out.println("Insert " + element);
        }
    }

    // delete element from the queue
    int dequeue() {
        int element;
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return (-1);
        } else {
            element = items[front];
            if (front >= rear) {
                front = -1;
                rear = -1;
            } else {
                front++;
            }
            System.out.println(element + " Deleted");
            return (element);
        }
    }

    void display() {
        if (isEmpty()) {
            System.out.println("Empty Queue");
        } else {
            System.out.println("Front index: " + front);
            System.out.println("Rear index: " + rear);
            System.out.println("Items in the queue: ");
            for (int i = front; i <= rear; i++) {
                System.out.print(items[i] + " ");
            }
        }
    }

    public static void main(String[] args) {
        Queue q = new Queue();

        // deQueue is not possible on empty queue
        q.dequeue();

        // enQueue 5 elements
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);
        q.enqueue(5);

        // 6th element can't be added to queue because queue is full
        q.enqueue(6);

        q.display();

        // deQueue removes element entered first
        q.dequeue();

        q.display();
    }
}
```

### Implementation in python

```py
class Queue:
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(self.queue)
```

### Real-life examples of queues (because our sir loves those)

1. Ticket lines: Queues are often used to manage ticket lines, such as at a
   movie theater or a sporting event. The first person in line gets the first
   ticket, and so on.

2. Print spoolers: Print spoolers use queues to manage print jobs. When a user
   sends a print job to a printer, it is placed in the print queue. The print
   jobs are then processed in the order in which they were received.

3. Message queues: Message queues are used to send and receive messages between
   different processes. Messages are placed in a queue, and then they are
   processed by the processes in the order in which they were received.

4. Traffic lights: Traffic lights use queues to control the flow of traffic.
   Cars are placed in a queue, and then they are allowed to pass through the
   intersection one at a time.

5. Operating systems: Operating systems often use queues to manage resources,
   such as CPU time and memory. Processes are placed in a queue, and then they
   are allocated resources in the order in which they were received.

6. Web servers: Web servers often use queues to manage requests from web
   browsers. Requests are placed in a queue, and then they are processed by the
   web server in the order in which they were received.
