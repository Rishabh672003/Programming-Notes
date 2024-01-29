## JSON Marshaling and UnMarshaling in Go

### What is JSON Marshaling and UnMarshaling ?

1. **JSON Marshaling** : Converting a Go Data Structure like `struct`, `slice` or `map` into a valid JSON string.

2. **JSON Unmarshaling** : Converting a valid JSON string into a Go Data Structure.

Below given is a simple Go code which implements a struct `Message`.

```go
package main
import "fmt"

type Message struct {
	Sender   string `json:"sender"`
	Receiver string `json:"receiver"`
	Text     string `json:"text"`
}

func main() {
	m := Message{"amit", "sumit", "hello"}
	fmt.Println("Original :", m)
}
```

```
Original : {amit sumit hello}
```

Let's encode the message `m` into a Valid JSON string.

---

### `encoding/json` package :

Package `encoding/json` implements encoding and decoding of JSON as defined in "**The JavaScript Object Notation (JSON) Data Interchange Format**"

---

### **1. Encoding :**

To encode JSON data, we use the `Marshal` function by `encoding/json` package :

```go
func Marshal(v interface{}) ([]byte, error)
```

Modifying our Messaging code:

```go
import (
    "encoding/json",
    "fmt"
)

type Message struct {
	Sender   string `json:"sender"`
	Receiver string `json:"receiver"`
	Text     string `json:"text"`
}

func main(){
    m := Message{"amit", "sumit", "hello"}
	fmt.Println("Original :", m)

    // encoding m into a JSON String
    b, err := json.Marshal(m)
	if err != nil {
		fmt.Println("error marshalling json")
	}
	fmt.Println("json encoded :", string(b))
}
```

Above update will print :

```
Original : {amit sumit hello}
json encoded : {"sender":"amit", "receiver":"sumit", "text":"hello"}
```

As we can observe, the Message m is now encoded into a JSON.

Not stringfying the result `b` will print the encoded JSON as a slice of `byte`

```
[123 34 115 101 110 100 101 114 34 58 34 97 109 105 116 34 44 34 114 101 99 101 105 118 101 114 34 58 34 115 117 109 105 116 34 44 34 116 101 120 116 34 58 34 104 101 108 108 111 34 125]
```

---

### **2. Decoding :**

To decode JSON data, we use the `Unmarshal` function.

```go
func Unmarshal(data []byte, v interface{}) error
```

Let's try to decode this Message m back to a `struct`.

```go
import (
    "encoding/json",
    "fmt"
)

type Message struct {
	Sender   string `json:"sender"`
	Receiver string `json:"receiver"`
	Text     string `json:"text"`
}

func main(){
    m := Message{"amit", "sumit", "hello"}
	fmt.Println("Original :", m)

    // encoding m into a JSON String
    b, err := json.Marshal(m)
	if err != nil {
		fmt.Println("error marshalling json")
	}
	fmt.Println("json encoded :", string(b))

    // decoding back to struct
    err = json.Unmarshal([]byte(b), &m)
    if err != nil {
    	fmt.Println(err)
    }
    fmt.Println("json decoded :", m)
}
```
