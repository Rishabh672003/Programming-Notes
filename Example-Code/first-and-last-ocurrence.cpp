#include <iostream>

using namespace std;

int firstOccurrence(int arr[], int n, int x) {
  int low = 0;
  int high = n - 1;
  int firstOcc = -1;

  while (low <= high) {
    int mid = low + (high - low) / 2;

    if (arr[mid] == x) {
      firstOcc = mid;
      high = mid - 1;
    } else if (arr[mid] < x) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return firstOcc;
}

int lastOccurrence(int arr[], int n, int x) {
  int low = 0;
  int high = n - 1;
  int lastOcc = -1;

  while (low <= high) {
    int mid = low + (high - low) / 2;

    if (arr[mid] == x) {
      lastOcc = mid;
      low = mid + 1;
    } else if (arr[mid] < x) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return lastOcc;
}

int main() {
  int arr[] = {1, 2, 2, 2, 2, 3, 4, 7, 8, 8};
  int n = sizeof(arr) / sizeof(arr[0]);
  int x = 2;

  int firstOcc = firstOccurrence(arr, n, x);
  int lastOcc = lastOccurrence(arr, n, x);

  if (firstOcc == -1) {
    cout << "Element not found" << endl;
  } else {
    cout << "First occurrence of " << x << " is at index " << firstOcc << endl;
    cout << "Last occurrence of " << x << " is at index " << lastOcc << endl;
  }

  return 0;
}