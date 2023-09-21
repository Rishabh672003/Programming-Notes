## Find Lower and Upper bound in an array.

### Lower Bound :

If we have a sorted array `arr` and a target element `x` which is supposed to be found in that array, then a Lower bound is the **Smallest** `index` in that array such that,

```cpp
arr[index] >= x;
```

---

**Example :**

```cpp
int arr[6] = {1, 2, 4, 4, 5, 7};
int x = 4; // element to be found in array
```

If we iterate over the array, we can find that 4 >= 4, 4 >= 4, 5 >= 4 and 7 >= 4. But the first occurence of 4 at index 2 satisfies the condition as it is `>=` the target element and it's index is the smallest of all.

**Hence, The Lower bound of this array is 2.**

---

### Upper Bound :

If we have a sorted array `arr` and a target element `x` which is supposed to be found in that array, then an Upper bound is the **Smallest** `index` in that array such that,

```cpp
arr[index] > x; // note the sign here
```

---

**Example :**

```cpp
int arr[6] = {1, 2, 4, 4, 5, 7};
int x = 4; // element to be found in array
```

If we iterate over the array, we can find that 5 > 4 and 7 > 4. But the value 5 at index 4 satisfies the condition as it is `>` the target element and it's index is the smallest of all.

**Hence, The upper bound of this array is 4.**

---

**Note :** There could be an edge case where no such target element exists or which satisfies `arr[index] >= target` or `arr[index] > target`, then we will return the nth element of the array because, then it would the hypothetical lower or upper bound for that array.

**Example :**

```cpp
int arr[6] = {1, 2, 4, 4, 5, 7};
int x = 7;
/*
this x value would have upper bound == 6,
as no element is > than 7
*/
```

---

**Implementation :**

```cpp
#include <bits/stdc++.h>
using namespace std;

int lowerBound(vector<int> &arr, int n, int x){
    int low = 0, high = n - 1;
    int ans = n;
    while (low <= high){
        int mid = low + (high - low) / 2;
        // maybe answer
        if (arr[mid] >= x){
            ans = mid;
            // look for more small index in left
            high = mid - 1;
        } else {
            low = mid + 1; // look for right
        }
    }
    return ans;
}

int upperBound(vector<int> &arr, int n, int x){
    int low = 0, high = n - 1;
    int ans = n;
    while (low <= high){
        int mid = low + (high - low) / 2;
        // maybe answer
        if (arr[mid] > x){
            ans = mid;
            // look for more small index in left
            high = mid - 1;
        } else {
            low = mid + 1; // look for right
        }
    }
    return ans;
}

int main(){
    int n; cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++>){
        cin >> arr[i];
    }
    int x; cin >> x;
    cout << "Lower Bound : " << lowerBound(arr, n, x);
    cout << "Upper Bound : " << upperBound(arr, n, x);
    return 0;
}
```

---

**Solve it on :**

[Coding Ninjas - Lower Bound](https://www.codingninjas.com/studio/problems/lower-bound_8165382?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf) & [Upper Bound](https://www.codingninjas.com/studio/problems/implement-upper-bound_8165383?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf)
