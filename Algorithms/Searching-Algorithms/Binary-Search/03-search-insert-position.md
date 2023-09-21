## Search Insert Position

You're given a sorted array `arr` of distinct values and a target value `m`. Search for the index of the target value in array.

---

**Note :**

- If the value is present in the array, return its index.

- If the value is absent, determine the index where it would be inserted in the array while **maintaining the sorted order.**

- Consider 0-based indexing only.

---

**Example :**

```
int arr[5] = {1, 2, 3, 5, 7};
m = 6;

Output : 3

Explanation : In the given array, the target 6 is not available so we can insert m = 6 at index 3 to maintain sorted order.
```

---

**Implementation :**

```cpp
#include <bits/stdc++.h>
using namespace std;

int searchInsert(vector<int>& arr, int m) {
  int n = arr.size();
  int low = 0, high = n - 1;
  int ans = n;
  while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] >= m) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return ans;
}

int main() {
  vector<int> arr = {1, 3, 5, 6, 8, 9};
  int m = 7;
  cout << searchInsert(arr, m) << endl;
  return 0;
}
```

```
Output : 4

Explanation : 7 isn't present in the array so 4 will be the index where 7 would be inserted so as to maintain sorted order.
```

---

**Refer :**
[Lower Bound](./02-lower&upper-bound.md), [Binary Search](./01-binary-search.md).

---

**Solve it on :**

[Coding Ninjas](https://www.codingninjas.com/studio/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf) &
[LeetCode](https://leetcode.com/problems/search-insert-position/#:~:text=Search%20Insert%20Position%20%2D%20LeetCode&text=Given%20a%20sorted%20array%20of,(log%20n)%20runtime%20complexity).
