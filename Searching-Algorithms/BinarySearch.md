# Binary Search.

_Search Element in a Linear **Sorted** Data Structure._

**Time Complexity:**

1. Best Case: O(1) --> Element at middle of the array.
2. Average / Worst Case: O(log n) --> Element at 1st or last position.

## Logic.

1. Find Mid --> mid = start + (end - start) / 2.
2. Compare mid with target --> possible comparisons (mid == target) or (mid > target) or (mid < target).
3. If mid == target, return mid.
4. If mid != target, change path w.r.t (mid > target) or (mid < target)
5. If mid > target, start --> same, end --> mid - 1.
6. If mid < target, end --> same, start --> mid + 1.
7. Repeat.

## Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

int binarySearch(int *arr, int size, int target) {
    int start = 0;
    int end = size - 1;
    int mid = start + (end - start) / 2;
    while (start <= end)
    {
        if (arr[mid] == target)
            return mid;
        if (arr[mid] > target)
            end = mid - 1;
        else
            start = mid + 1;
        mid = start + (end - start) / 2;
    }
    return -1;
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int index = binarySearch(arr, 5, 3);
    if (index == -1)
        cout << "NOT FOUND!";
    else
        cout << "Element found at Index " << index;
    return 0;
}

```

## Linear Search v/s Binary Search.

In Linear search, for the worst case, if the size of array is 1000, then the function will perform 1000 comparisons.
In Binary Search, for worst case, for 1000 size array, the function will perform log<sub>2</sub>(1000) = 10 comparisons,
which is 100 times less than Linear Search.

## How O(log n) ?

Suppose a N sized array perform binary search, then the middle element will be at N/2<sup>1</sup> position where 1 represents 1st comparison.

The next mid will be at N/2<sup>2</sup> Position where 2 represents 2nd comparison.

Similarly at last comparison, N/2<sup>k</sup> , the mid = size of array i.e, 1.

Therefore N/2<sup>k</sup> = 1

N = 2<sup>k</sup>

Log<sub>2</sub>N = K

Which means, at kth comparison, the size of array will be log<sub>2</sub>N
