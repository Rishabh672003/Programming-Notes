# Arrays

### Basic definition

In C++, an array is a collection of elements of the same type that are stored sequentially in memory. Each element in an array can be accessed using an index value, which starts at 0 for the first element and increments by 1 for each subsequent element.

### Initializing an array

First you define the type of each element in the array, and then you initialize the array with its name and number of elements in the array

```cpp
int arr[5]; // defines an array of 5 integers
string arr[5]; // defines an array of 5 strings
```

OR

```cpp
int arr[5] = {1,2,3,4,5}
string arr[5] = {"a","b","c","d","e"}

```

You access the elements of an array using the index value, which starts at 0 for the first element and increments by 1 for each subsequent

```cpp
int x = arr[0]; // access the first element of the array
int y = arr[1]; // access the second element of the array
int z = arr[2]; // access the third element of the

```

##### Note that in C++, arrays do not perform bounds checking, so it is possible to access elements outside the bounds of the array. This can lead to undefined behavior, so it's important to be careful when working with arrays to ensure that you stay within the bounds of the array.

### Size of Array

```cpp
int arr[2] = {2,7};
int arrSize = sizeof(arr)/sizeof(int); // That is 8 / 4 = 2.
cout<<" Size of array is " << arrSize <<endl;
```

### Array & Functions.

```cpp
void printArray(int arr[], int size) {
  cout<< " printing the array " << endl;
  for(int i =0; i<size; i++) {
      cout << arr[i] << " ";
  }
}
```

### Array Algorithms:

- 1. Linear Search.

  ```cpp

  #include <bits/stdc++.h>
  using namespace std;

  bool isPresent(int *arr, int size, int key)
  {

      for (int i = 0; i < size; i++)
      {
          if (arr[i] == key)
          {
              return 1;
          }
      }
      return 0;
  }

  int main()
  {
      int arr[7] = {3, 4, 5, 67, -9, 1, 0};
      int key;
      cout << "Enter Number to be found: ";
      cin >> key;
      bool found = isPresent(arr, 7, key);

      if (found)
          cout << "Present!" << endl;
      else
          cout << "Not Found!" << endl;

      return 0;
  }

  ```

- 2. Binary search.

  ```cpp
  #include<iostream>
  using namespace std;

  int binarySearch(int arr[], int size, int key) {

      int start = 0;
      int end = size-1;

      int mid = start + (end-start)/2;

      while(start <= end) {

          if(arr[mid] == key) {
              return mid;
          }

          //go to right wala part
          if(key > arr[mid]) {
              start = mid + 1;
          }
          else{ //key < arr[mid]
              end = mid - 1;
          }

          mid = start + (end-start)/2;
      }

      return -1;
  }


  int main() {

      int even[6] = {2,4,6,8,12,18};
      int odd[5] = {3, 8, 11, 14, 16};

      int evenIndex = binarySearch(even, 6, 6);

      cout << " Index of 6 is " << evenIndex << endl;

      int oddIndex = binarySearch(odd, 5, 14);

      cout << " Index of 14 is " << oddIndex << endl;


      return 0;
  }

  int findPeak(int arr[], int n) {

      int s =0, e = n-1;
      int mid = s + (e-s)/2;

      while(s<e) {
          //cout<<" s " << s <<" e " << e << endl;
          if(arr[mid] < arr[mid+1]){
              s = mid+1;
          }
          else{
              e = mid;
          }
          mid = s + (e-s)/2;
      }
      return s;
  }
  ```

