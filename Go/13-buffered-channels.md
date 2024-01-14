## Buffered Channels

**Table of content :**

1. What arre buffered channels?
2. Closing the channel
3. Looping over buffered channels.
4. Select-Case Statement for buffered channels.
5. Tickers

---

What arre buffered channels?

Buffered channels in Go are channels with a **specified capacity.**

Unlike unbuffered channels, which require both the sender and receiver to be ready to communicate at the same time, buffered channels allow a certain number of values to be stored in the channel before the receiver is ready to receive them.

![Buffered channels](https://github.com/amitsuthar69/assets/blob/main/Go/buffered-channels-go.png?raw=true)

---

### Features of buffered channels :

**1. Capacity :**

- A buffered channel has a specified capacity, which determines the number of values it can hold at a given time. The buffer length is passed as a secong argument in `make()` function.

- Example:

```go
ch := make(chan int, 3) // creates a buffered channel with capacity of 3.
```

**2. Non-blocking Send :**

- In a buffered channel, a sender can continue sending values until the channel is full (reaches its capacity).

- This means that the send operation does not block until the channel is full.

- Once the channel is full, further sends will block until the receiver has received some values and made room in the channel.

**3. Decoupling sender and receiver :**

- Buffered channels allow for some decoupling between the sender and receiver in terms of synchronization.

- If the sender and receiver are not perfectly synchronized in time, buffered channels provide a way for them to proceed independently up to the capacity limit.

**4. Mitigating Blocking Issues:**

- In certain scenarios, using buffered channels can help prevent deadlocks caused by blocking when a sender and receiver are not perfectly synchronized.

- Buffered channels provide a temporary storage for values, allowing one side to proceed even if the other is not immediately ready.

Complete Example :

```go
package main
import "fmt"

func addEmailsToQueue(emails []string) chan string {
	emailsToSend := make(chan string, len(emails))
	for _, email := range emails {
		emailsToSend <- email
	}
	return emailsToSend
}

func sendEmails(batchSize int, ch chan string) {
	for i := 0; i < batchSize; i++ {
		email := <-ch
		fmt.Println("Sending email:", email)
	}
}

func test(emails ...string) {
	fmt.Printf("Adding %v emails to queue...\n", len(emails))

	ch := addEmailsToQueue(emails)

	fmt.Println("Sending emails...")
	sendEmails(len(emails), ch)
	fmt.Println("--------------------------")
}

func main() {
	fmt.Println("Buffered Channels: ")
	test("Hello John, tell Kathy I said hi", "Whazzup bruther")
}
```

---

### Closing the channel :

Channels can be explicitly closed in Go **by a sender**.

```go
ch := make(chan int)

// ... do something

close(ch) // closing the "ch" channel.
```

We can also check if a channel is closed or not :

```go
v, ok := <- ch
```

`ok` is false if channel is empty and closed.

Never send on a closed channel, it'll cause panic. A panic on the main goroutine will cuase the entire progarm to crash and on any other gorotine will cause that goroutine to crash.

Closing channels isn't necessary, it's okay if we kept the channel open, the garbage collect will look for it.

---

### Looping over buffered channels.

Similar to slices and maps, channels can be ranged overr.

```go
for item := range ch {
    // item is the next value being received from the channel.
}
```

This example will recive values over the channel (blocking at each iteration if nothing new is there) and will exit when the channel is closed.

Example :

```go
package main
import (
	"fmt"
	"time"
)

func concurrrentFib(n int) {
	ch := make(chan int)
	go fibonacci(n, ch)

    // take all number from channel and print them.
	for v := range ch {
		fmt.Println(v)
	}
}

func fibonacci(n int, ch chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		ch <- x
		x, y = y, x+y
		time.Sleep(time.Millisecond * 10)
	}
	close(ch)
}

func test(n int) {
	fmt.Printf("Printing %v numbers...\n", n)
	concurrrentFib(n)
	fmt.Println("--------------------------")
}

func main() {
	test(10)
	test(5)
	test(20)
	test(13)
}

/* i know caluclating fibonacci doesn't have to do anything with channels
but this is just for the sake of explanation, cope with it.
*/
```

---

### Select-Case Statement for buffered channels.

Sometimes we have a single goroutine listening to multiple channels and want to process data in the order it comes through each channel.

A `select` statement is used to listen to multiple channels at the same time. It is similar to a `switch` statement **but for channels**.

```go
select {
  case i, ok := <- chInts:
    fmt.Println(i)
  case s, ok := <- chStrings:
    fmt.Println(s)
}
```

- The first channel with a value ready to be received will fire and its body will execute. If multiple channels are **ready at the same time one is chosen randomly**.

- The `ok` variable in the example above refers to whether or not the channel has been closed by the sender yet.

Example :

```go
func logMessages(chEmail, chSms chan string){
    for {
        select {
        case email, ok := <- chEmail:
            if !ok { return }
            fmt.Println(email)
        case sms, ok := <- chSms:
            if !ok { return }
            fmt.Println(sms)
        }
    }
}
```

**Select deault case :**

The `default` case in a `select` statement executes immediately if no other channel has a value ready. A `default` case stops the `select` statement from blocking.

```go
select {
    case v, ok := <-ch:
        // do smthn with v
    default:
        // receiving from ch would block
        // so do something else
}
```

---

### Tickers

In Go, a `Ticker` is a built-in type provided by the `time` package. It represents a ticker that sends time values (year, month, day, hour, minute, second, and nanosecond) on a channel at regular intervals.

A Ticker is useful when you need to perform an action repeatedly at fixed intervals.

- `time.Tick()` is a standard library function that returns a channel that sends a value on a given interval.

- `time.After()` sends a value once after the duration has passed.

- `time.Sleep()` blocks the current goroutine for the specified amount of time.

```go
func main(){
    ticker := time.NewTicker(1000 * time.Millisecond)
	go func() {
		<-ticker.C
		fmt.Println("Tick at", time.Now())
	}()

	// Allow the ticker to run for 3 seconds
	time.Sleep(3 * time.Second)

	// Stop the ticker after 3 seconds
	ticker.Stop()
	fmt.Println("Ticker stopped")
}
```

In this example:

- We create a Ticker using `time.NewTicker`, specifying the interval between ticks (500 milliseconds in this case).

- An anonymous goroutine is launched to perform actions at each tick. The `<-ticker.C` channel receives values at each tick.

- The program then sleeps for 3 seconds to allow the ticker to run.

- After 3 seconds, the `Stop` method is called on the Ticker to stop the ticking.

- The program prints "Ticker stopped" to indicate that the ticker has been stopped.

This is a simple use case, but Ticker is often employed in scenarios where periodic actions need to be performed, such as **polling for updates, checking for changes, or triggering regular maintenance tasks**.
