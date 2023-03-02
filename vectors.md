# STL vector in C++

In C++, a vector is a dynamic array that can resize itself during runtime. It is defined in the <vector> header file.

```cpp
#include <vector>
```

here's how to initialize a vector:

```cpp
vector<int> v;
```

to insert values into the vector:

```cpp
vector.push_back(1);
```

You can also access elements in the vector using the square bracket notation, just like with arrays:

```cpp
cout << vector[1]
```

Useful vector functions:

```cpp
vector.size(); // gives you the size of the vector
vector.capacity(); // gives you the capacity of the vector
vector.empty(); // empties the vector
vector.resize(n); // resizes the vector to n elements
vector.reserve(n); // reserves the capacity of the vector to n elements
vector.swap(v2); // swaps the contents of the vector v and v2
vector.clear(); // clears the vector
vector.front(); // returns the first element of the vector
vector.back(); // returns the last element of the vector
vector.data(); // returns a pointer to the vector's elements
vector.data() + i; // returns a pointer to the i'th element of the vector
vector.begin(); // returns a pointer to the first element of the vector
vector.end(); // gives you a pointer to the end of the vector
sort(vector.begin(), vector.end()); // sorts the vector in ascending order comes from STL
```

You can output all the elements of the vector using the `for` loop:

```cpp
for (auto i = 0; i < vector.size(); i++)
{
    cout << vector[i] << endl;
}
```
list out the function in the algorithm header file:

```cpp
sort(vector.begin(), vector.end()); // sorts the vector in ascending order comes from STL
reverse(vector.begin(), vector.end()); // reverses the vector

auto it = find(vector.begin(), vector.end(), 1); // finds the element 1 in the vector

```


