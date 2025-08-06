# Logical Operators in C++

Logical operators are used to perform logical operations on the given expressions, mostly to test the relationship
between different variables or values. They return a boolean value i.e., either true (1) or false (0) based on the
result of the evaluation.

C++ provides the following logical operators:

- **AND Operator (&&)**
  The AND operator checks if both the operands/conditions are true, then the expression is true. If any one of the
  conditions is false, the whole expression will be false.
  ```
  (expression1 && expression2)
  ```
  Example:
  ```cpp
  int a = 5, b = 10;
  if (a > 0 && b > 0) {
      cout << "Both values are positive." << endl;
  }
  ```
- **OR Operator (||)**
  The OR operator checks if either of the operands/conditions are true, then the expression is true. If both the
  conditions are false, it will be false.

  ```
  (expression1 || expression2)
  ```

  Example:

  ```cpp
  int a = 5, b = -10;
  if (a > 0 || b > 0) {
      cout << "At least one value is positive." << endl;
  }
  ```

- **NOT Operator (!)**
  The NOT operator reverses the result of the condition/expression it is applied on. If the condition is true, the NOT
  operator will make it false and vice versa.
  ```
  !(expression)
  ```
  Example:
  ```cpp
  int a = 5;
  if (!(a < 0)) {
      cout << "The value is not negative." << endl;
  }
  ```

Using these operators, you can create more complex logical expressions, for example:

```cpp
int a = 5, b = -10, c = 15;

if (a > 0 && (b > 0 || c > 0)) {
    cout << "At least two values are positive." << endl;
}
```

This covers the essential information about logical operators in C++.

# Arithmetic Operators in C++

Arithmetic operators are used to perform mathematical operations with basic variables such as integers and
floating-point numbers. Here is a brief summary of the different arithmetic operators in C++:

## 1. Addition Operator (`+`)

It adds two numbers together.

```cpp
int sum = a + b;
```

## 2. Subtraction Operator (`-`)

It subtracts one number from another.

```cpp
int difference = a - b;
```

## 3. Multiplication Operator (`*`)

It multiplies two numbers together.

```cpp
int product = a * b;
```

## 4. Division Operator (`/`)

It divides one number by another. Note that if both operands are integers, it will perform integer division and the
result will be an integer.

```cpp
int quotient = a / b;                 // integer division
float quotient = float(a) / float(b); // floating-point division
```

## 5. Modulus Operator (`%`)

It calculates the remainder of an integer division.

```cpp
int remainder = a % b;
```

## 6. Increment Operator (`++`)

It increments the value of a variable by 1. There are two ways to use this operator: prefix (`++x`) and postfix (`x++`).
Prefix increments the value before returning it, whereas postfix returns the value first and then increments it.

```cpp
int x = 5;
int y = ++x; // x = 6, y = 6
int z = x++; // x = 7, z = 6
```

## 7. Decrement Operator (`--`)

It decrements the value of a variable by 1. It can also be used in prefix (`--x`) and postfix (`x--`) forms.

```cpp
int x = 5;
int y = --x; // x = 4, y = 4
int z = x--; // x = 3, z = 4
```

These are the basic arithmetic operators in C++ that allow you to perform mathematical operations on your variables. Use
them in combination with other control structures, such as loops and conditionals, to build more complex programs.
