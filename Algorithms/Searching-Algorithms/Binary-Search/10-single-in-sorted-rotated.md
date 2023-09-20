## Single Element in a Sorted Array

**Problem Statement :**
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.
Your solution must run in **O(log n)** time and **O(1)** space.

---

**Example :**

```
Input: arr[9] = [1,1,2,3,3,4,4,8,8];
Output: 2
```

---

### Implementation :

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& arr) {
    int n = arr.size();

	if (n == 1) return arr[0]; // if only 1 element in array

	// trimming down array size to avoid extra comparisons.
	if (arr[0] != arr[1]) return arr[0];
	if (arr[n-1] != arr[n-2]) return arr[n-1];
	int low = 1, high = n - 2;

	while (low <= high){
		int mid = low + (high - low) / 2;

		// search for mid to be a single
		if (arr[mid] != arr[mid - 1] && arr[mid] != arr[mid + 1]) return arr[mid];

        /* if one of th half is sorted, our answer is in the opposite half. if we are on left half and it is sorted, eleminate it */
		if ((mid % 2 == 1 && arr[mid] == arr[mid - 1])
			|| (mid % 2 == 0 && arr[mid] == arr[mid + 1])) {
				low = mid + 1;
		}

		// else right half is sorted, eleminate it.
		else {
			high = mid - 1;
		}

	}
	return -1;
    }
};
```

---

**Solve it on :**

[Coding Ninjas](https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf) &
[LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/).
