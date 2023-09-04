## Find the maximum Occurring number.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    // create an unordered_map to store the frequencies of the elements
    unordered_map<int, int> mp;
    for(int i = 0; i < n; i++){
        mp[arr[i]]++;
    }

    // find the maximum value in the map
    int max_val = -1;
    int max_key = -1;

    for(auto it = mp.begin(); it != mp.end(); it++){
        if(it->second > max_val){
            max_val = it->second;
            max_key = it->first;
        }
    }

    // print the maximum occurring number
    cout << max_key << " -> " << max_val << endl;

    return 0;
}
```

```
Output:

5  --> size of array
1 1 1 2 3  --> array elements
1 -> 3  --> most occurred value -> how many times it occurred.
```

---

### Explanation :

- In this code, the mp `unordered_map` is used to store the frequencies of the elements in the `arr` array.

- The `max_val` variable is used to store the maximum value in the map and the `max_key` variable is used to store the key corresponding to the maximum value.

- The for loop iterates over the `mp` map and finds the maximum value.

- `it->first` is the key, `it->second` is the value of that particular iterator value.

- The maximum occurring number and it's occurrence is then printed.
