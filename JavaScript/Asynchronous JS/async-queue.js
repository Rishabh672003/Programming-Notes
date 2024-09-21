/* Async Task Queue :
An async queue in JavaScript is a data structure designed to manage async tasks (functions that return promises) in a controlled manner. 
It ensures that these tasks are processed one at a time, or in batches, while respecting their async nature. 
This is useful when you need to limit the number of tasks running concurrently or when tasks must be processed in a specific order.

- Enqueue: Add an async task to the queue.
- Dequeue: Start processing a task from the queue.
- Concurrency Control: Optionally, you can control the number of tasks that run at the same time. 
  For example, a concurrency of 1 means tasks are processed one by one.
- Task Completion: Once a task finishes, the next task in the queue is processed.
- Error Handling: Proper handling of errors to ensure they don’t block the queue from processing the remaining tasks.
*/

// -------------------------------------------------------------------------------------------------------------------------------------------------- //

/* 
steps to create a simple async task queue, processing a task one at a time :

1. create a queue and a flag to check if any task in under process.
2. create an enqueue function which will :
  - accept a task and push it into the queue.
  - call the processQueue function to process that pushed task.
3. processQueue function :
  - check if a task is already under process, (the flag)
  - if true, return immediately; else :
    - set the flag to true,
    - while the queue doesn't get empty : 
      - dequeue the task from the queue,
      - execute the task (await the call to task()) and handle promise rejection error.
    - set the flag to false
*/

class AsyncTaskQueue {
  constructor() {
    this.queue = [];
    this.isProcessing = false;
  }

  enqueue(task) {
    this.queue.push(task);
    this.processQueue();
  }

  async processQueue() {
    if (this.isProcessing) return;
    this.isProcessing = true;

    while (this.queue.length > 0) {
      const task = this.queue.shift();
      try {
        await task(); // here awaiting the task is important as we wait untill it's done i.e blocking the execution of other tasks
      } catch (error) {
        console.log("Error in processing task", error);
      }
    }
    this.isProcessing = false;
  }
}

const asyncQueue = new AsyncTaskQueue();

const task = async (id) => {
  console.log(`Task ${id} queued`);
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/todos/${id}`
  );
  const data = await response.json();
  console.log({ id: data.id, title: data.title });
  console.log(`Task ${id} ended`);
};

for (let i = 1; i <= 10; i++) {
  asyncQueue.enqueue(() => task(i));
}

/* 
Here is a version of the async queue which is quite efficient and introduces the concept of concurrency control 
by limiting the number of "workers" (i.e., concurrent tasks) that can be processed at any given time.
*/

class RateLimitedQueue {
  constructor(maxRequests) {
    this.maxRequests = maxRequests;
    this.queue = [];
    this.activeTasks = 0;
  }

  enqueue(task) {
    this.queue.push(task);
    this.processQueue();
  }

  async processQueue() {
    if (this.activeTasks >= this.maxRequests) return; // Ensuring rate limit is respected

    while (this.activeTasks < this.maxRequests && this.queue.length > 0) {
      const task = this.queue.shift(); // Get the next task in the queue
      this.activeTasks++;

      // Process the task
      task()
        .then((result) => {
          console.log(result); // process the result
        })
        .catch((error) => {
          console.error("Task failed:", error);
        })
        .finally(() => {
          this.activeTasks--; // Mark task as completed
          this.processQueue(); // Continue processing the queue
        });
    }

    // Wait 1 second before processing the next batch of requests
    if (this.queue.length > 0) {
      setTimeout(() => {
        this.processQueue();
      }, 1000);
      // the 1000 ensures that no more than maxRequests tasks are processed every second.
    }
  }
}

/*
The hardcoded wait (setTimeout) of 1000 is there to simulate rate limiting
and ensure you don’t overwhelm a system that has constraints (e.g., API rate limits).
If you don’t need rate limiting, you can remove the wait
and let the tasks be processed as fast as possible, up to your concurrency limit (maxNumOfWorkers).
*/

const makeApiRequest = (id) => {
  return () =>
    fetch(`https://jsonplaceholder.typicode.com/todos/${id}`)
      .then((response) => response.json())
      .then((data) => {
        // console.log(`Request ${id} complete`, data);
        return { id: data.id, title: data.title };
      });
};

const rateLimitedQueue = new RateLimitedQueue(3); // Limit to 3 API requests per second

// enqueuing 20 tasks to fetch data from the API
for (let i = 10; i <= 20; i++) {
  rateLimitedQueue.enqueue(makeApiRequest(i));
}
