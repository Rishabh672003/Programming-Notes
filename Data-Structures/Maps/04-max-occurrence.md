## Find the Maximum Occurence of an element in an array using unorderd map.

**Concept :**
An unordered map is an associative array in C++ that stores elements in a hash table. The elements are not sorted in any particular order, but are instead accessed by their unique keys.

This makes unordered maps very efficient for accessing individual elements, but less efficient for iterating over all the elements in the map.

Here is an example of how to create an unordered map in C++:

```cpp
unordered_map<int, int> um;
```

---

```cpp
#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  int arr[] = {1, 2, 3, 2, 1, 2, 5, 2};
  int n = sizeof(arr) / sizeof(arr[0]);

  // Create an unordered_map
  // to store the frequency of each element

  unordered_map<int, int> um;

  // Iterate over the array and update
  // the frequency of each element in the map.

  for (int i = 0; i < n; i++) {
    um[arr[i]]++;
  }

  // Find the element with the maximum frequency

  int max_element = 0, max_count = 0;
  for (auto it = um.begin(); it != um.end(); it++) {
    if (it->second > max_count) {
      max_element = it->first;
      max_count = it->second;
    }
  }

  // Print the element with the maximum frequency

  cout << "Element with maximum occurrence is " << max_element << ", With count :" << max_count << endl;

  return 0;
}
```

---

### Breakdown :

- The `unordered_map` data structure is used to store the frequency of each element in the array. The key of the map is the element and the value is the frequency of the element.

- The for loop iterates over the array and updates the frequency of each element in the map. The `um[arr[i]]++` statement increments the frequency of the element `arr[i]` in the map.

- The `max_element` and `max_count` variables are used to store the element with the maximum frequency and its count, respectively.

- The for loop iterates over the map and finds the element with the maximum frequency. The `it->second > max_count` statement checks if the frequency of the current element is greater than the maximum count. If it is, then the current element is assigned to `max_element` and its frequency is assigned to `max_count`.

- The cout statement prints the element with the maximum frequency.

---

### Let's visualize the statement `um[arr[i]]++`.

The statement `um[arr[i]]++` is a shorthand for the following:

```cpp
um.find(arr[i]) -> second++;
```

This statement first finds the element `arr[i]` in the map `um`. If the element is **not found**, then it is **added** to the map with a value of 1.

If the element is **found**, then its **value** is **incremented** by 1.

To visualize this, let's say we have an unordered map `um` that maps integers to their frequencies. The initial state of the map is:

```
um = {
  1: 0,
  2: 0,
  3: 0,
  ...
}
```

Now, let's say we execute the statement `um[arr[i]]++` for the array `arr[] = {1, 2, 3, 3}`.

The first time this statement is executed, it will find the element 1 in the map. The value of 1 in the map is incremented by 1, so the map becomes:

```
um = {
1: 1,
2: 0,
3: 0,
...
}
```

The second time this statement is executed, it will find the element 2 in the map. The value of 2 in the map is incremented by 1, so the map becomes:

```
um = {
1: 1,
2: 1,
3: 0,
...
}
```

The third time this statement is executed, it will find the element 3 in the map. The value of 3 in the map is incremented by 1, but since the element 3 is not in the map, it is added to the map with a value of 1.

So the final state of the map is:

```
um = {
1: 1,
2: 1,
3: 1,
...
}
```

Now, the element 3 comes again, so the value of 3 will be updated to 2.

```
um = {
1: 1,
2: 1,
3: 2,
...
}
```

**Hence the most occured element here becomes 3.**
