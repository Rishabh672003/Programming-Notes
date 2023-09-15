## First and Last occurrence of an element.

### First occurrence --> Lower Bound.

### Last occurrence --> Upper bound - 1.

---

**Implementation :**

```cpp
int lowerBound(vector<int> &arr, int n, int x){
    int low = 0, high = n - 1;
    int ans = n;
    while (low <= high){
        int mid = low + (high - low) / 2;
        if (arr[mid] >= x){
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
}

int upperBound(vector<int> &arr, int n, int x){
    int low = 0, high = n - 1;
    int ans = n;
    while (low <= high){
        int mid = low + (high - low) / 2;
        // maybe answer
        if (arr[mid] > x){
            ans = mid;
            // look for more small index in left
            high = mid - 1;
        } else {
            low = mid + 1; // look for right
        }
    }
    return ans;
}

pair<int, int> firstAndLastPosition(vector<int>& arr, int n, int k)
{
    int lb = lowerBound(arr, n, k);
    if (lb == n || arr[lb] != k) return {-1, -1};
    return {lb, upperBound(arr, n, k) - 1};
}

int main() {
  vector<int> arr = {1, 3, 5, 5, 5, 5, 7, 8, 9};
  int k = 5;
  pair<int, int> result = firstAndLastPosition(arr, arr.size(), k);
  cout << "The first and last position of " << k << " in the array are " << result.first << " and " << result.second << endl;
  return 0;
}
```

```
Output :
The first and last position of 5 in the array are 2 and 5
```