- 3. Reverse an Array.

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  void revArray(int arr[], int size)
  {
      int start = 0;
      int end = size - 1;

      while (start <= end)
      {
          swap(arr[start], arr[end]);
          start++;
          end--;
      }
  }

  void printArr(int arr[], int size)
  {
      for (int i = 0; i < size; i++)
      {
          cout << arr[i] << " ";
      }
  }

  int main()
  {
      int even[6] = {1, 2, 3, 4, 5, 6};
      int odd[5] = {1, 2, 3, 4, 5};
      revArray(even, 6);
      revArray(odd, 5);

      printArr(even, 6);
      cout << endl;
      printArr(odd, 5);

      return 0;
  }
  ```

- 4. Find Duplicate Element.

  ```cpp
  #include <bits/stdc++.h>
  using namespace std;

  int findUnique(int a[], int size)
  {
      sort(a, a + size); // Time Complexity O(nLogn)

      int duplicate = a[0];

      for (int i = 1; i < size; i++)
      {
          if (a[i] == a[i - 1])
          {
              duplicate = a[i];
              break;
          }
      }

      return duplicate;
  }

  int main()
  {
      int a[7] = {1, 2, 3, 4, 5, 6, 6};
      int size = sizeof(a) / sizeof(a[0]);

      int duplicate = findUnique(a, size);

      cout << "The Duplicate element in the array is: " << duplicate << endl;

      return 0;
  }
  ```

- 5. Sort 0 1

  ```cpp
  // 0 0 1 1 2 2...

  #include <bits/stdc++.h>
  using namespace std;

  void printArray(int *arr)
  {
      for (int i = 0; i < 10; i++)
      {
          cout << arr[i] << " ";
      }
      cout << endl;
  }

  void swap1(int *arr)
  {
      int left = 0, right = 9; //  right == size - 1
      while (left < right)     // start from arr[i] till arr[n-1]
      {
          // shift all 0's to left and 1's to right
          while (arr[left] == 0 && left < right)
              left++; // If Left Already 0 then update index.

          while (arr[right] == 1 && left < right)
              right--; // If right Already 1 then update index.

          if (left < right)
              swap(arr[left], arr[right]);
          left++;
          right--;
      }
      printArray(arr);
  }

  int main()
  {
      int arr[10] = {1, 1, 0, 0, 1, 0, 0, 1, 1, 1};
      // METHOD 1: Sort --> O(nLogn)
      sort(arr, arr + 7);
      printArray(arr);

      // METHOD 2: Swap --> O(n)
      swap1(arr);

      return 0;
  }
  ```

- 6. Array Min/Max

  ```cpp
  #include<iostream>
  using namespace std;

  int getMin(int num[], int n) {

      int mini = INT_MAX;

      for(int i = 0; i<n; i++) {

          mini = min( mini, num[i]);

          //if(num[i] < min){
          //    min = num[i];
          //}
      }

      //returning min value
      return mini;
  }

  int getMax(int num[], int n) {

      int maxi = INT_MIN;

      for(int i = 0; i<n; i++) {

          maxi = max(maxi, num[i]);

         // if(num[i] > max){
           //   max = num[i];
         // }
      }

      //returning max value
      return maxi;
  }

  int main() {

      int size;
      cin >> size;

      int num[100];

      //taking input in array
      for(int i = 0; i<size; i++) {
          cin >> num[i];
      }

      cout << " Maximum value is " << getMax(num, size) << endl;
      cout << " Minimum value is " << getMin(num, size) << endl;

      return 0;
  }
  ```

- 7. Swap Alternate.

  ```cpp
  #include<iostream>
  using namespace std;

  void printArray(int arr[], int n) {

      for(int i = 0; i<n; i++ ) {
          cout<< arr[i] <<" ";
      }cout<<endl;

  }

  void swapAlternate(int arr[], int size) {

      for(int i = 0; i<size; i+=2 ) {
          if(i+1 < size) {
              swap(arr[i], arr[i+1]);
          }
      }

  }

  int main() {

      int even[8] = {5,2,9,4,7,6,1,0};
      int odd[5] = {11, 33, 9, 76, 43};

      swapAlternate(even, 8);
      printArray(even, 8);

      cout << endl;

      swapAlternate(odd, 5);
      printArray(odd, 5);

      return 0;
  }
  ```
