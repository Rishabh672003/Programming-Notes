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
        await task();
      } catch (error) {
        console.log("Error in processing task", error);
      }
    }
    this.isProcessing = false;
  }
}

const asyncQueue = new AsyncTaskQueue();

const task1 = async () => {
  console.log("Task 1 queued");
  await new Promise((resolve) => setTimeout(resolve, 1000));
  console.log("Task 1 ended");
};

const task2 = async () => {
  console.log("Task 2 queued");
  await new Promise((resolve) => setTimeout(resolve, 500));
  console.log("Task 2 ended");
};

// asyncQueue.enqueue(task1);
// asyncQueue.enqueue(task2);

/* 
Here is a version of the async queue whihc is quite efficient and introduces the concept of concurrency control 
by limiting the number of "workers" (i.e., concurrent tasks) that can be processed at any given time.
*/

function createQueue(tasks, maxNumOfWorkers = 4) {
  var activeWorkers = 0; // Track how many tasks are currently being worked on
  var taskIndex = 0; // Track the index of the next task to execute

  return new Promise((done) => {
    const handleResult = (index) => (result) => {
      tasks[index] = result; // Store the result of the task back in the array at the correct index
      activeWorkers--; // Decrement the number of active workers
      getNextTask(); // Try to process the next task
    };

    const getNextTask = () => {
      // Check if we can start a new task (if there's room for more workers)
      if (activeWorkers < maxNumOfWorkers && taskIndex < tasks.length) {
        // Execute the next task and handle its result
        tasks[taskIndex]()
          .then(handleResult(taskIndex))
          .catch(handleResult(taskIndex));

        taskIndex++; // Move to the next task in the queue
        activeWorkers++; // Increment the number of active workers
        getNextTask(); // Recursively call getNextTask to fill up the worker slots
      }
      // Check if all tasks have been processed and all workers are done
      else if (activeWorkers === 0 && taskIndex === tasks.length) {
        // All tasks completed, resolve the main promise
        done(tasks);
      }
    };
    getNextTask(); // Start processing tasks
  });
}

const tasks = [
  () =>
    new Promise((resolve) =>
      setTimeout(() => resolve("Task 1 complete"), 1000)
    ),
  () =>
    new Promise((resolve) => setTimeout(() => resolve("Task 2 complete"), 500)),
  () =>
    new Promise((resolve) =>
      setTimeout(() => resolve("Task 3 complete"), 2000)
    ),
  () =>
    new Promise((resolve) => setTimeout(() => resolve("Task 4 complete"), 800)),
  () =>
    new Promise((resolve) =>
      setTimeout(() => resolve("Task 5 complete"), 1200)
    ),
  () =>
    new Promise((resolve) =>
      setTimeout(() => resolve("Task 6 complete"), 2000)
    ),
  () =>
    new Promise((resolve) =>
      setTimeout(() => resolve("Task 7 complete"), 3000)
    ),
  () =>
    new Promise((resolve) =>
      setTimeout(() => resolve("Task 8 complete"), 1000)
    ),
];

createQueue(tasks, 3).then((results) => {
  console.log("All tasks completed");
  console.log("Results:", results);
});

// const task1 = async () => {
//   console.log("Task 1 queued");
//   await new Promise((resolve) => setTimeout(resolve, 1000)).then(() =>
//     console.log("Task 1 ended")
//   );
// };

// const task2 = async () => {
//   console.log("Task 2 queued");
//   await new Promise((resolve) => setTimeout(resolve, 500)).then(() =>
//     console.log("Task 2 ended")
//   );
// };

// const task1 = async () => {
//   console.log("Task 1 queued");
//   await new Promise((resolve) => setTimeout(resolve("Task 1 ended"), 1000));
// };

// const task2 = async () => {
//   console.log("Task 2 queued");
//   await new Promise((resolve) => setTimeout(resolve("Task 2 ended"), 500));
// };
