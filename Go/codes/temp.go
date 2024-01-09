package main

import (
	"fmt"
)

func addNums(nums ...int) int {
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
	}
	return sum
}

func main() {
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

	fmt.Println("Map before sumit : ")
	for key, value := range ages {
		fmt.Println(key, value)
	}

	fmt.Println()

	delete(ages, "Sumit") // deleting a value with it's key

	fmt.Println("Map after sumit : ")

	// printing the map as key value pair
	for key, value := range ages {
		fmt.Println(key, value)
	}
}
