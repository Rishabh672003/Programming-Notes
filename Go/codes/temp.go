package main

import (
	"fmt"
	"time"
)

func getResult(resultChan chan<- int) {
	time.Sleep(time.Second) // Simulating some work
	resultChan <- 42
}

func main() {
	fmt.Println("goroutines")
	resultChannel := make(chan int)
	go getResult(resultChannel)
	result := <-resultChannel
	fmt.Println(result)

	c1 := make(chan int)

	fmt.Println("push 69 into channel")
	go func() {
		c1 <- 69
	}()

	g1 := <-c1
	fmt.Println("Got from channel: ", g1)
}
