## Search in Rotated Sorted Array of Duplicate Elements.

**NOTE : A function Searching for an element in Rotated Sorted Array of Duplicate Elements cannot return it's index but returns a boolean value if the target is present in element or not.**

---

In [previous problem](./07-search-in-rotated-sorted-unique-array.md), when we searched the element in a rotated array of unique elements, if followed the steps :

- Compare mid with target.
- Check for the sorted half.
- Check for the element in the sorted half.

This steps would probably work with array of duplicate elements in very few cases, for example, if we have an array

```cpp
int arr[9] = {5, 6, 1, 2, 3, 3, 4, 4, 4};
int target = 4;
```

Everything works fine, we check for the sorted part by comparing `mid` with `low` and we see that the left half is not sorted so we trim that part and then we check for the target in right half and we found some duplicates of target so we returned `true` and everthing seems fine.

---

### But we are not considering an edge case !

```cpp
int arr[6] = {3, 1, 3, 3, 3, 3};
int target = 1;
```

Here we can't even compare the `mid`, `low` and `high` in order to find the sorted part as `low == mid == high`. But finding the sorted part is a crucial step to move forward! So how we'll procced further ??

---

**Well, to tackle this problem, we an first check if the mid is not equal to target and if it's not then we can trim down the search space until we find duplicates on low, mid and high.**

Here's what I mean :

```
Initial array:

index -->     0  1  2  3  4  5
int arr[6] = {3, 1, 3, 3, 3, 3}
              ^     ^        ^
             low   mid      high
```

```
Array after trimming corner duplicates if mid != target :

index -->     0  1   2  3  4  5
int arr[6] = {3, 1,  3, 3, 3, 3}
                 ^   ^     ^
                low mid   high
```

Once we came to a situation where `low != mid` or `mid != high`.

---

**How to trim the search space :**

```cpp
if (arr[low] == arr[mid] && arr[mid] == arr[high]){
    low++; high--;
    continue;
}
```

---

### Implementation :

```cpp
bool searchInARotatedSortedArrayII(vector<int>&arr, int target) {
    int n = arr.size();
    int low = 0; int high = n - 1;
    while (low <= high){
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return true;

        // if corner elements are duplicates of mid element
        if (arr[low] == arr[mid] && arr[mid] == arr[high]){
            low++; high--;
            continue;
        }

        // normal search-rotate-sort algorithm
        if (arr[low] <= arr[mid]){
            if (arr[low] <= target && target <= arr[mid]){
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        else {
            if (arr[mid] <= target && target <= arr[high]){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
    return false;
}
```

---

**Solve it on :**

[Coding Ninjas](https://www.codingninjas.com/studio/problems/search-in-a-rotated-sorted-array-ii_7449547?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf) &
[LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/).