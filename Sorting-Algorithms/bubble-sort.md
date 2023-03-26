# Bubble Sort

**Bubble sort is a simple sorting algorithm that repeatedly steps through a list of elements to be sorted, compares each pair of adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.**

### Working

Here is an example of how bubble sort works on a list of numbers:

1. Compare the first two elements. If the first element is greater than the second element, swap them.
2. Move to the next pair of elements (second and third) and repeat step 1.
3. Continue to compare and swap adjacent elements until the end of the list is reached.
4. Repeat steps 1-3 until no more swaps are needed.

### Implementation in C++

```cpp
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}

```

we define a function called bubbleSort that takes an array of integers and the size of the array as its arguments. The function then uses nested loops to compare adjacent elements in the array and swap them if they are in the wrong order. This process is repeated until the entire array is sorted.

### Time and Space Complexity of Bubble Sort

The time complexity of bubble sort is O(n^2), where n is the number of elements in the array. This means that the time taken by the algorithm to sort an array grows quadratically with the size of the input data. Specifically, in the worst case scenario where the array is already sorted in reverse order, the algorithm will take n\*(n-1)/2 comparisons and swaps to sort the array. In the average case, it will take about the same number of comparisons and swaps.

The space complexity of bubble sort is O(1), which means that the amount of memory required by the algorithm remains constant regardless of the size of the input data. This is because bubble sort only requires a few variables to keep track of the current state of the algorithm, such as the indices of the elements being compared, and a temporary variable used for swapping elements.
