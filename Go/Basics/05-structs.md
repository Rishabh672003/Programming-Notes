## Structs in Go

**Table of content :**

1. What are structs in Go?
2. Anonymous structs
3. Embedded structs
4. Methods in struct

---

### What are structs in Go ?

Structs are user-defined types that group related values (fields) of different types under a single name.

Structs in Go are conceptually similar to TypeScript's type aliases for objects.

1. A Go struct declaration :

```go
type Person struct {
    name string
    age  int
    city string
}
```

2. Creating Instance of this struct :

```go
user := Person{"Amit", 19, "Palo Alto"}
```

3. Accessing struct fields :

```go
username := user.name // output: Amit
```

---

**Example :**

```go
type Message struct {
    sender string
    receiver string
}

func sendMessage(m Message) {
    fmt.Println("Message sent by %s to %s", m.sender, m.receiver)
}

func main(){
// Create a Message instance
msg := Message{"Amit", "Rizzabh"}
sendMessage(msg)
// Output: "Message sent by Amit to Rizzabh"
}
```

---

And we can also nest structs within other structs

```go
type Car struct {
    Make string
    Model string
    FrontWheel Wheel // utilizing Wheel struct
    RearWheel wheel
}

type Wheel struct {
    Radius int
    Material string
}

func main(){
    myCar := Car {} // empty car | assigned to default values
    myCar.FrontWheel.Radius = 20
}
```

---

### Anonymous Structs

An Anonymous struct is just like a normal struct, but it is defined without any name and therfore can not be referenced elsewhere in the code.

To create an Anonymous struct, just instantiate the instance immediately using a second pair of curly brackets after declaring the type.

```go
person := struct {
    name string
    age int
} {
    name: "Amit"
    age: 19
}
```

Nesting Anonymous structs :

```go
type Car struct {
    Make string
    Model string
    Wheel {
        Radius int
        Material string
    }
}
```

Anonymous structs are best suited for handling HTTP handlers to handle the shape of JSON payloads.

---

### Embedded structs

Go is not a OOP language but it provides a kind of data-level inheritance (not in complete sense) using embedded structs.
These kind of structs are just a way to elevate & share fields among structs

```go
type person struct {
    name string
    age int
}
type user struct {
    person
    isAuthorised bool
}

func main(){
    user1 := user{
        person: person{
            name: "Amit"
            age: 19
        }
        isAuthorised: true
    }
}
```

---

### Methods in struct

Even though Go is not an OOP language, It does support methods defined on structs. These methods are just fucntions which have receivers.

A receiver is a special parameter that syntactically gos before the name of function.

```go
type Rect struct {
    width int
    height int
}

func (r Rect) area() int {
    return r.width * r.height
}
```

Now, `area()` becomes a method for struct `Rect` and can be called for any `Rect` struct instantiation :

```go
func main(){
    rect := Rect{
		width:  10,
		height: 10,
	}
	fmt.Println(Rect.area())
}
```
