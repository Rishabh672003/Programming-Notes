## Buffered Channels

**Table of content :**

1. What arre buffered channels?
2. Closing the channel

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

---

### Closing the channel :

... to be continued
