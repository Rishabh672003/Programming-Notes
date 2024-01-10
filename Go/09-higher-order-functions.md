## Higher order functions in Go

**Table of content :**

1. First Class and Curring functions
2. Defers

---

### First Class and Curring functions :

In Go, funtions can be can be passed around into any other function as a value just as we pass in variables.

- A function which accepts functions as an argument is called a **Higher order function**

- A function which returns a function is called a **Curried function**

Example :

```go
func add(x, y int) int {
	return x + y
}

func mul(x, y int) int {
	return x * y
}

// higher order function
func aggregate(x, y, z int, arithmetic func(int, int) int) int {
	return arithmetic(arithmetic(x, y), z)
}

// curried function
func selfMath(mathFunc (x, y int) int) func (int) int {
    return func (x int) int {
        return mathFunc(x, x)
    }
}
```

```go
func main(){
    fmt.Println(aggregate(1,2,3, add)) // prints 6
	fmt.Println(aggregate(2,3,2, mul)) // prints 12

    square := selfMath(mul)
    double := selfMath(add)

	fmt.Println(square(5)) // prints 25
	fmt.Println(double(5)) // prints 10

}
```

In the above example, we've two distinct `add` and `mul` function which takes two integers and returns their sum and product as integer.

The function `aggregate` takes (`x`, `y`, `z`) three integers, and a function `arithmetic` which again takes in two integers and returns an integer just as our `add` and `mul` functions. The `aggregate` function applies the given math function to the first 3 integers.

Hence `add` and `mul` functions can be passed as a value inside the `aggregate` function's call.

---

At first, it may seem like dynamically creating functions and passing them around as a variable adds unnecessary complexity. Most of the time we would be right. But there are some cases when functions as value makes sense. Some of these includes :

- HTTP API handlers
- Onclick callbacks
- Pub/Sub handlers

---

### Defers

... to be continued
