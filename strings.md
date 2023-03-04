# Strings

In C++, a string is a sequence of characters stored in a contiguous block of memory. The standard library provides a string class that encapsulates the management of these sequences of characters.

- ### To use Strings you need to import the string class from the <string>

```cpp
#include <string>
```

- ### Initialization and declaration:

```cpp

#include <string>
using namespace std;

string str;               // declares an empty string
string str1 = "Hello";    // declares a string initialized with "Hello"
string str2("World");     // declares a string initialized with "World"
string str3 = str1 + " " + str2;  // concatenates two strings

```

- ### To input and output strings

```cpp

cout << str1 << endl;     // prints the string to the console
cin >> str;               // reads a string from input
getline(cin, str);        // reads a line of text (string) from input

```

- ### String manipulation

```cpp

str.append(" World");     // appends " World" to the string
str.insert(0, "Hello ");  // inserts "Hello " at the beginning of the string
str.replace(0, 5, "Hi");  // replaces the first 5 characters with "Hi"
str.erase(0, 3);          // erases the first 3 characters of the string

```
