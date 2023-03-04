## yehi ayega

```c
#include <stdio.h>
struct Person {
  int id;
  char name[20];
  char address[30];
  struct DOB {
    int day;
    int month;
    int year;
  } d1;
} p1;

int main() {
  printf("Enter ID :\n");
  scanf("%d", &p1.id);
  printf("Enter Name :\n");
  scanf("%s", &p1.name);
  printf("Enter Address :\n");
  scanf("%s", &p1.address);
  printf("Enter Date of Birth in dd/mm/yyyy form :\n");
  scanf("%d%d%d", &p1.d1.day, &p1.d1.month, &p1.d1.year);
  printf("\n PERSON INFORMATION :");
  printf("\nID = %d", p1.id);
  printf("\nNAME = %s", p1.name);
  printf("\nADDRESS = %s", p1.address);
  printf("\nDATE OF BIRTH = %d:%d:%d", p1.d1.day, p1.d1.month, p1.d1.year);
}
```
