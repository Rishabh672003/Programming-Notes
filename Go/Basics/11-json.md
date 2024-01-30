## JSON Marshaling and UnMarshaling in Go

**Table of content :**

1. What is JSON Marshaling and UnMarshaling ?
2. encoding/json package
3. JSON Encoding & Decoding.

---

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

### **1. Marshaling :**

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

### **2. Unmarshaling :**

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

---

### JSON Encoding & Decoding (yeah, it's different from Marshalling)

`encoding/json` package provides few more Encoding & Decoding methods.

### **1. NewEncoder :**

- Creates an `Encoder` that writes JSON-encoded data to an `io.Writer` (file, network connection, etc).

- Used for streaming encoding, where data might be produced incrementally.

- Example: `encoder := json.NewEncoder(os.Stdout), encoder.Encode(myStruct)`

### **2. NewDecoder :**

- Creates a `Decoder` that reads JSON-encoded data from an `io.Reader` (file, network connection, etc).

- Used for decoding streams of JSON data, where the entire data might not be available at once.

- Example: `decoder := json.NewDecoder(res.Body), err := decoder.Decode(&myStruct)`

**Key Differences:**

- Whole Data vs. Streams: `Marshal` and `Unmarshal` operate on complete data, while `encoders`/`decoders` **handle streams of data.**

- Under-the-Hood: `Marshal` often uses an `encoder` internally, and `Unmarshal` often uses a `decoder`.

- Error Handling: `Decoders` can return `io.EOF` to signal the end of the stream, while `Unmarshal` typically returns other errors if parsing fails.

**When to Use Which:**

- Complete Data: Use `Marshal` and `Unmarshal` for one-time encoding/decoding of complete data structures.

- Streaming Data: Use `encoders`/`decoders` for working with large or streaming JSON data to avoid loading everything into memory at once.

- Multiple Objects: Use `decoders` to iterate over **multiple JSON objects** in a stream and process them individually.

**Let's fetch some JSON from an api nd parse it to better understand Decoding:**

To fetch JSON data, we'll use `https://hand-over.vercel.app/api/items` end-point which returns an array of items created at [handOver](https://hand-over.vercel.app). (yeah, that's my project)

```go
package main
import (
	"fmt"
	"net/http"
	"encoding/json"
)

func main(){
	res, err := http.Get("https://hand-over.vercel.app/api/items")
	if err != nil {
		panic(err)
	}

	defer res.Body.Close()
	var items []Item
	decoder := json.NewDecoder(res.Body)
	if err := decoder.Decode(&items); err != nil {
		fmt.Println("Error decoding JSON:", err)
	} else {
		fmt.Println(items)
	}
}
```

```go
type Item struct {
	Id          string `json:"id"`
	Description string `json:"description"`
	Price       string `json:"price"`
	ImageUrl    string `json:"imageUrl"`
	PublicId    string `json:"publicId"`
	CatName     string `json:"catName"`
	AuthorEmail string `json:"authorEmail"`
	CreatedAt   string `json:"createdAt"`
	UpdatedAt   string `json:"updatedAt"`
	Author      Author `json:"author"`
}

type Author struct {
	Name  string `json:"name"`
	Phone string `json:"phone"`
}
```
