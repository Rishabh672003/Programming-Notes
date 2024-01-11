package main

import (
	"fmt"
)

type Shape interface {
	area() float64
	perimeter() float64
}
type Rectangle struct {
	length  float64
	breadth float64
}

func (r Rectangle) area() float64 {
	return r.length * r.breadth
}

func (r Rectangle) perimeter() float64 {
	return 2*r.length + 2*r.breadth
}

func printdetails(s Shape) {
	fmt.Printf("Area : %f, Perimeter: %f", s.area(), s.perimeter())
}

func add(x, y int) int {
	return x + y
}

func mul(x, y int) int {
	return x * y
}

func aggregate(x, y, z int, arithmetic func(int, int) int) int {
	return arithmetic(arithmetic(x, y), z)
}

func addNums(nums ...int) int {
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
	}
	return sum
}

type User struct {
	name string
	age  int
}

// closure
func concattor() func(string) string {
	doc := ""
	return func(word string) string {
		doc += word + " "
		return doc
	}
}

func main() {

	rect := Rectangle{
		length:  10,
		breadth: 10,
	}

	printdetails(rect)

	fmt.Println()

	user := User{
		name: "Amit",
		age:  19,
	}
	fmt.Println(user)

	person := struct {
		name string
		age  int
	}{
		name: "Amit",
		age:  19,
	}
	fmt.Println(person)

	fmt.Println(aggregate(1, 2, 3, add))
	fmt.Println(aggregate(2, 3, 2, mul))

	array := [5]int{1, 2, 3, 4, 5}
	slice := array[1:4]
	fmt.Println(array)
	fmt.Println(slice)

	fmt.Printf("Length: %v", len(slice))
	fmt.Printf("\nCapacity: %v", cap(slice))

	total := addNums(slice...)
	fmt.Printf("\nSum of slice: %v", total)

	fmt.Println()

	words := []string{"Hii", "Hello", "nodejs", "python"}
	badWords := []string{"nodejs", "python"}
	for i, word := range words {
		for _, badWord := range badWords {
			if word == badWord {
				fmt.Printf("found bad word %v at index %d", badWord, i)
				fmt.Println()
			}
		}
	}

	// map
	ages := map[string]int{
		"Amit":    19,
		"Rishabh": 18,
	}
	ages["Sumit"] = 19  // inserting new element
	age := ages["Amit"] // getting a value with it's key
	fmt.Printf("Amit's age: %d", age)

	fmt.Println()

	makeFriends := concattor()

	fmt.Println("Map before sumit : ")
	for key, value := range ages {
		fmt.Println(key, value)
		makeFriends(key)
	}

	fmt.Println()

	fmt.Println(makeFriends("Harshil")) // prints Amit Rishabh Sumit Harshil

	fmt.Println()

	delete(ages, "Sumit") // deleting a value with it's key

	fmt.Println("Map after sumit : ")

	// printing the map as key value pair
	for key, value := range ages {
		fmt.Println(key, value)
	}
}
