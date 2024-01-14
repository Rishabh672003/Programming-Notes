## Maps ~ The Go Objects

**Table of content**

1. What are Maps in Go?
2. Mutating maps

---

### What are Maps in Go?

Maps in Go are similar to JavaScript objects or Python dictionaries. Maps are a data structure that provides a key->value mapping.

We can create maps using a literal or `make()` function :

```go
// mapName := make(map[keyType]valueType) creates an empty map
ages := make(map[string]int)
ages["Amit"] = 18
ages["Rishabh"] = 18
ages["Amit"] = 19 // overwrites 18
```

```go
// mapName := map[keyType]valueType{...}
ages := map[string]int{
    "Amit": 19,
    "Rishabh": 18,
}
```

The `len` function works on maps as well, it returns the total number of key-value pairs in that map

```go
fmt.Println(len(ages)) // 2
```

To print these key-value pairs, we can use `for` loops as :

```go
for key, value := range ages {
	fmt.Println(key, value)
}
// Amit 19
// Rishabh 18
```

Looking up a value in a map is much faster than searching thorough a slice.

---

### Mutating maps

1. Inset an element :

```go
m[key] = elem
```

2. Get an element :

```go
elem = m[key]
```

3. Deleting an element

```go
delete(m, key)
```

4. Check if key exists :

```go
elem, ok := m[key]
// if key is in m, ok is true else, its false
```

If key is not in the map, then `elem` is the zero value for the map's element type.

---

The key types in maps can be anything comporable among primitive data types, and not slices, maps or functions which are not a comparable data type.

```go
myMap = make(map[string]map[string]int)
```

The above code, creates a map whose key is a `string` but the value is again an another map whose key is also a `string` and value is an `int`.
