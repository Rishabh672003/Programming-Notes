## First Negative Number in every window of size k

**Problem Statement :**

You're given an array `arr` of size `n`, your task is to find the first negative integer in every window of size `k.`

---

**We'll use the concept of sliding window to solve this problem.**

```cpp
#include <bits/stdc++.h>
using namespace std;
vector<long long>printFirstNegative(int arr[], int n, int k){
    vector<long long> ans;
    queue<long long> list;
    int i = 0, j = 0;
    while(j < n){
        if(arr[j] < 0){
            list.push(arr[j]);
        } if(j - i + 1 < k){
            j++;
        } else if (j - i + 1 == k){
            if(list.size() == 0){
                ans.push_back(0);
            } else {
                ans.push_back(list.front());
                if (arr[i] == list.front()){
                    list.pop();
                }
            }
            i++; j++;
        }
    }
    return ans;
}
int main(){
    int t, i;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        for (i = 0; i < n; i++) {
            cin >> arr[i];
        }
        int k;
        cin >> k;

        vector<long long> ans = printFirstNegative(arr, n, k);
        for (auto it : ans) cout << it << " ";
        cout << endl;
    }
}
```

---

**Explanation :**

The code first initializes two variables: i and j. The variable i is used to track the index of the current element in the array, and the variable j is used to track the index of the next element to be added to the window.

The code then iterates over the array. On each iteration, the following steps are performed:

1. If the current element is negative, then it is added to the queue.

2. If the size of the window is equal to k, then the following steps are performed:

   If the queue is empty, then the output vector is appended with 0.

   Otherwise, the output vector is appended with the first element in the queue.

   The first element in the queue is removed.

   The index i is incremented by 1.

3. The index j is incremented by 1.

---

**Example :**

THe output for an input [-8, 2, 3, -6, 10] and window size 2 is [-8, 0, -6, -6].

The first window is [-8, 2]. The first negative integer in this window is -8, so it is appended to the output vector.

The second window is [2, 3]. There are no negative integers in this window, so 0 is appended to the output vector.

The third window is [3, -6]. The first negative integer in this window is -6, so it is appended to the output vector.

The fourth window is [-6, 10]. The first negative integer in this window is -6, so it is appended to the output vector.

---

**Analysis :**

The output of the code is the vector of the first negative integers in the sliding windows of size `k` in the array `arr`.

The time complexity of the code is **O(N)**, where N is the number of elements in the array. This is because the code iterates over the array once. The space complexity of the code is **O(k)**, where k is the size of the window. This is because the queue can store up to k elements.
