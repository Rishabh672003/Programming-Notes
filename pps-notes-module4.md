# PPS Notes Module 4

## Functions

- A ‘C’ program is made up of one or more functions.
- All C programs contain at least one function, called main() where
  execution starts.

- ### Advantages

  - Modular programming
  - Source code length can be reduced
  - can be called as many times as you like

- ### Types of function

  - Library Built in functions written in header files like -
    - stdio.h
    - Ctype.h
    - math.h
    - stdlib.h

- #### Call by value and Call by reference

  - On the basis of arguments there are two types of function are available in C
    language, they are If a function take any arguments, it must declare variables that
    accept the values as a arguments. These variables are called the formal parameters of the function. There are two
    ways to pass value or data to function in C language which is given below

    • Call by value

    • Call by reference

  - Call by value
    - in this the original value cant be changed or modified
    - when the value is modified its for local or caller function only
      and not the original function.
  - Call by reference
    - in this the original value is changed or modified because we pass
      the address to the variable like with `type *var name`
    - value is modified in the original function also.
  - #### differences between them
    ![image](https://user-images.githubusercontent.com/53911515/214080799-b3e400d4-59a9-416c-b085-d62d4e7feab1.png)

- ### Parts of function

  - #### Function prototype/ declaration.
    `void add();`
    - specify the value that needs to be returned from the function
    - defined before function call
  - #### Function call.
    `add();`
    - calls the function with the parameters
  - #### Function definition / body.
    ```c
    void add()
    {
    int a=10,b=20,c;
    printf(“Sum=%d”,a+b)
    }
    ```
    - independent program module
    - specifies what function needs to do
    - Syntax
      ```c
      return_type function name(formal_parameter list){
          function_body
      }
      ```
  - #### Sample function call
    ```c
    #include <stdio.h>
    void main(){
        printf("hello world");
    }
    ```
  - ##### Four types of function

    - no arguments and no returns
    - arguments but no return
    - no arguments and return
    - arguments and return

  - ## Function to check whether a number is prime or not

    ```c
    #include<stdio.h>
    void prime(int n);
    void main()
    {
      char c;
      int n;
      printf("Enter a positive integer: ");
      scanf("%d",&n);
      prime(n);
    }

    void prime(int n){
      int i,count=0;
      for(i=1; i<=n; i++) {
        if(n%i==0)
        count++;
      }
      if(count==2)
        printf("\n%d is a prime number.", n);
      else
        printf("\n%d is not a prime number.", n);
    }
    ```

    ## Program for Armstrong number using function between ranges

    ````c
    #include <stdio.h>
    void armstrong(int n);
    int main() {
      char c;
      int n;
      for (n = 100; n <= 999; n++)
        armstrong(n);
    }
    void armstrong(int n) {
      int sum = 0, rem, temp;
      temp = n;
      while (n != 0) {
        rem = n % 10;
        sum += rem * rem * rem;
        n /= 10;
      }
      if (sum == temp)
        printf("\n%d.", n);
    }
    ````

  - #### Recursion

    - A function that calls itself is known as recursive
      function and this technique is known as recursion
      in C programming.
    - Simple example
      ```c
      void main(){
          print("somethig");
          main();
      }
      ```
    - ### program to calculate the factorial

      ```c
      #include <stdio.h>

      int factorial(int);
      int main() {
        int n, f;
        printf("Enter the no");
        scanf("%d", &n);
        f = factorial(n);
        printf("\n Factorial of %d = %d", n, f);
      }
      int factorial(int x) {
        if (x == 1 || x == 0)
          return 1;
        else
          return x * factorial(x - 1);
      }
      ```

    - ### function to calculate the fibonacci series
      ```c
        #include <stdio.h>
        void fibonacci(int);
        int main() {
          int k, n;
          int i = 0, j = 1, f;
          printf("Enter the range of the Fibonacci series: ");
          scanf("%d", &n);
          printf("Fibonacci Series: ");
          printf("%d %d ", 0, 1);
          fibonacci(n);
        }
        void fibonacci(int n) {
          static int first = 0, second = 1, sum;
          if (n > 0) {
            sum = first + second;
            first = second;
            second = sum;
            printf("%ld ", sum);
            fibonacci(n - 1);
          }
        }
      ```

  - ### Differences between recursion and iteration
    ![image](https://user-images.githubusercontent.com/53911515/214092152-39384ba3-1fe4-4a98-9da8-f0f494407c7e.png)
