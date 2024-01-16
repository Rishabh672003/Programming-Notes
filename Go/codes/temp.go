package main

import (
	"fmt"
	"time"
)

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

func fibonacci(n int) int {
	x, y := 0, 1
	total := 0
	for i := 0; i < n; i++ {
		total += x
		x, y = y, x+y
	}
	return total
}

func splitAnySlice[T any](s []T) ([]T, []T) {
	mid := len(s) / 2
	return s[:mid], s[mid:]
}

func main() {

	firstInts, secondInts := splitAnySlice([]int{0, 1, 2, 3})
	fmt.Println(firstInts, secondInts)

	fmt.Println("Buffered Channels: ")
	test("Hello John, tell Kathy I said hi", "Whazzup bruther")
	test("I find that hard to believe.", "When? I don't know if I can", "What time are you thinking?")
	test("She says hi!", "Yeah its tomorrow. So we're good.", "Cool see you then!", "Bye!")
	fmt.Println()

	fib := fibonacci(69)
	fmt.Print(fib)

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
