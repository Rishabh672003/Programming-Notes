## Arrays and Slices in Go

**Table of content :**

1. Arrays in Go.
2. What are Slices?

---

### Arrays in Go

In Go, Arrays are ordered lists, obviously 0 based indexing.

But this Arrays are more similar to arrays in C or C++ and not similar to python or javascript. If you got me, Arrays in Go are static, meaning they **have fixed sizes**.

**Declaration Syntax : `var arrayName [size]type`**

```go
var myArray[10]int
```

The above code declares an integer array `arr` of size 10.

---

We better initialize it directly

**Initialization Syntax : `arrayName := [size]type{array, elements}`**

```go
myArray := [5]int{1, 2, 3, 4, 5}
```

---

**Fuctions have a return type of array as :**

```go
func returnArray() [3]string {
    // returns a string array of size 3
}
```

To overcome this fixed sized paradigm, Slices are introduced.

---

### What are Slices ?

Slices in Go are **dynamic in nature**, means unlike arrays, they don't have fixed sizes.

These slices are built on the top of arrays, means they have the ability to extract elements from an existing array.

---

In terms of memory allocation, under the hood, slices works same as the vector data structure from C++.

Meaning any effort made to grow the size of slice by adding some more value in it, it just clones itself with a **size double** to it's original.

---

The syntax is much similar to an array, just fill in the `[]` brackets or keep it empty.

Syntax :

```
arrayName[lowIndex:highIndex] for a range
arrayName[lowIndex:] from lowIndex till end
arrayName[:highIndex] from starting till highIndex
arrayName[:] entire array
```

Example :

```go
array := [6]int{1, 2, 3, 4, 5, 6} // [1 2 3 4 5 6]
slice1 := array[1:4] // [2 3 4]
slice2 := array[1:] // [2 3 4 5 6]
slice3 := array[:4] // [1 2 3 4]
slice4 := array[:] // [1 2 3 4 5 6]
```

---

If we want to create a slice with specific set of values, we can use slice literals

**Syntax : `sliceName := []type{"slice", "elements"}`**

```go
mySlice := []string{"I", "am", "Amit"}

fmt.Println(len(mySlice)) // 3 (current size)
fmt.Println(cap(mySlice)) // 3 (maximum size)
```

Note that the array brackets do not have a `3` in them. If they id, we'd have an array instad of a slice.

---

In Go, 99% of the time, we never deal with an array, we use slices instead.
