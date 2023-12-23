# Exit codes

In C++, the `exit` function is used to terminate the execution of a program. The value supplied as an argument to `exit` is returned to the operating system as the program's exit code. By convention, a return code of zero means that the program completed successfully.

Here are some of the commonly used exit codes in C++:

- `EXIT_SUCCESS`: 0, indicates successful termination of the program.
- `EXIT_FAILURE`: 1, indicates abnormal termination of the program.
- `SIGINT`: 2, indicates that the program was terminated by a user interrupt (Ctrl+C).
- `SIGSEGV`: 11, indicates that the program attempted to access a memory location that is not accessible.
- `SIGABRT`: 6, indicates that the program was aborted by a call to the `abort` function.
- `SIGKILL`: 9, indicates that the program was killed by the operating system.

You can also use user-defined exit codes. However, it is important to avoid using the following exit codes, as they have special meanings:

- 1, 2, 126-165, and 255

The `exit` function is defined in the `<stdlib.h>` header file.

Here is an example of how to use the `exit` function:

```c++
#include <stdlib.h>

int main() {
    if (some_error_occurred) {
        exit(1); // Terminate the program with an exit code of 1
    }

    // Do something else

    return 0; // Terminate the program with an exit code of 0
}
```

## Example: Using return in `main`

```cpp
#include <iostream>

int main() {
    // Some code here...

    if (/*some error condition*/) {
        std::cout << "An error occurred." << std::endl;
        return 1;
    }

    // More code here...

    if (/*another error condition*/) {
        std::cout << "Another error occurred." << std::endl;
        return 2;
    }

    return 0; // Successful execution
}
```
