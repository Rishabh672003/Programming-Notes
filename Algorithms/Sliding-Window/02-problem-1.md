## Maximum sum of subarray with size k

**Flow** :

1. Problem Statement - Input - Output
2. Identification
3. Abstract
4. Actual Code

---

**Problem Statement :**
Given an array `arr` of size `n`, Find the maximum sum subarray with size k.

---

**Input :**

```cpp
int n = 7;
int arr[n] = {2, 5, 1, 8, 2, 9, 1};
k = 3 // window size.
```

---

**Output :**

Return an integer which is maximum sum among all the subarrays.

---

**Identificaion :**

We are given with an **array/string**, we're asked for a **subarray/substring** and either we have a window size [**fixed size window**] or a condition for window size [**variable size window**].

---

**Abstract :**

1. **How do we code the window ?**

   To design a window, we need something to represent it's **start** and somthing to represent it's **end**.

   Let's denote it's start with a pointer `i` and it's end by another pointer `j`.

   Then the size of window `k` can be given as `k = j - i + 1`

2. **How to begin ?**

   Initialize two pointers, `i` & `j` [start and end] with 0. `i = 0` and `j = 0`. Why 0? because initially start and end will be at same position.

   Then we'll check if our window size `j-i+1` is less than `k`, if it is, then we'll increase it's size by incrementing `j` untill it reaches `k`.

   We increase the size beacause, the only useful window size to us is of size k where we need to perform our calculation.

   If the size is less than k, we'll increase our `j` pointer and we'll check if the size reaches `k`.

3. **How we'll get the answer ?**

   Once we reach the condition `j-i+1 == k`, we'll then perform our calculation and we'll get our very first answer.

   At this moment we don't want to loose our window size, we'll maintain the window size by incrementing `i` and `j` simutaneously. And this is how our window will move / slide.

4. **Conclusion :**

   We'll initialise 2 pointers `i = 0` and `j = 0`, `i` denotes start, `j` denotes end, we'll increase the window size by moving the `j` pointer untill we hit the required size `k = j-i+1`, once we hit the requires size, we'll perform our calculation and maintain the size by incrementing `i` as `i++` and `j` as `j++`.

---

**Actual Code :**

```cpp
#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    long maximumSumSubarray(int k, vector<int> &arr , int n){
  int i = 0, j = 0;
  long long sum = 0;
  long long maxi = INT_MIN;

  while (j < n) {
    sum += arr[j];
    if (j - i + 1 < k) {
      j++;
    } else if (j - i + 1 == k) {
      maxi = max(maxi, sum);
      sum -= arr[i];
      i++;
      j++;
    }
  } return maxi;
    }
};

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int N,K;
        cin >> N >> K;;
        vector<int>Arr;
        for(int i=0;i<N;++i){
            int x;
            cin>>x;
            Arr.push_back(x);
        }
        Solution ob;
        cout << ob.maximumSumSubarray(K,Arr,N) << endl;
    }
    return 0;
}
```
