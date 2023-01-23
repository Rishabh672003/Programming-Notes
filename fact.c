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
