## Go Concurrency

**Table of content :**

1. What is concurrecy?
2. Concurrency in Go.
3. Goroutines
4. Channels
5. Blockings and Deadlocks

---

### What is concurrecy?

Concurrency is the ability to perform multiple tasks at same time.

Typically our code is executed one line at a time, one after the other. This is called as **sequential / synchronous programming.**

If the computer we're using has a single [cores](https://www.computerhope.com/jargon/c/core.htm), the execution of code occurs in a sequential manner.

In a single-core system, the processor can only handle one instruction at a time.

This means that even if multiple tasks are running, they have to share the processing time, and the CPU switches between them rapidly, giving the illusion of parallel execution.

In contrast, when a computer has multiple cores, each core can execute its set of instructions independently. This is called as **concurrent / asynchronous programming**.

This enables true parallelism, allowing multiple tasks to be performed simultaneously. Each core can work on a different [thread](https://www.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/4_Threads.html) or task, leading to potentially faster and more efficient processing.

The below picture makes it more clear:

![go-concurrency](https://github.com/amitsuthar69/assets/blob/main/Go/go-concurrency.png?raw=true)

---

### Concurrency in Go.

**Go was designed to be concurrent**, which is a trait fairly unique to Go. It excels at performing many tasks simultaneously & safely using a simple syntax.

There isn't a popular programming language in existence where spawning concurrent execution is quiet as elegent, atleast in my opinion.

Concurrency is as simple as using a `go` keyword when calling a function.

```go
go doSomething()
```

In the example above, `doSomething()` will be executed concurrently with the rest of the code in the function. The Go keyword is used to spawn a new **goroutine**.

---

### Goroutines

A goroutine is unique to Go programming language, a goroutine is a lightweight, **concurrent thread of execution**. Goroutines are part of Go's approach to concurrent programming. They are similar to threads, but they are managed by the Go runtime and are more lightweight compared to traditional threads.

Any funtion called with the `go` keyword spwans a new goroutine.

So whenever we use the `go` keyword, the execution kind of immediately jumps to the next step after the function call. So that `doSomething()` function will go be executed in parallel and then exectution continues from the next line.

---

Example :

```go
package main

import (
	"fmt"
	"time"
)

func sendEmail(message string) {
	go func() { // goroutine
		time.Sleep(time.Millisecond * 250) // wait for 250 ms
		fmt.Printf("Email received: '%s'\n", message)
	}()
	fmt.Printf("Email sent: '%s'\n", message)
}

func test(message string) {
	sendEmail(message)
	time.Sleep(time.Millisecond * 500)
	fmt.Println("-------------------")
}

func main() {
	test("Hello there Amit!")
	test("Hi there Rishabh!")
	test("Hey there Sumit!")
}
```

In the above code, the anonymous function `go func(){...}()` is a goroutine which generates a fake delay for 250 ms before the "Email received ..." line get's printed. With this `go` keyword, we create a new goroutine for this function and a new thread of execution is alloted to it.

But, this goroutine **can never return a value if used like this**. The reason for this is that **the `go` keyword starts the goroutine and immediately proceeds to the next line of code without waiting for the goroutine to finish. As a result, there's no straightforward way to retrieve the return value**.

If we need to retrieve a value from a goroutine, we typically use **channels** to do so.

---

### Channels

Channels are typed, thread-safe queues. Channels allow different goroutines to communicate with each other.

![image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*qj8m4H2qYuIovlL1BOFnEg.png)

**Sending to a channel blocks until another goroutine receives from that channel**, and vice versa. This blocking behavior helps in synchronization between goroutines.

A sender can close a channel to indicate that no more values will be sent.
Receivers can use a special syntax to detect whether a channel has been closed.

1. Creating a Channel :

Just like maps and slices, channels must be cread before use. They also use the `make()` keyword along with the `chan` keyword.

```go
myChannel := make(chan int)
```

2. Send data to a channel :

```go
ch <- 69
```

The `<-` keyword is called the `channel operator`. Data flows in the direction of arrow. This operation will block until another goroutine is ready to receive the value.

3. Receive data from a channel :

```go
v := <- ch
```

This reads and removes the value from the channel and assigns it to the variable `v`.

Small example :

```go
func main(){
    c1 := make(chan int) // create the channel

	fmt.Println("push into channel")
	go func() {
		c1 <- 69 // send value to the channel
	}()

	g1 := <-c1 // receive value from the channel
	fmt.Println("get g1:", g1)
}
```

---

Another Example :

```go
package main
import (
	"fmt"
	"time"
)

// function that takes in an int channel
func getResult(resultChan chan<- int) {
	time.Sleep(time.Second) // Simulating some work
	resultChan <- 42 // passing 42 through this channel
}

func main() {
	resultChannel := make(chan int) // making a channel
	go getResult(resultChannel) // calling a goroutine
	result := <-resultChannel // assigning the value received from channel
	fmt.Println(result) // prints 42
}
```

In the above code, there are **two** goroutines:

- **The main goroutine, which is the default goroutine that gets executed when a Go program starts. This is the goroutine that executes the main function.**

- **The goroutine created by the go statement inside the main function when calling `getResult(resultChannel)`.**

The `getResult` function is executed concurrently in the second goroutine, simulating some work and passing the value 42 through the channel.