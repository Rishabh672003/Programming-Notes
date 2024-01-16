## Introduction to Go

**Table of contents:**

1. Introduciton to Go Language.
2. Go under the hood.
3. Memory Management.
4. Comparison with other languages.

---

### Introduciton to Go Language.

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

The Go runtime automatically manages memory allocation and deallocation for the programmer. This eliminates the need for manual memory management, but it comes with a cost:

- The Go runtime must keep track of every object that is allocated, leading to increased performance overhead.

- In certain scenarios, such as when an HTTP server processes requests with large protobuf blobs (which contain many small objects), this can result in the Go runtime spending a significant amount of time tracking each of those individual allocations, and then deallocating them. As a result this also causes signicant performance overhead.

---

### Comparison with other languages:

Unlike interpreted languages like Python, Go compiles to native code, offering faster execution. However, compilation adds an extra step compared to directly running interpreted code.

Go's static type system provides better error checking and refactoring possibilities compared to dynamically typed languages like JavaScript.

Go shines in concurrency with its goroutines and channels, compared to languages like JavaScript which is single-threaded & relies on an event loop to handle asynchronous operations.

---

Go [Installation](https://go.dev/doc/install).
