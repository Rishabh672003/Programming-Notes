# Linear Search
*Searching Elements in Contigious Linear Data Structure.*

__Time Complexity:__
1. Best Case: O(1) --> Element found at 1st comparison.
2. Average / Worst Case: O(n) --> for n comparisons. (where n is the size of array)

# Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

int linearSearch(int arr[], int n, int x)
{
    // loop through each element in the array
    for (int i = 0; i < n; i++)
    {
        // if the current element matches the search value, return the index
        if (arr[i] == x)
        {
            return i;
        }
    }
    // if the search value is not found in the array, return -1
    return -1;
}

int main()
{
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 30;

    int index = linearSearch(arr, n, x);
    if (index == -1)
    {
        cout << "Element not found" << endl;
    }
    else
    {
        cout << "Element found at index " << index << endl;
    }

    return 0;
}

```
