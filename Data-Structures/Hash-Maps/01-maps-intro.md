## What is a Map ?

A map data structure, also known as an associative array or dictionary, is a fundamental concept in computer science.

It's used to store and manage a collection of **key-value pairs**, where each key is a unique identifier and each value is associated with that key.

This allows for efficient and fast retrieval of values based on their corresponding keys.

## Why Map ?

The map data structure is particularly useful when you want to:

1. **Retrieve Data Efficiently:** With a map, you can quickly look up a value using its associated key, making searching for specific information a lot faster compared to searching through an entire list.

2. **Maintain Relationships:** Maps are great for maintaining relationships between different pieces of data. For instance, you can use a map to associate a person's name with their contact information.

3. **Count Occurrences:** Maps are excellent for counting the occurrences of elements in a collection. For example, you could count the frequency of each word in a text.

4. **Implementing Algorithms:** Many algorithms and problem-solving techniques involve maps to store intermediate results or to track progress efficiently.

5. **Implementing Hash Tables:** Under the hood, a common way to implement maps is using hash tables, which are fundamental in computer science.

## Initialization

In C++, the map data structure is called a `std::map.`

It's part of the C++ Standard Template Library (STL) and provides a way to store key-value pairs in a sorted order based on the keys.

The keys in a `std::map` are unique, which means that each key can only appear once in the map.

```cpp
#include <map> // include standard map library
```

---

```cpp
// declaring a map in STL
std::map<datatype_of_key, datatype_of_value>name_of_map;
```

---

```cpp
// example :
std::map<int, int>mp;
```

---

```cpp
// Adding a key-value pair in a map

#include <bits/stdc++.h>
using namespace std;

int main(){

    map<string, int> scores;

    // adding value to a key :-
    // here, "Amit" is the key and 99 is the value.
    scores["Amit"] = 99;

    cout << "Amit's Score: " << scores["Amit"] << endl;

    return 0;
}

// output: 99

/*
Note that scores["Amit"] = 99;
is similar to what we do to initialise
an array element by arr[index] = some_value;
In case of a map, the index value can be of any data type.
In above example the key was a string, hence it was quoted inside a "...".
*/
```
