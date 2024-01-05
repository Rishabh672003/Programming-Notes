## Introduction to Go

Go, often called Golang, is a statically typed & compiled programming language created at Google.

It aims for simplicity, readability, and **concurrency**, making it great for building performant web services, network applications, and CLI tools.

_statically typed_ : the data type of each variable must be explicitly declared.

_compiled language_ : translated directly into machine code.

_concurrency_ : the ability of a program to handle multiple tasks or computations seemingly at the same time.

---

### Go under the Hood

Go uses a compiler to translate code into machine code. Its runtime environment manages memory, concurrency, and other low-level functionality.

Concurrency features are implemented using lightweight threads called **goroutines**, which communicate data through channels.

_goroutines_ : these are the foundation of Go's powerful concurrency features. They are lightweight threads of execution that run concurrently with other goroutines and the main program thread.

---

### Memory Management

Go uses garbage collection (GC) to automatically reclaim unused memory allocated during program execution. This simplifies memory management for developers and prevents memory leaks.

---

Comparison to Other Languages:

Unlike interpreted languages like Python, Go compiles to native code, offering faster execution. However, compilation adds an extra step compared to directly running interpreted code.

Go's static type system provides better error checking and refactoring possibilities compared to dynamically typed languages like JavaScript.

Go shines in concurrency with its goroutines and channels, compared to languages like JavaScript which is single-threaded & relies on an event loop to handle asynchronous operations.

---

Go [Installation](https://go.dev/doc/install).
