package main

import (
	"fmt"
)

func main() {
	array := [5]int{1, 2, 3, 4, 5}
	slice := array[1:4]
	fmt.Println(array)
	fmt.Println(slice)

	fmt.Printf("Length: %v", len(slice))
	fmt.Printf("\nCapacity: %v", cap(slice))
}
