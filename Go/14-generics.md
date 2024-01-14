## Generics in Go

**Table of content :**

1. Go before Generics (before v1.20)
2. Type Parameters
3. Why Generics?
4. Constraints

---

### Go before Generics (before v1.20)

As I've mentioned, **Go does not support classes**. For a long time, that meant that Go code couldn't easily be reused in many circumstances.

For example, imagine some code that splits a slice into 2 equal parts. The code that splits the slice doesn't really care about the values stored in the slice. Unfortunately in Go we would need to write it multiple times for each type, which is a very un-DRY thing to do.

```go
// for int type slices
func splitIntSlice(s []int) ([]int, []int) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}

// for string type slice
func splitStringSlice(s []string) ([]string, []string) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

### In Go 1.20 however, support for generics was released, effectively solving this problem!

---

### Type Parameters

Put simply, generics allow us to use variables to refer to specific types. This is an amazing feature because it allows us to write abstract functions that drastically reduce code duplication.

```go
// for any type of slice
func splitAnySlice[T any](s []T) ([]T, []T) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

```go
firstInts, secondInts := splitAnySlice([]int{0, 1, 2, 3})
fmt.Println(firstInts, secondInts)
```

---

### Why Generics?

**1. Generics reduce repetitive code**

We should care about generics because they mean we don’t have to write as much code! It can be frustrating to write the same logic over and over again, just because we have some underlying data types that are slightly different.

**2. Generics are used more often in libraries and packages**

Generics give Go developers an elegant way to write amazing utility packages. While we will see and use generics in application code, I think it will much more common to see generics used in libraries and packages.

Libraries and packages contain importable code intended to be used in many applications, so it makes sense to write them in a more abstract way. Generics are often the way to do just that!

---

### Constraints

Sometimes we need the logic in your generic function to know something about the types it operates on. The example I used in the first exercise didn't need to know anything about the types in the slice, so we used the built-in any constraint.

`Constraints` are just `interfaces` that allow us to write generics that **only operate within the constraint of a given interface type**. In the example above, the `any` constraint is the same as the **empty interface** because it means the type in function can be anything.

**Creating custom constraints**

```go
type stringer interface {
    String() string
}

func concat[T stringer](vals []T) string {
  result := ""
    for _, val := range vals {
        // this is where the .String() method
        // is useful. That's why we need a more specific
        // constraint instead of the any constraint
        result += val.String()
    }
    return result
}
```
