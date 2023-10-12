## Find Minimum in Rotated Sorted Array

Given the sorted rotated array **arr** of **unique** elements, return the **minimum** element of this array.
You must write an algorithm that runs in **O(log n)** time.

```cpp
int findMin(vector<int>& arr)
{
	int low = 0, high = arr.size() - 1;
	int ans = INT_MAX;
	while (low <= high) {
		int mid = low + (high - low) / 2;

		if (arr[low] <= arr[high]) {
			ans = min(ans, arr[low]);
			break;
		}

		if (arr[low] <= arr[mid]){
			ans = min(ans, arr[low]);
			low = mid + 1;
		} else {
			high  = mid - 1;
			ans = min(ans, arr[mid]);
		}
	}
	return ans;
}
```

---

**Solve it on :**

[Coding Ninjas](https://www.codingninjas.com/studio/problems/rotated-array_1093219?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf) &
[LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/).
