package main

import (
	"fmt"
	"time"
)

func getUserId(id chan<- int) {
	time.Sleep(time.Second)
	id <- 69
}

func getUserById(id int) string {
	if id == 69 {
		return "Amit"
	}
	return "user not found"
}

func main() {
	idChannel := make(chan int)
	go getUserId(idChannel)

	fmt.Println("fetching user id...")
	userId := <-idChannel

	fmt.Println("fetching User by id:", userId)
	user := getUserById(userId)

	fmt.Println("User: ", user)
}

/*
- flow of execution :
1. main function runs,
2. idChannel gets spawned,
3. a new goroutine named getUserId is launched concurrently with main goroutine,
4. getUserId goroutine gets blocked for a second, but the main goroutine still runs,
5. after a second, getUserId gouroutne sends 69 into the idChannel,
6. Meanwhile, the main goroutine prints the message "fetching user id..." to the console,
7. The main goroutine then receives the value from the idChannel channel using userId := <-idChannel.
8. The getUserById function checks if the user ID is 69 and returns,
9. The main goroutine prints the retrieved user information to the console,
10. The execution completes.
*/
