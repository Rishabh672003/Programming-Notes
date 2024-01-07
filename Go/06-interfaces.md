## Interfaces in Go

**Table of Content :**

1. What are interfaces ?
2. Type assertions in Go.
3. Type Switch

---

### What are interfaces ?

In Go, interfaces are **collections of method signatures**. And any `type` (`struct`) that implements these methods adheres to that interface.

Interfaces are **implicitly implemented** on adhering types so we don't explicitly have to do any just. Any struct which implements all the methods from an interface adheres that interfce.

In the below example, interface `Shape` has methods `area()` and `perimeter()` which are later defined over `Rect` struct. Hence the struct `Rect` implements `Shape` by defining its own `area()` and `perimeter()` methods.

```go
package main
import (
    "fmt"
    "math"
)

// interface Shape with methods area & perimeter
type Shape interface {
	area() float64
	perimeter() float64
}
```

```go
// type Rectangle which implements area & perimeter methods
type Rect struct {
	width  float64
	height float64
}

func (r Rect) area() float64 {
	return r.width * r.height
}

func (r Rect) perimeter() float64 {
	return 2*r.height + 2*r.width
}

// type Circle which implements area & perimeter methods
type Circle struct {
	radius float64
}

func (c Circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c Circle) perimeter() float64 {
	return 2*math.Pi * c.radius
}
```

This `printDetails` fucntion takes in the `Shape` interface and prints down the area and permeter for any struct which implements `Shape` interface.

```go
func printDetails(s Shape) {
	fmt.Printf(
        "Area : %f Perimeter : %f",
        s.area(), s.perimeter()
    )
}
```

We can now create instances of these structs and can call the `printDetails` function for both the instances.

```go
func main() {
	rect := Rect{
		width:  10,
		height: 10,
	}
    circle := Circle{
        radius: 25,
    }
	printDetails(rect)
	printDetails(circle)
}
```

---

We can also have methods with named arguments and return type in interfaces which are more concise to their purpose.

```go
type Copier interface {
    Copy(srcFile string, destFile string) (bytesCopied int)
}
```

We can avoid naming them, these are just for readabilty purpose.

---

### Type assertions in Go

Whenever we need access to the underlying type of an interface, we can cast that interface to it's underlying type using type assertions.

```go
package main
import (
    "fmt"
    "math"
)
```

```go
type circle struct {
    radius float32
}

func (c circle) area() float32 {
    return math.Pi * c.radius * c.radius
}

type Imposter struct {
	side float64
}

func (i Imposter) area() float64 {
	return i.side * i.side
}
```

```go
type shape interface {
    area() float32
}

func getDetails (s Shape) {
    c, ok := s.(circle) // type assertion
    if ok {
        fmt.Printf(
            "Area of circle: %f",
            c.area()
        )
    } else {
		fmt.Println("unAuthorised shape")
	}
}
```

```go
func main() {
	circle := Circle { radius: 25 }
	imp := Imposter { side: 10 }
    printDetails(circle) // prints area
    printDetails(imp) // prints unauthorised shape
}
```

Inside `getDetails` function,

The assertion attempts to convert `s` (of type `Shape`) to a `circle` value. (checks if the provided `Shape` is specifically a `circle`.)

- If successful, `c` will hold the `circle` value, and `ok` will be `true`. And then, the area will be printed.

- If unsuccessful (e.g., `s` is a different shape type), `c` will be zero-valued, and `ok` will be `false`. And then, the else clause will be excuted.

A more experienced _Gopher_ will suggest to use a `type switch` instead of assertions because it's more handy and readable.

---

### Type Switch

A `type switch` in Go is a regualr switch statement, but case specify `types` (`structs`) instead of values.

```go
/* Syntax :
switch variable := interface.(type) {
case aType:
    methods on aType are accessible in this block within v
default :
    default case
}
*/
```

Rewriting above getDetails with type switch :

```go
func printDetails(s Shape) {
	switch v := s.(type) { // casting s to v
	case Circle:
		fmt.Printf("Area: %f \n", v.area())
	default:
		fmt.Println("Imposter!")
	}
}
```
