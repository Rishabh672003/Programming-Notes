#include <stdio.h>
void armstrong(int n);

int main() {
  char c;
  int n;
  printf("Enter a positive integer: ");
  scanf("%d", &n);
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
  if (sum == temp){
    printf("\n%d is an Armstrong number.", n);
  }
  else
    printf("\n%d is not an Armstrong number.",n);
}
