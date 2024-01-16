## Errors in Go

**Table of content :**

1. Errors in Go are special
2. Early returns & Guard Clause
3. Handling errors
4. Custom Errors
5. Go error package

---

### Errors in Go are special

In Go, **errors are treated as values**, represented by the error interface.

```go
type error interface {
	Error() string
}
```

So an error is a string which states what went wrong or it's nothing (`nil`).

This means errors can be passed around, returned from functions, and assigned to variables like any other data type.

Go doesn't have exceptions; errors are handled explicitly using checks and returns.

---

### Early returns & Guard Clause

Go supports the ability to `return` early from a function. This is much powerful when used with **Guard Clauses**.

Guard clauses immediately return from a function if certain conditions aren't met, preventing unnecessary code execution and potential errors.

We'll look upto Guard clauses later ont this doc.

---

### Handling Errors:

**Returning Errors from Functions**: Functions typically return both a result and an error value. The caller is responsible for checking the error and handling it appropriately.

**`if err != nil` Checks**: The idiomatic way to check for errors is to use an if err != nil statement. If the error is not nil, it indicates an error occurred and should be handled.

```go
// strconv.Atoi() func converts a stringified number to integer
int, err := strconv.Atoi("42b")
if err != nil {
	fmt.Printf("Cannot convert: ", err)
	/*
	because 42b isn't a valid integer, we print:
	Cannot convert: strconv.Atoi: parsing "42b: invalid string
	*/
	return
}
// if we get here, int was sucessfully converted
```

These err checks called as Guard clauses.

---

Example :

```go
package main
import (
	"fmt"
)

func getUser() (User, error) {
	// user logic, Early returns & Guard Clause
}

func getUserProfile(id string) (User, error) {
	// user logic, Early returns & Guard Clause
}

func main() {
	user, err := getUser()
	if err != nil {
		fmt.Println("Error fetching user")
		return
	}
	// if fetching user was successful,
	userProfile, err := getUserProfile(user.ID)
	if err != nil {
		fmt.Println("Error fetching user")
		return
	}
	// if fetching user was successful, further code ...
}
```

As errors are interfaces, we can create our own custom errors.

---

### Custom Error

```go
type userError struct {
	name string
}

func (e userError) Error() string {
	return fmt.Sprintf(
		"%v has problem with their account",
		 e.name,
	)
}
```

And we can use this `userError` interface as :

```go
func sendSMS(msg, userName string) error {
	if !canSendSMS(userName) {
		return userError{ name: userName }
	}
	// ...
}
```

But as we can see implementing our own erros maybe sometimes a pain in the ass, so we might prefer the `errors` package by go.

---

### Go Error Package

Go comes with a standard library errors package to create basic error with the specified message.

```go
import "errors"
```

```go
errors.New("error message")
```

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
