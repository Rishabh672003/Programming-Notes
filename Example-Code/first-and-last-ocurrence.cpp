#include <bits/stdc++.h>
using namespace std;

int firstOcc(int *arr, int size, int target) {
    int start = 0;
    int end = size - 1;
    int mid;
    int ans = -1;
    while (start <= end) {
        mid = start + (end - start) / 2;
        if (arr[mid] == target) {
            ans = mid;
            end = mid - 1;
        } else if (arr[mid] > target) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    return ans;
}

int lastOcc(int *arr, int size, int target) {
    int start = 0;
    int end = size - 1;
    int mid;
    int ans = -1;
    while (start <= end) {
        mid = start + (end - start) / 2;
        if (arr[mid] == target) {
            ans = mid;
            start = mid + 1;
        } else if (arr[mid] > target) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    return ans;
}

int main() {
    int arr[8] = {1, 2, 3, 3, 3, 3, 4, 5};
    cout << "First Occurrence at: " << firstOcc(arr, 8, 3) << endl;
    cout << "Last Occurrence at: " << lastOcc(arr, 8, 3);
    return 0;
}
