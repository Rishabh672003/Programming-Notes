package main

import (
	"errors"
	"fmt"
)

type Message struct {
	sender   string
	receiver string
}

type person struct {
	name string
	age  int
}

type user struct {
	person
	isVerified bool
}

type Rect struct {
	width  int
	height int
}

func (r Rect) area() int {
	return r.width * r.height
}

func sendMessage(m Message) {
	fmt.Printf("Message sent by %s to %s", m.sender, m.receiver)
}

func main() {
	var age int
	fmt.Print("Enter your age: ")
	fmt.Scanf("%d", &age)
	message, err := isAdult(age)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(message)
	}
	msg := Message{"Amit", "Rizzabh"}
	sendMessage(msg)

	fmt.Println()

	user1 := user{
		person: person{
			name: "Amit",
			age:  19,
		},
		isVerified: true,
	}
	fmt.Println(user1.name)

	rect := Rect{
		width:  10,
		height: 10,
	}
	fmt.Println(rect.area())
}

func isAdult(age int) (string, error) {
	if age < 18 {
		return "", errors.New("you're not an elegible")
	}
	status := "You are elegible"
	return status, nil
}
