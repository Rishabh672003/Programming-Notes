# Templates

Templates in C++ are a powerful feature that allows you to write generic code. This means you can write a function or a
class that can work with different data types, without having to write separate versions of the function or class for
each data type.

**Function Templates**

Function templates are functions that can work with different data types. Here's an example of a function template that
prints out the value of an object of any type:

```cpp
template <typename T> void print(T value) { std::cout << value << std::endl; }

print(1);
print("Hello");
print(5.3);
```

In the above code, `T` is a placeholder for any data type. When you call the `print` function, you can pass an object of
any type for which operator `<<` is overloaded, and the `print` function will print out the value of the object.

**Class Templates**

Class templates are classes that can work with different data types. Here's an example of a class template that holds an object of any type:

```cpp
template <typename T> class Box {
    T value;

  public:
    Box(T value) : value(value) {}
    void print() { std::cout << value << std::endl; }
};
```

In the above code, `T` is a placeholder for any data type. When you create an object of the `Box` class, you can specify
the type of the object, and the `Box` class will hold an object of that type.

**Template Specialization**

Template specialization is a way to provide a different implementation of a function or a class for a specific data
type. Here's an example of a function template and a specialized version of the function for the `int` data type:

```cpp
// Function template
template <typename T> T add(T a, T b) { return a + b; }

// Specialized version for int
template <> int add<int>(int a, int b) { return a + b; }
```

In the above code, the `add` function template can add two objects of any type. The specialized version of the `add`
function for the `int` data type adds two `int` objects.

**Class Template Specialization**

Similarly, you can provide a different implementation of a class for a specific data type. Here's an example of a class
template and a specialized version of the class for the `int` data type:

```cpp
// Class template
template <typename T> class Box {
    T value;

  public:
    Box(T value) : value(value) {}
    void print() { std::cout << value << std::endl; }
};

// Specialized version for int
template <> class Box<int> {
    int value;

  public:
    Box(int value) : value(value) {}
    void print() {
        std::cout << "This is an integer box. Value: " << value << std::endl;
    }
};
```

In the above code, the `Box` class template can hold an object of any type. The specialized version of the `Box` class
for the `int` data type holds an `int` object and prints a different message when the `print` method is called.
