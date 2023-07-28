## Decision making statements

### Write a program to check whether a number is even or odd

```py
a = int(input("Enter the number: "))
if a%2==0:
    print("The number is even")
else:
    print("The number is odd")
```

### Write a program to find largest number out of three numbers entered by a user.

```py
a, b, c = map(int, input("Enter three numbers: ").split())

if a > b:
    if a > c:
        print(f"the larget number is {a}")
    else:
        print(f"the larget number is {c}")
else:
    if b > c:
        print(f"the larget number is {b}")
    else:
        print(f"the larget number is {c}")
```

### Write a program to check whether the last digit of a number is divisible by 4 or not

```py
a = int(input("Enter the number: "))
last_digit = a % 10

if last_digit % 4 == 0:
    print("Last digit is divisible by 4")
else:
    print("Last digit is not divisible by 4")
```

### Write a program to check whether a year entered by the user is leap or not.

```py
year = int(input("Enter the Year: "))
if year % 4 == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
```

### A college grading system

```py
marks = int(input("Enter the marks: "))

if marks < 40:
    print("You have failed")
elif marks >= 40 and marks < 45:
    print("The grade is P")
elif marks >= 45 and marks < 50:
    print("The grade is E")
elif marks >= 50 and marks < 60:
    print("The grade is D")
elif marks >= 60 and marks < 70:
    print("The grade is C")
elif marks >= 70 and marks < 75:
    print("The grade is B")
elif marks >= 75 and marks < 80:
    print("The grade is A")
else:
    print("The grade is O")
```
