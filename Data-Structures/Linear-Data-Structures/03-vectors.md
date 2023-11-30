# STL vector in C++

In C++, a vector is a dynamic array that can resize itself during runtime. It is defined in the <vector> header file.

```cpp
#include <vector>
```

Here's how to initialize a vector:

```cpp
vector<int> v;
```

Initialize Vector with size.

```cpp
vector<int> v1(5); // Vector with size 5. By Default all elements are assigned as 0.
vector<int> v2(5, 1) // Vector with size 5, and all elements are assigned as 1.
```

To insert and remove values from the vector:

```cpp
vector.push_back(1); // Insert Values from behind.
vector.pop_back();   // Removes an element from end.
```

You can also access elements in the vector using the square bracket notation, just like with arrays:

```cpp
cout << vector[1];
```

Adding elements in vector with `for` loop.

```cpp
vector<int> a(5);
for (int i : a) // for i belongs to vector a.
{
    cin >> i;
}
```

You can output all the elements of the vector using the `for` loop:

```cpp
for (auto i = 0; i < vector.size(); i++) {
    cout << vector[i] << " ";
}
/*
The keyword auto is used to declare a variable i without specifying its type
explicitly. Instead, the type of i is automatically deduced by the compiler
based on the type of the container.
*/
```

```cpp
vector<int> b(a); // Copying vector a to another vector b.
```

Vector in a function.

```cpp
returnType functionName(vector<int>& vectorName, int size) { returnValue; }
```

Useful vector functions:

```cpp
vector.size();          // gives you the size of the vector
vector.capacity();      // gives you the capacity of the vector i.e; the memory
                        // allocated to it.
vector.empty();         // empties the vector
vector.resize(n);       // resizes the vector to n elements
vector.shrink_to_fit(); // releases unused memory and set the capacity to match
                        // the current size.
vector.reserve(n);      // reserves the capacity of the vector to n elements
vector.swap(v2);        // swaps the contents of the vector v and v2
vector.clear();         // clears the vector
vector.front();         // returns the first element of the vector
vector.back();          // returns the last element of the vector
vector.data();          // returns a pointer to the vector's elements
vector.data() + i;      // returns a pointer to the i'th element of the vector
vector.begin();         // returns a pointer to the first element of the vector
vector.end();           // gives you a pointer to the end of the vector
back_inserter(vector);  // returns an iterator to the last element
sort(vector.begin(),
     vector.end()); // sorts the vector in ascending order comes from STL
sort(vector.begin(), vector.end(),
     greater<int>()); // sorts the vector in descending order comes from STL
```

These are some functions in the algorithm library in c++ very useful for manipulating vectors:

```cpp

#include <algorithm> // you need this to use the algorithm library

reverse(vector.begin(), vector.end()); // reverses the vector
auto it = find(vector.begin(), vector.end(), 1); // finds the element 1 in the vector
auto it = min_element(vector.begin(), vector.end()); // finds the minimum element in the vector
auto it = max_element(vector.begin(), vector.end()); // finds the maximum element in the vector
sum(vector.begin(), vector.end());          // returns the sum of all elements in the vector
swap(vector[0], vector[1]); // swaps the first two elements of the vector
unique(vector.begin(), vector.end()); // removes all the duplicates from the vect
binary_search(vector.begin(), vector.end(), 1); // returns true if 1 is in the vector, false otherwise
erase(vector.begin(), vector.end()); // erases all the elements from the)
```
