## Find Peak Element

**Problem Statement :**
A peak element is an element that is **strictly** greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. _If the array contains multiple peaks, return the index to any of the peaks._

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be **strictly** greater than a neighbor that is outside the array.

You must write an algorithm that runs in **O(log n)** time.

---

**Example :**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

---

### Implementation :

```cpp
int findPeakElement(vector<int> &arr) {
    int n = arr.size();

    // trimming search space by checking corners
    if (n == 0) return 0;
    if (arr[0] > arr[1]) return 0;
    if (arr[n - 1] > arr[n - 2]) return n - 1;
    int low = 1, high = n - 2;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        // if my mid is a peak
        if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]) return mid;

        // if mid is on an increasing curve
        else if (arr[mid] > arr[mid - 1]) low = mid + 1;

        // if mid is on an deccreasing curve
        else high = mid - 1;
    }
    return -1;
}
```

---

[Coding Ninjas](https://www.codingninjas.com/studio/problems/find-peak-element_1081482?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf) &
[LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/).
