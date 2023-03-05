# PPS Notes Module 5

## Arrays and Strings

### Arrays

- #### What are arrays?

  - It is a derived data type
  - Collection of similar type of elements that is of same type
  - stored in continuous memory location
  - fixed size once its created
  - Instead of declaring individual variables, such as A0,
    A1,A2,….A99, you declare one array variable such as A[100]
    and use A[0], A[1], and ..., A[99] to represent individual
    variables.
  - Array index starts with 0 and ends with size-1.

- #### Array declaration
  - To declare an array in C, a programmer specifies the type of
    the elements, and the number of elements required by an
    array as follows:
    ```c
    data_type array_name[array_size];
    ```
  - This is a single dimension array, array size must be a positive integer
    data type can be any, examples of array declaration -
    ```c
    double balance[10];
    int A[10];
    ```
- #### Array initialization

  - `int a[5] = {100, 200, 300, 400, 500}`
  - The number of values between braces {} cannot be larger than the number
    of elements that we declare for the array between square brackets [ ].

- #### Accessing Array elements
  - An element is accessed by indexing the array name.
    ```c
    int num = A[4];
    ```
  - To read Array elements
    ```c
    for(i=0; i < size; i++){
        scanf("%d", &A[i]);
    }
    ```
  - To display array elements
    ```c
    for(i=0; i < size; i++ ){
        printf("%d", A[i]);
    }
    ```
- #### 2d Array

  - `int A[3][3]` will make an array of 3 x 3 that is a matrix of 3x3
  - It will look like this
  - ![image](https://user-images.githubusercontent.com/53911515/214111673-32d2c764-ea91-437a-b1b5-66bf039ee02b.png)
    - 2D array declaration
    - `int A[][] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}`
  - To read 2D array elements
    ```c
    for(i=0;i<row;i++){
      for(j=0;j<col;j++){
        scanf("%d",&A[i][j]);
      }
    }
    ```
  - To display 2-D array elements

  ```c
  for(i=0;i<row;i++){
    for(j=0;j<col;j++){
      printf("%d\t",A[i][j]);
    }
    printf("\n");
  }
  ```

- ## Add 2 matrix of size m x n

  ```c
  #include <stdio.h>
  int main() {
    int a[2][3], b[2][3], c[2][3], i, j;
    printf("\nENTER VALUES FOR MATRIX A:\n");
    for (i = 0; i < 2; i++)
      for (j = 0; j < 3; j++)
        scanf("%d", &a[i][j]);
    printf("\nENTER VALUES FOR MATRIX B:\n");
    for (i = 0; i < 2; i++)
      for (j = 0; j < 3; j++)
        scanf("%d", &b[i][j]);
    for (i = 0; i < 2; i++)
      for (j = 0; j < 3; j++)
        c[i][j] = a[i][j] + b[i][j];
    printf("\nTHE VALUES OF MATRIX C ARE:\n");
    for (i = 0; i < 2; i++) {
      for (j = 0; j < 3; j++)
        printf("%5d", c[i][j]);
      printf("\n");
    }
  }
  ```

### Strings

- #### What are Strings
  - Strings in C are represented by One- dimensional Character Arrays
  - An array formed by characters is a string in C.
  - The end of the string is marked with a special character, the null
    character The null character is represented by character escape sequence,
    '\0'.
- #### String declaration
  - Strings can be declared like one-dimensional arrays.
    `data_type string_name[size]`
  - examples
   ```c
  char str[5];
  char name[10];
   ```
