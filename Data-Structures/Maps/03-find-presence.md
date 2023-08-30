## Find Presence of an element in an array.

```cpp
#include <bits/stdc++.h>
using namespace std;

map<int, bool> elementMap;

void buildMap(vector<int>& arr){
    for (int i = 0; i < arr.size(); ++i){
        // making a key value pair.
        elementMap[arr[i]] == i;
        // store index of each element.
    }
}

int findElementIndex(int target){
    if (elementMap.find(element) != elementMap.end()){
        return elementMap[target];
    } else return -1;
}

int main(){

    vector<int> arr = {10, 25, 30, 15, 20};
    int target = 3;

    buildMap(arr);
    int index = findElement(target);

    if (index != -1) {
        cout << "Element " << elementToFind << " found at index " << index << endl;
    } else {
        cout << "Element " << elementToFind << " not found in the array." << endl;
    }

    return 0;
}

```

---

### Let's Breakdown the code :

**Step 1.** `buildMap()` --> **Building the map :**

```cpp
void buildMap(vector<int>& arr){
    for (int i = 0; i < arr.size(); ++i){
        // making a key value pair.
        elementMap[arr[i]] == i;
        // store index of each element.
    }
}
```

- When buildMap is called, it iterates through the array and for **each element, it stores the element as a key in the elementMap and associates it with its index.**

- Here's how the elementMap looks after each iteration:

```
After processing 10: {10: 0}

After processing 25: {10: 0, 25: 1}

After processing 30: {10: 0, 25: 1, 30: 2}

After processing 15: {10: 0, 25: 1, 30: 2, 15: 3}

After processing 20: {10: 0, 25: 1, 30: 2, 15: 3, 20: 4}
```

---

Expading `elementMap[arr[i]] == i;`

The line `elementMap[arr[i]] = i;` is used to insert a key-value pair into the map. Let's break it down step by step:

- `arr[i]`: This is the element at the current index `i` in the array arr.

- `elementMap[arr[i]]:` This part is using the value of arr[i] as the key for the map.

- `i`: This is the index of the current element in the array.

When you put it all together, `elementMap[arr[i]] = i;` is storing the index i in the map with the key being the value of `arr[i]`.

Here's a visual representation of how the process works with a small example:

Let's say you have the array `arr = [10, 25, 30]`:

- When `i = 0`, `arr[i]` is 10, and `elementMap[10]` is assigned the value 0 (the index of 10 in the array).

  elementMap becomes `{10: 0}`

- When `i = 1`, `arr[i]` is 25, and `elementMap[25]` is assigned the value 1 (the index of 25 in the array).

  elementMap becomes `{10: 0, 25: 1}`

---

Step 2: `findElementIndex()` --> **Finding index of target :**

```cpp
int findElementIndex(int target){
    if (elementMap.find(element) != elementMap.end()){
        return elementMap[target];
    } else return -1;
}
```

- When you call `findElementIndex(30)`, the map is checked for the key 30.

- Since 30 exists in the map, the condition `elementMap.find(element) != elementMap.end()` is `true`.

- The index of 30 is 2, so the function returns 2.

- When you call `findElementIndex(99)`, the map is checked for the key 99.

- Since 99 doesn't exist in the map, the condition is false.

- The function returns -1, indicating that the element is not found.

---

### Solution 2 :

```cpp
#include <iostream>
#include <map>

using namespace std;

int search(int arr[], int N, int X) {
  map<int, int> mp;
  for (int i = 0; i < N; ++i) {
    mp[arr[i]] = i;
  }
  auto iterator = mp.find(X);
  if (iterator != mp.end()) {
    return iterator -> second;
  } else {
    return -1;
  }
}

int main() {
  int arr[] = {1, 2, 3, 4};
  int N = sizeof(arr) / sizeof(arr[0]);
  int X = 3;
  int index = search(arr, N, X);
  cout << index << endl;
  return 0;
}

```

Explanation :

- `auto iterator = mp.find(X)`:

  This line creates an iterator that points to the element in the map that has the key X.

  The `find()` method returns an iterator to the first element in the map that has the given key.

  If the key is not found, the `find()` method returns an iterator to the end of the map.

- `if (iterator != mp.end())`:

  This line checks if the iterator is not pointing to the end of the map.

  If it is not pointing to the end of the map, then the element with the key X is found in the map.

- `return iterator -> second`:

  This line returns the second element of the pair pointed to by the iterator it.

  In this case, the iterator it is pointing to the element in the map that has the key X.

  The `second` element of this pair is the index of the element in the array, so the expression `iterator -> second` returns the index of the element that is equal to X.
