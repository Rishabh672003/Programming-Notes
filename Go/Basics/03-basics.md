## Go Basics

**Table of content :**

1. Console I/O
2. Variables
3. Type Casting
4. String Formatting
5. if-else and for loop
6. functions
7. Variadic functions

---

### Console I/O

```go
var age int
fmt.Print("Enter your age: ")
fmt.Scanf("%d", &age) // reading input
fmt.Println("You are", age, "years old.")
```

---

### Variables

```go
var age int = 18 // mutable
const name = "amit" // immutable
```

- Constants in Go are not explicitly typed.
- The compiler automatically infers the type of a constant based on its value.

---

### Type Casting

```go
accountAge := 2.6
accountAgeInt := int(accountAge)

temperatureInt := 32
temperatureFloat := float64(temperatureInt)
```

---

### String Formatting

1. `Printf()`: Prints the formatted string in console.
2. `Sprintf()`: Returns the formatted string as a value.

**String formatting verbs (placeholders) :**

- `%v`: Default format, prints the value in a suitable format based on its type. (General Verb)
- `%T`: Prints the type of the value.
- `%%`: Prints a literal percent sign (%).
- `%s`: String
- `%d`: Integer (base 10)
- `%f`: Floating-point number (decimal notation)
- `%c`: Character

```go
const name = "Amit"
const age = "19"

bio := fmt.Sprintf(
    "Hi, I'm %s and I'm %d years old",
    name,
    age
)

fmt.Println(bio)
```

---

### if-else, else if

```go
if 1 > 0 {
	fmt.Println("1 > 0")
} else {
    fmt.Println("0")
}
```

As we skip parenthesis, we can now have the abilty to declare a variable within the `if` scope. (Just a Go syntactic sugar, we can avoid this if we want)

```go
// normal if statement
length := getLength(email)
if length < 1 {
    fmt.Println("Invalid Email")
}

// if STATEMENT; CONDITION {...}
if length := getLength(email); length < 1 {
    fmt.Println("Invalid Email")
}
```

Not only the modified code is short, it also removes the length from parent scope, because we don't actually need it there.

---

### for loop

```go
for i := 3; i > 0; i-- {
    fmt.Println(i, " ")
}
```

**the `:=` operator is a shortcut for declaring and initializing a variable in one line (Go uses the value on the right to determine the variable's type).**

**When we use the `:=` operator, the Go compiler infers the variable's type automatically based on the value you assign to it.**

Taking the long way, you might have written this as:

```go
var i int;
for i = 3; i > 0; i-- {
    fmt.Println(i, " ")
}
```

For loops in Go are quite unique because, unlike other languages, we can skip statements of loop signature.

```go
for INITIAL; ;AFTER {
    // do something
}
```

Due to this ability, there are **no while loops** in Go.

We can just use a for loop by skipping the initialization and incremental part and keeping the conditional part.

```go
for CONDITION {
    // a while loop, runs untill CONDITION is no longer true
    // make sure you handle the loop braking logic
}
```

---

### functions

```go
// func FuncName(param paramType) returnType {...}

func Hello(name string) string {
	message := fmt.Sprintf("Hi, %v. Welcome!", name)
	return message
}

func Add(a int, b int) int {
	return a + b
}

/* multiple arguments of same type can have a single type
defination in the end, assuming that they are in order
*/
func Sub(a, b int) int {
	return a + b
}
```

**Functions in Go can return multiple values**

```go
func main(){
    firstName, lastName := getName()
}

func getName() (string, string) {
    return "amit", "suthar"
}
```

We can also explicitly ignore one of the returned value from such types of function by using a underscore `_`. The compiler completely ignores this underscore.

```go
func main(){
    firstName, _ := getName()
}
```

Also, remember that return statements without arguments returns the named return value.

Which means,

```go
func getCords() (x, y int) {
    // x and y are initialized with zero values
    return // automatically returns x and y
}
```

is same as :

```go
func getCords() (int, int){
    var x int
    var y int
    return x, y
}
```

---

### Calling Functions

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello Jan 6")

	fmt.Println(Hello("Amit")) // calling Hello
	fmt.Println(Add(2, 3)) // calling Add
	fmt.Println(Add(4, 3)) // calling Sub
}
```

### Variadic functions (variable arguments)

Variadic function in Go are funtions with variable number of argumets as [slices](https://github.com/amitsuthar69/Programming-Notes/blob/main/Go/07-arrays-slices.md).

While this concept is more similar to Python's `args`, the syntax is more similar to javascript's `...spread` operator.

```go
func addNums(nums ...int) int {
    sum := 0
    for i := 0; i < len(nums); i++ {
        sum += nums[i]
    }
    return sum
}
```

```go
func main(){
    slice := []int{1, 2, 3, 4, 5}
    total  := addNums(slice...)
    fmt.Println(total) // prints 15
}
```

You would've noticed 3 strange things here!

1. the `nums` in function signature is treated as a slice, hence we can leverage the `len` and underlying index of `nums`.

2. `...int` is a type spread operator which assigns type `int` to each slice element and expects the function call to be injected with all the slice elements.

3. `slice...` populates the function call with all the slice element which is the expected behaviour.

The familiar `fmt.Println()` and `fmt.Sprintf()` are variadic!
`fmt.Println()` prints each element with space delimiters and a newline at the end.

```go
func Println(a ...interface{}) (n int, err error) {}
```
