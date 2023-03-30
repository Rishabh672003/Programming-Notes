# Selection Sort

### Definition

**Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from an unsorted list and placing it at the beginning of the list. The algorithm maintains two sub-lists: a sorted sub-list that is built up from left to right at the front of the list, and an unsorted sub-list that contains the remaining elements to be sorted.**

<!-- # Example 1: Sorting a list of numbers -->

### Working

1. Set the first element of the list as the minimum value.
2. Compare the minimum value to the second element of the list. If the second element is smaller than the minimum value, set it as the new minimum value.
3. Repeat step 2 for every element in the list, until the end of the list is reached.
4. Swap the minimum value with the first element of the list.
5. Repeat steps 1-4 for the remaining unsorted sub-list.

### Implementation in C++

```cpp

#include <iostream>
using namespace std;

void selectionSort(int arr[], int n) {
    int i, j, min_idx;

    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        swap(arr[min_idx], arr[i]);
    }
}

int main() {
    int arr[] = {8, 3, 2, 7, 4, 6, 5, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSort(arr, n);
    cout << "Sorted array: \n";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    return 0;
}

```

**How will the above code will actually work**

| unsorted list          | sorted list            |
| ---------------------- | ---------------------- |
| 8, 3, 2, 7, 4, 6, 5, 1 |                        |
| 1, 3, 2, 7, 4, 6, 5, 8 | 1                      |
| 1, 2, 3, 7, 4, 6, 5, 8 | 1, 2                   |
| 1, 2, 3, 7, 4, 6, 5, 8 | 1, 2, 3                |
| 1, 2, 3, 4, 7, 6, 5, 8 | 1, 2, 3, 4             |
| 1, 2, 3, 4, 5, 6, 7, 8 | 1, 2, 3, 4, 5          |
| 1, 2, 3, 4, 5, 6, 7, 8 | 1, 2, 3, 4, 5, 6       |
| 1, 2, 3, 4, 5, 6, 7, 8 | 1, 2, 3, 4, 5, 6, 7    |
| 1, 2, 3, 4, 5, 6, 7, 8 | 1, 2, 3, 4, 5, 6, 7, 8 |

### Time and Space Complexity

The time complexity of selection sort is O(n^2), where n is the number of elements in the list. This means that the running time of the algorithm grows quadratically with the number of elements in the list.

In terms of space complexity, selection sort requires only a constant amount of extra space, since it operates directly on the input list without creating any additional data structures. Therefore, the space complexity of selection sort is O(1).

Although selection sort is not the most efficient sorting algorithm, its simplicity and low space requirements make it useful for small lists or as a building block in more complex algorithms.
