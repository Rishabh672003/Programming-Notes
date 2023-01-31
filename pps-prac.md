# Code for PPS practical

## **This only contains code that was done in PPS practical and no others**

## And only those which i though were somewhat difficult i haven't included the very easy one which anyone can do

## I dont guarantee that only these code will come in practical any other can also come

## Prac 2

### to swap two vars without a temp var

```c
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int a, b;
    scanf("%i%i", &a, &b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("%i %i", a, b);
    return 0;
}
```

## Prac 3

### To find roots of the quadratic equation

**execute with `-lm` flag on linux**

```c
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int a, b, c, d;
    double root1, root2;
    printf("this program will find the roots of the ax^2+bx+c=0");
    printf("enter a, b and c\n");
    scanf("%i%i%i", &a, &b, &c);
    d = b * b - 4 * a * c;

    if (d < 0) {
        double e = -(b) / (double)(2 * a);
        double f = sqrt(-d) / 2 * a;
        printf("first root = %.2lf + i%.2lf\n", e, f);
        printf("second root = %.2lf - i%.2lf\n", e, f);
    }

    else {
        root1 = (-b + sqrt(d)) / (2 * a);
        root2 = (-b + sqrt(d)) / (2 * a);
        printf("first root= %.2lf\n", root1);
        printf("second root= %.2lf\n", root2);
    }
    return 0;
}
```

### Whether input is number or uppercase or lowercase

```c
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char a;
    scanf("%c", &a);
    if (islower(a)) {
        printf("lowercase character");
    } else if (isupper(a)) {
        printf("uppercase character");
    } else if (isdigit(a)) {
        printf("number");
    } else {
        printf("special");
    }
    return 0;
}
```

## Prac 4

### prob 1

### To find the sum of 1/1! + 1/2! + 1/3! + .... + 1/n!

```c
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int i, fact, j;
    int n;
    float sum;
    printf("Enter the value of N :");
    scanf("%d", &n);
    sum = 0.0f;
    for (i = 1; i <= n; i++) {
        fact = 1;
        for (j = 1; j <= i; j++) {
            fact = fact * j;
        }
        sum = sum + ((float)1 / (float)fact);
    }
    printf("sum of series is : %f\n", sum);
    return 0;
}
```

### Prob 2

![image](https://user-images.githubusercontent.com/53911515/215794827-ea48fdf5-85e7-450e-955c-c552980be5d2.png)

```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 4; i++) {
        // inner loop to print spaces
        for (int j = 4; j >= i; j--) {
            printf("  ");
        }
        // inner loop to print numbers
        for (int k = 1; k <= i; k++) {
            printf("%d ", k);
        }
        // inner loop to print alphabets
        int m = 65;
        for (int l = 2; l < i; l++) {
            printf("%c ", (char)m);
            m++;
        }
        printf("\n");
    }
    return 0;
}
```

## Prac 5

- ### expt 1 - armstrong number

```c
#include <stdio.h>

int isarmstrong(int num);
void printarmstrong(int start, int end);

int main() {
    int start, end;

    printf("Enter lower limit to print armstrong numbers: ");
    scanf("%d", &start);
    printf("Enter the upper limit to print armstrong: ");
    scanf("%d", &end);
    printf("All armstrong numbers between %d to %d are: \n", start, end);
    printarmstrong(start, end);
    return 0;
}

int isarmstrong(int num) {
    int temp, lastdigit, sum;
    temp = sum;
    sum = 0;

    while (temp != 0) {
        lastdigit = temp % 10;
        sum += lastdigit * lastdigit * lastdigit;
        temp /= 10;
    }

    if (num == sum) {
        return 1;
    } else {
        return 0;
    }

    return 0;
}

void printarmstrong(int start, int end) {
    while (start <= end) {
        if (isarmstrong(start)) {
            printf("%d, ", start);
        }
        start++;
    }
}
```

- ### expt 2 is prime?

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

- ### expt 3 factorial

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

## prac 6

## if you get this one you are pretty fucked

- ### expt 1 deleting elemts from array

```c
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int a[1000], pos, c, n;
    char ch = 'y';
    printf("Enter number of elements in the array\n");
    scanf("%d", &n);
    printf("Enter %d elements\n", n);
    for (c = 0; c < n; c++) {
        scanf("%d", &a[c]);
    }
    do {
        if (ch == 'y') {
            printf("Enter the location you wish to delete element\n");
        }
        scanf("%d", &pos);
        if (pos > n + 1) {
            printf("deletion not possible\n");
        } else {
            for (c = pos - 1; c < n - 1; c++) {
                a[c] = a[c + 1];
            }
            n = n - 1;
            if (n > 0) {
                printf("resultant array: \n");
                for (c = 0; c < n; c++) {
                    printf("%d\n", a[c]);
                }
            } else {
                printf("Array is empty\n");
                exit(0);
            }
        }
        printf("Continue??\n");
        char flushall();
        scanf("%c", &ch);
    } while (ch == 'y' && n != 0);
    return 0;
}
```
