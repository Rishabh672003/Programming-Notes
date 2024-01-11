## Hello Go!

Ensure you've Go installed in your system!

1. Create a Go module :

Navigate to the directory where you want to create your Go project and run the command

```bash
mkdir hellogo
cd hellogo
```

- **go mod init {REMOTE}/{USERNAME}/hellogo**

```bash
go mod init github.com/amitsuthar69/hellogo
```

What it does:

- Initializes a new Go module named `github.com/amitsuthar69/hellogo` in the current directory.
- Generates a file named `go.mod` at the root of your project, which tracks the module's dependencies.

Purpose of `go.mod`:

- Manages the dependencies required for your project, ensuring reproducible builds and managing version conflicts.
- Helps organize your code into modules, promoting modularity and reusability.

`go.mod` file :

```mod
module github.com/amitsuthar69/hellogo

go 1.21.5
```

---

2. Write Go code:

Create your first Go source files with `.go` extension files within the module directory.

```go
// hello.go file
package main

import "fmt"

func main() {
	fmt.Print("Let's Fckn Go!")
}
```

Here's a breakdown of the syntax :

- `package main`: This line declares that the code belongs to a package named `main`.

  The main package is special in Go because it's **the entry point for executable programs**.

- `import "fmt"`: This line imports the `fmt` package, which provides functions for formatted I/O (input and output) operations, such as printing to the console.

- `func main() { ... }`: This defines a function named main. In Go, the main function is the first function that gets executed when a program starts.

- `fmt.Print("Let's Fckn Go!")`: The `Print` function function from the `fmt` package prints the string to the console without adding a newline character at the end.

---

3. Run your code to see the greeting.

```
$ go run .
```
