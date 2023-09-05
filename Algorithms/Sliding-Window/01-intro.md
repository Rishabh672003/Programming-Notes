## Introduction to Sliding Window Algorithm.

- The sliding window algorithm is a technique for solving problems that involve a sequence of elements, such as an **array** or a **string**.

- The sliding window can be termed as a **sub-array** or a **sub-string** which moves over the sequence, and some operation is performed on the elements within the window.

- The algorithm works by maintaining a window of fixed or variable size over the sequence.

---

## Why we need this algorithm ?

Suppose you've a problem where your are provided an integer array,

```cpp
int arr[7] = {2, 3, 5, 2, 9, 7, 1};
```

and an integer let's say '3' which denotes the size of subarray. Find the maximum sum of subarrays.

**A subarray is a subset of an array. But it must be continuous in nature.**

```
The array 2 3 5 2 9 7 1 can have the follg. size 3 subarrays with their sum :

2 3 5  sum = 10
3 5 2  sum = 10
5 2 9  sum = 16
2 9 7  sum = 18 --> Maximum sum
9 7 1  sum = 17
```

To solve this problem, we might think about the Brute Force Aproach, where we consider 2 pointers `i` and `j`, we use 2 nested `for` loops where `i` iterates from 0 to size and `j` iterates from `i` to `j < i + 3` and stores the sum for each sub-array and at the end returns the max of all individual sums.

But then we will be performing a **repetitive task** of adding 2 same numbers for each iteration which we've **already performed** in previous iteration.

**Here's what I mean :**

```
2 + 3 + 5
3 + 5 + 2  we repeat 3 + 5
5 + 2 + 9  we repeat 5 + 2
2 + 9 + 7  we repeat 2 + 9
9 + 7 + 1  we repeat 9 + 7
```

Whenever you find such repetations in any program, there's a need of **Optimization**.

To overcome this repetitions, what we can do is to remove the previous value, once it gets added up and then add the upcoming value and so on.

This is something what a Sliding Window does. Whenever it moves ahead it leaves behind the previous value and includes the upcoming value.

**See Below Example :**

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--YIp-yToX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m12gjqex1tbxgsunop0h.png" />

---
