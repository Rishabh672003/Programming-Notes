## Blockings and Deadlocks

A deadlock happens when a group of goroutines are all blocking, so none of them can continue. This is a common bug that we need to watch out for in concurrent programming.

```go
func main(){
   	c1 := make(chan int)

	fmt.Println("push into channel")
	c1 <- 10

	go func() {
		g1 := <-c1
		fmt.Println("get g1: ", g1)
	}()
}
```

```bash
push into channel
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
        /home/amit/Documents/Programming-Notes/Go/codes/temp.go:23 +0x16b
exit status 2
```

The above code results a deadlock because we are attempting to send a value to the channel `c1` in the `main` goroutine without any other goroutine ready to receive the value.

The channel operation `<-c1` in the goroutine is expecting to receive a value before proceeding, and since there is no other goroutine ready to send, it leads to a deadlock.

Correct Code :

```go
func main(){
   	c1 := make(chan int)

    fmt.Println("push into channel")
	go func() {
		g1 := <-c1
	}()

	c1 <- 69
	fmt.Println("got g1: ", g1)
}
```

In this corrected version:

- The goroutine is started before attempting to send a value to the channel.
- The value 10 is sent to the channel inside the main goroutine.

---

... to be continued
