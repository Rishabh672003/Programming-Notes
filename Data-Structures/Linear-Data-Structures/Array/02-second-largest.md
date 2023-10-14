## Find Second largest element in the array

Approach :

1. Brute : Sort --> Traverse from n - 2 --> if (a[i] != largest) ==> secondLargest == a[i]

   Time Complexity : O(N Log N) + N ==> [Sort + Traversal]

Code :

```cpp
int secondLargest(vector<int> &arr, int n){
    int secondLargest = -1;
    sort(arr.begin(), arr.end()); // O(N Log N)
    for (int i = n - 2; i >= 0; i++) { // O(N)
        if (arr[i] != largest) {
            secondLargest = arr[i];
        }
    }
    return secondLargest;
}
```

2. Better : Traverse for Largest --> set SecondLargest = -1 --> Traverse again --> if (arr[i] > SecondLargest and arr[i] != largest) ==> secondLargest == a[i]

   Time Complexity : O(2N) ==> [Two Traversals]

Code :

```cpp
int secondLargest(vector<int> &arr, int n){
    int largest = arr[0];
    int secondLargest = -1;
    for (int i = 0; i < n; i++){ // O(N)
        if (arr[i] > largest){
            largest = arr[i];
        }
    }
    for (int i = 0; i < n; i++){ // O(N)
        if (arr[i] > secondLargest && arr[i] != largest){
            secondLargest = arr[i];
        }
    }
    return secondLargest;
}
```

3. Optimal : set FirstElement to Largest, set SecondLargest = -1 --> Traverse from 0 to n --> if found an a[i] > Largest ==> SecondLargest == Largest and Largest == arr[i] --> else if found an a[i] < largest but a[i] > SecondLargest ==> SecondLargest == a[i]

   Time Complexity : O(N) ==> [Single Traversal]

Code :

```cpp
int secondLargest(vector<int> &arr, int n){
    int largest = arr[0];
    int secondLargest = -1;
    for (int i = 0; i < n; i++){ // O(N)
        if (arr[i] > largest){
            secondLargest = largest;
            largest = arr[i];
        } else if (arr[i] < largest && arr[i] > secondLargest){
            secondLargest = arr[i];
        }
    }
    return secondLargest;
}
```

---

### Bonus : Find Second Smallest

```cpp
int secondLargest(vector<int> &arr, int n){
    int smallest = arr[0];
    int secondSmallest = INT_MAX;
    for (int i = 0; i < n; i++){
        if (arr[i] < smallest){
            secondSmallest = smallest;
            smallest = arr[i];
        } else if (arr[i] != smallest && arr[i] < secondSmallest){
            secondSmallest = arr[i];
        }
    }
    return secondSmallest;
}
```
