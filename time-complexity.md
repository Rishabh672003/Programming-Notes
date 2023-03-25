# Time Complexity with the big O notation

Time complexity refers to the amount of time it takes for an algorithm to execute as a function of the size of its input.
In other words, it is a measure of the amount of time it takes an algorithm to solve a problem as the size of the problem increases.

The time complexity of an algorithm is generally expressed in big O notation.
It provides an upper bound on the growth rate of the algorithm's running time.

For example, if an algorithm has a time complexity of O(n), it means that the algorithm's running time increases linearly with the size of its input,
where n represents the size of the input. If the algorithm has a time complexity of O(n^2),
it means that the algorithm's running time increases quadratically with the size of its input.

A time complexity of O(n^2) may still run faster than an algorithm with a time complexity of O(n) for small inputs,
but as the input size increases, the O(n^2) algorithm will eventually become slower.

Some common time complexities:

```
O(1) (constant time),
O(log n) (logarithmic time),
O(n) (linear time),
O(n log n) (quasilinear time),
O(n^2) (quadratic time), and
O(2^n) (exponential time).

Increase in Time Complexity -->
O(1) < O(log n) < 0(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)
```

Time Complexity for various functions:

1. If-Else:

The time complexity of an if-else statement in C++ is O(1), or constant time,

For example, consider the following if-else statement:

```cpp
if (n > 0) {
  /* the amount of time it takes to evaluate the condition
  and execute the corresponding block of code does not depend on the size of the input.*/
} else {}
```

2. For Loop:

The time complexity of a for loop depends on the number of iterations it performs.
In general, a for loop with a fixed number of iterations has a time complexity of O(1) because the number of iterations is constant
and does not depend on the size of the input.

For example, consider the following for loop in C++ that iterates 10 times:

```cpp
for (int i = 0; i < 10; i++) {
  // Since the number of iterations is fixed at 10, the time complexity of this for loop is O(1).
}
```

However, if the number of iterations in the for loop depends on the size of the input,
then the time complexity will depend on the input size.

For example, consider the following for loop that iterates n times:

```cpp
for (int i = 0; i < n; i++) {
  /* In this case, the time complexity of the for loop is O(n)
  because the number of iterations depends on the size of the input, which is represented by the variable n.*/
}
```

##### Other algorithms

```
3. Array Access: O(1) Accessing an element in an array takes constant time since the index can be used to directly access the element.
4. Bubble Sort: O(n^2)
5. Insertion Sort: O(n^2)
6. Selection Sort: O(n^2)
7. Merge Sort: O(n log n)
8. Quick Sort: O(n log n) (average case)
9. Linear Search: O(n)
10. Binary Search: O(log n) (for a sorted array)
11. Length: O(1)
12. Concatenation: O(m+n) (where m and n are the lengths of the strings being concatenated)
13. Comparison: O(min(m,n)) (where m and n are the lengths of the strings being compared)
```
--------------------------------------------------------------------------
![Time-complexity](https://user-images.githubusercontent.com/53911515/227717627-0e7671ac-1dc7-4863-8832-6fed71ef3e23.png)
--------------------------------------------------------------------------
These time complexities are for worst-case scenarios and may vary depending on the specific implementation of the function and the input data.

TLE (Time Limit Exceeded): It is a common error that occurs when the execution time of a program exceeds the time limit set by the compiler.

Tips to avoid TLE:

1. Avoid nested loops.
2. Use efficient data structures.
3. Avoid recursion.
4. Understand the time limit.
