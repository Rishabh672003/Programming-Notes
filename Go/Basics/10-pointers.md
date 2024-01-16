## Pointers in Go

**Table of content :**

1. Pointers
2. Pointer Receivers

---

### Pointers

In any programming language, **pointers are variables which stores memory address of another variable**. This means that the pointer "points to" the location of where the data is stored _NOT_ the actual data itself.

Below image will help you understand pointers on memory level:

![pointers](https://github.com/amitsuthar69/assets/blob/main/Go/pointers.png?raw=true)

The type of a pointer in go is defined with `*` syntax

```go
var p *int // creates a pointer to an integer
```

This `&` operator generates a pointer to its operand.

```go
myString := "hello"
myStringPtr = &myString
```

Example :

```go
myString := "Hello"
fmt.Println(myString)     // Hello

myStringPtr := &myString  // creates a pointer

fmt.Println(myStringPtr)  // memory address 0xc000014080
fmt.Println(*myStringPtr) // Dereferences the pointer, prints Hello

*myStringPtr = "world"    // mutating myString with reference
fmt.Println(myString)     // world
```

---

### Pointer Receivers

A receiver type on a method can also be a pointer.

Methods with pointer receivers can modify the value to which the receiver points. Since methods often need to modify their receiver, pointer receivers are more common than value receivers.

```go
type car struct {
    color string
}

// making changes to the instance of type
func (c car) setColor(color string) {
    c.color = color // warning: ineffective assignment to field car.color
}
```

As soon as you try modifying the color property, your LSP warns you that this operation is ineffective. And even if you try to setColor to something else the changes would not be reflected.

So instead of passing the `car` struct, we can pass a reference of that struct as :

```go
type car struct {
	color string
}

func (c *car) setColor(color string) {
	c.color = color
}

func main(){
    c := car{
        color: "red",
    }
    c.setColor("black")
    fmt.Println(c.color) // black
}
```

NOTE that `c` is not a pointer to in the calling fuction but the method still gains access to a pointer to `c`.
