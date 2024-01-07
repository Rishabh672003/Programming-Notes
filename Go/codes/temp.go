package main

import (
	"fmt"
	"math"
)

type Shape interface {
	area() float64
}
type Circle struct {
	radius float64
}

type Squ struct {
	side float64
}

func (c Circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (s Squ) area() float64 {
	return s.side * s.side
}

func printDetails(s Shape) {
	switch v := s.(type) {
	case Circle:
		fmt.Printf("Area: %f \n", v.area())
	default:
		fmt.Println("Imposter!")
	}
}

func main() {
	var radius float64
	fmt.Print("Enter Radius: ")
	fmt.Scanf("%f", &radius)
	circle := Circle{
		radius: radius,
	}
	squ := Squ{
		side: 10,
	}
	printDetails(circle)
	printDetails(squ)
}
