# Type Casting

Type casting in C++ is a way of converting an object of one data type into another. It allows you to change the data
type of a variable or expression. There are two types of type conversion: implicit and explicit.

**Implicit Type Conversion**: Also known as 'automatic type conversion', it is done by the compiler on its own, without
any external trigger from the user. It generally takes place when in an expression more than one data type is present.
In such conditions, type conversion (type promotion) takes place to avoid loss of data. All the data types of the
variables are upgraded to the data type of the variable with the largest data type. However, it is possible for implicit
conversions to lose information, signs can be lost (when signed is implicitly converted to unsigned), and overflow can
occur (when long long is implicitly converted to float)

**Explicit Type Conversion**: This process is also called type casting and it is user-defined. Here the user can
typecast the result to make it of a particular data type. In C++, it can be done by two ways:

1. **Converting by assignment**: This is done by explicitly defining the required type in front of the expression in
   parenthesis. This can be also considered as forceful casting.

```cpp
double x = 1.2;
// Explicit conversion from double to int
int sum = (int)x + 1;
```

2. **Conversion using Cast operator**: A Cast operator is an unary operator which forces one data type to be converted
   into another data type.

```cpp
float f = 3.5;
// using cast operator
int b = static_cast<int>(f);
```

C++ supports four types of casting:

1. **static_cast**: This is the most commonly used type of casting in C++. It can be used for conversions between
   related types (like from a base class pointer to a derived class pointer), among other things. It can also be used
   for conversions between unrelated types, such as from an int to a float. However, it does not perform any runtime
   checks, so it's up to the programmer to ensure the cast is safe.

```cpp
double x = 10.3;
int y;
y = static_cast<int>(x); // y is now 10
```

2. **const_cast**: This is used to add or remove the const or volatile qualifier from a variable. It can be used to
   modify a const object, which is undefined behavior in C++.

```cpp
const char* c = "sample text";
char* nonConst = const_cast<char*>(c); // nonConst now points to "sample text"
```

3. **dynamic_cast**: This is used for downcasting in the context of inheritance. It can be used to safely downcast a
   pointer or reference to a base class to a derived class. If the object is not of the target type, dynamic_cast
   returns null for pointers or throws a std::bad_cast exception for references.

```cpp
class Base {};
class Derived : public Base {};
Base* a = new Base;
Derived* b = dynamic_cast<Derived*>(a); // b is null
```

4. **reinterpret_cast**: This is the most powerful type of cast. It can convert any pointer type to any other pointer
   type, regardless of the classes they point to. It can also be used to convert any pointer type to an integer type and
   vice versa. It's the least safe type of cast and should be used sparingly.

```cpp
int* pi = new int(3);
char* pc =
    reinterpret_cast<char*>(pi); // pc now points to the same memory as pi
```

It's important to note that while these casts can be very useful, they should be used judiciously. Incorrect use of type
casting can lead to bugs that are hard to detect and fix. Always prefer safer casts (like static_cast and dynamic_cast)
over more dangerous ones (like reinterpret_cast), and only use const_cast when necessary to modify a const object.
