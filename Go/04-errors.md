## Errors in Go

**Table of content :**

1. Errors in Go are special
2. Handling errors
3. Early returns & Guard Clause

---

### Errors in Go are special

In Go, **errors are treated as values**, represented by the error interface.

This means they can be passed around, returned from functions, and assigned to variables like any other data type.

Go doesn't have exceptions; errors are handled explicitly using checks and returns.

Go comes with a standard library errors package to create basic error with the specified message.

```go
import "errors"
```

```go
errors.New("error message")
```

---

### Handling Errors:

**Returning Errors from Functions**: Functions typically return both a result and an error value. The caller is responsible for checking the error and handling it appropriately.

**`if err != nil` Checks**: The idiomatic way to check for errors is to use an if err != nil statement. If the error is not nil, it indicates an error occurred and should be handled.

---

### Early returns & Guard Clause

Go supports the ability to `return` early from a function. This is much powerful when used with **Guard Clauses**.

Guard clauses immediately return from a function if certain conditions aren't met, preventing unnecessary code execution and potential errors.

Example Code :

```go
package main

import (
	"errors"
	"fmt"
)

func isAdult(age int) (string, error) {
	if age < 18 {
		// guard clause
		return "", errors.New("you're inelegible")
	}
	status := "You are elegible"
	return status, nil
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
}
```
