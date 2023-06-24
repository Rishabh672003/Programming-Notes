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
// A string ends with a null character '\0' in memory, which shows that the string ends here.
```

- ### To input and output strings

```cpp

cout << str1 << endl;  // prints the string to the console
cin >> str;            // reads a string from input. 'cin' stops consideering an input as string whenever it gets a space " ".
getline(cin, str);     // reads a line of text (string) from input and Overcome 'cin'.

```

- ### Length of a String.

```cpp
string str = "Hello, world!";
int length = str.length(); // or str.size();
cout << "Length of string: " << length << endl;
```

- ### Reverse a String.

```cpp
string myString = "Hello, world!";
reverse(myString.begin(), myString.end());
cout << "Reversed string: " << myString << endl;

// Or By Character Array Method.
void reverseString(vector<char>& s) {
    int st = 0;
    int e = s.size() - 1;
    while(st < e) {
      swap(s[st++], s[e--]);
    }
}
```

- ### Rotate A String.

```cpp
string myString = "Hello, world!";
rotate(myString.begin(), myString.begin() + 7, myString.end());
cout << "Rotated string: " << myString << endl;

/* Explanation:

This code will output: Rotated string: world!Hello,

The rotate() function takes three arguments:
The first one is the beginning of the range to be rotated,
The second one is the new beginning of the range after the rotation, and
The third one is the end of the range to be rotated.
In this case, we are rotating the string by 7 positions to the right,
so we pass myString.begin() + 7 as the second argument to rotate().
This means that the characters from index 0 to index 6 will be moved to the end of the string,
while the characters from index 7 to the end of the string will be moved to the beginning of the string.

*/
```

- ### String manipulation

```cpp

str.append(" World");     // appends " World" to the string
str.insert(0, "Hello ");  // inserts "Hello " at the beginning of the string
str.replace(0, 5, "Hi");  // replaces the first 5 characters with "Hi"
str.erase(0, 3);          // erases the first 3 characters of the string

```

- ### String Case Change.

```cpp

string str;
cout << "Enter String: ";
cin >> str;

// Convert each character to lowercase
for (char &c : str){
  c = tolower(c); // For uppercase, use toupper(c);
}

cout << str << endl; // prints lower case output.

/* How Case Conversion works:

1. Uppercase --> Lowercase
('CHARACTER' - 'A') + 'a'.

2. Lowercase --> Uppercase
('character' - 'a') + 'A'.

eg: [B]
We know that A --> 1, B --> 2.
then, B - A --> 2 - 1 = 1.
now, This 1 + 'a' --> 1 + 1 = 2 --> 'b'

3. Character --> Number (integer)
suppose, char = '1'.
then, 'ch' - '0' = number
i.e; '1' - '0' = 1.
*/
```

- ### Check Palindrome [For a Single Word].

```cpp
bool isPalindrome(string s)
{
    int left = 0, right = s.length() - 1;
    while (left < right)
    {
        if (s[left] != s[right])
        {
            return false;
        }
        left++;
        right--;
    }

    return true;
}
```

- ### Check Palindrome [for a sentence inculding spaces & special characters]

```cpp
/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: After removing all the spaces and special characters, "amanaplanacanalpanama" is a palindrome.
*/

#include <bits/stdc++.h>
using namespace std;

bool isAlphanumeric(char ch)
{
    return isalpha(ch) || isdigit(ch); // checks alphabet and digits, return true if alphabet or digit
}

bool isPalindrome(string s)
{
    // Remove non-alphanumeric characters and convert to lowercase
    string cleanStr;
    for (char ch : s)
    {
        if (isAlphanumeric(ch))
        {
            cleanStr += tolower(ch);
        }
    }

    // Check if the cleaned string is a palindrome
    int left = 0, right = cleanStr.length() - 1;
    while (left < right)
    {
        if (cleanStr[left] != cleanStr[right])
        {
            return false;
        }
        left++;
        right--;
    }

    return true;
}

int main()
{
    string str;
    cout << "Enter Something: ";
    cin >> str;
    cout << "Is Palindrome: " << isPalindrome(str); // Returns 1 or 0, if palindrome or not.
    return 0;
}

```
