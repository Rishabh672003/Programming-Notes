# Arrays

### basic definition

In C++, an array is a collection of elements of the same type that are stored sequentially in memory. Each element in an array can be accessed using an index value, which starts at 0 for the first element and increments by 1 for each subsequent element.

### initializing an array

First you define the type of each element in the array, and then you initialize the array with its name and number of elements in the array

```cpp
int arr[5]; // defines an array of 5 integers
string arr[5]; // defines an array of 5 strings
```

or

```cpp
int arr[5] = {1,2,3,4,5}
string arr[5] = {"a","b","c","d","e"}

```

You access the elements of an array using the index value, which starts at 0 for the first element and increments by 1 for each subsequent

```cpp
int x = arr[0]; // access the first element of the array
int y = arr[1]; // access the second element of the array
int z = arr[2]; // access the third element of the

```
##### Note that in C++, arrays do not perform bounds checking, so it is possible to access elements outside the bounds of the array. This can lead to undefined behavior, so it's important to be careful when working with arrays to ensure that you stay within the bounds of the array.
