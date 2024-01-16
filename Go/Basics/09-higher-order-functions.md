## Higher order functions in Go

**Table of content :**

1. First Class and Curring functions
2. Defers
3. Closures

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

The `defer` keyword in functions is fairly unique feature to Go. It allows a function to be executed automatically just before it's enclosing function returns.

The `defer` call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

Deferred functions are typially used in closing database connections and file handlers.

```go
// CopyFile copies file from srcName to dstName on the local
func CopyFile(dstName, srcName string) (written int, err error){
    src, err = os.Open(srcName)
    if err != nil {
        return
    }
    // close the source file when CopyFile function returns
    defer src.Close()

    dst, err = os.Open(dstName)
    if err != nil {
        return
    }
    // close the destination file when CopyFile function returns
    defer dst.Close()

    return io.Copy(dst, src)
}
```

Let's see an another Example to understand it's use better :

```go
func logAndDeleteUser(users map[string]User, name string) (log string){
    user, ok := users[name]
    if !ok {
        delete(users, name)
        return "User not found"
    }
    if user.admin {
        delete(users, name)
        return "Admin deleted"
    }
    delete(users, name)
    return "User deleted"
}
```

The above `logAndDeleteUser` function takes in a user map, name, and return some server logs. In this function we check have 3 checks before deleteing that user, whether the user exists, if exist then is the user an admin, or it's just a normal user. And for each check, we call the `delete()` function.

But function `delete()` is being called thrice and this thing can be a problem if we add some more checks in future and we forget to delete the user.
We can hence use `defer` keyword as :

```go
func logAndDeleteUser(users map[string]User, name string) (log string){
    defer delete(users, name)
    user, ok := users[name]
    if !ok {
        return "User not found"
    }
    if user.admin {
        return "Admin deleted"
    }
    return "User deleted"
}
```

This function still works the same, the `defer` keyword before `delete()` function makes sure that any time `logAndDeleteUser` returns something, the `delete()` function gets called.

---

### Closures

A closure is a function that refrences a variable from outside its own function body. The function may access and assign to the referenced variable.

When a variable is enclosed in a closure, the enclosing function has access to **a mutable reference of that variable** and **not a copy of that variable.**

Example :

```go
func concatter() func(string) string {
	doc := ""
	return func(word string) string {
		doc += word + " "
		return doc
	}
}
```

```go
func main(){
    makeFriends = concatter()
    makeFriends("Amit")
    makeFriends("Rishabh")
    makeFriends("Sumit")
    fmt.Println(makeFriends("Harshil")) // prints Amit Rishabh Sumit Harshil
}
```

In the above code, the `concatter()` function returns a function which has a reference to an enclosed `doc` variable. Each successive call to `makeFriends` mutates that same doc variable. Note that `doc` in this closure
