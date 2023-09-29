## Floor and Ceil in array.

**Floor : _Largest_ element in array which is <= x.**

**Ceil : _Smallest_ element in array which is >= x.**

---

**Example :**

```
int arr[5] = {10, 20, 30, 40, 50};
int x = 25

here, floor --> 20 and ceil --> 30

Explanation :
floor : 10 <= 25, 20 <= 25 but 20 > 10, so 20.
ceil : 30 >= 25, 40 >= 25, 50 >= 25 but 40 > 30 < 50, so 30.
```

**Note :** If the element exists in the array then the **element itself** is floor and ceil.

---

**Implementation :**

```cpp
int findFloor(vector<int>& arr, int x){
    int n = arr.size();
    int low = 0, high = n - 1;
    int ans = -1;
    while (low <= high){
        int mid = low + (high - low) / 2;
        if (arr[mid] <= x){
            ans = arr[mid]; // maybe an answer
            low = mid + 1;
            // eleminate the left search space as we want to find the 'largest' element.
        } else {
            high = mid - 1;
        }
    }
    return ans;
}

int findCeil(vector<int>& arr, int x){
    int n = arr.size();
    int low = 0, high = n - 1;
    int ans = -1;
    while (low <= high){
        int mid = low + (high - low) / 2;
        if (arr[mid] >= x){
            ans = arr[mid]; // maybe an answer
            high = mid - 1;
            // eleminate the right search space as we want to find the 'smallest' element.
        } else {
            low = mid + 1;
        }
    }
    return ans;
}

int main() {
  vector<int> arr = {1, 3, 5, 6, 8, 9};
  int x = 7;
  int floor = findFloor(arr, x);
  int ceil = findCeil(arr, x);
  cout << "The floor of " << x << " is " << floor << endl;
  cout << "The ceil of " << x << " is " << ceil << endl;
  return 0;
}

```

```
output :
The floor of 7 is 6
The ceil of 7 is 7
```

---

**Refer :**
[Lower Bound](./02-lower&upper-bound.md), [Binary Search](./01-binary-search.md).

---

**Solve it on :**

[Coding Ninjas](https://www.codingninjas.com/studio/problems/ceiling-in-a-sorted-array_1825401?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf)
