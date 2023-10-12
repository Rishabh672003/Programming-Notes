## Number of Occurrence of element in an array.

### Number of occurrence = last occurrence - first occurrence + 1

---

**Implementation :**

```cpp
#include <bits/stdc++.h>
using namespace std;

int lowerBound(vector<int>& arr, int n, int x) {
  int low = 0, high = n - 1;
  int ans = n;
  while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] >= x) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return ans;
}

int upperBound(vector<int>& arr, int n, int x) {
  int low = 0, high = n - 1;
  int ans = n;
  while (low <= high) {
    int mid = low + (high - low) / 2;
    if (arr[mid] > x) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return ans;
}

pair<int, int> firstAndLastPosition(vector<int>& arr, int n, int k) {
  int lb = lowerBound(arr, n, k);
  if (lb == n || arr[lb] != k) return {-1, -1};
  return {lb, upperBound(arr, n, k) - 1};
}

int count(vector<int>& arr, int n, int x) {
  pair<int, int> ans = firstAndLastPosition(arr, n, x);
  if (ans.first == -1) return 0;
  return ans.second - ans.first + 1;
}

int main() {
  vector<int> arr = {1, 3, 5, 5, 5, 5, 7, 8, 9};
  int x = 5;
  int count = count(arr, arr.size(), x);
  cout << "The number of occurrences of " << x << " in the array is " << count << endl;
  return 0;
}
```

```
Output :
The number of occurrences of 5 in the array is 4
```

---

**Solve it on :**

[Coding Ninjas](https://www.codingninjas.com/studio/problems/occurrence-of-x-in-a-sorted-array_630456?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf).
