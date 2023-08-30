## Functions

```py
def function_name(parameters): # define the function
    # code goes here
function_name(arguments) # call function
```

## Define a function to add two numbers

```py
def add(a, b):
    return a + b
print(add(2, 3))
```

## Define a function to greet user

```py
def greetUser(name, time):
    time = time.upper()
    if (time == "MORNING" or time == "DIN"):
        return f"Good Morning, {name}"
    elif (time == "AFTERNOON" or time == "DOPHAR"):
        return f"Good Afternoon, {name}"
    elif (time == "NIGHT" or time == "SHAAM"):
        return f"Good Evening, {name}"
    else:
        return f"Good Night, {name}"


x = input("What's your name: ")
y = input("What's your day time: ")

print(greetUser(x, y))
```

## Define a function to calculate GCD of two numbers

```py
def gcd(n1, n2):
    if (n2 == 0):
        return abs(n1)
    else:
        return gcd(n2, n1 % n2)

n, m = map(int, input("Enter two numbers: ").split())
print(f"GCD of {n} and {m} is {gcd(n, m)}")
```

## Define a function to print first nth terms in fibonacci terms.

```py
def fibo(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

d = int(input("Enter the value of 'n': "))

if d > 0:
    for i in range(1, d + 1):
        print(fibo(i), end=" ")
else:
    print("Invalid Input, n should be a positive integer!")
```

## Define a function to print factorial of a number.

```py
def fact(n):
    if n <= 0:
        return "Invalid input"
    elif n < 2:
        return 1
    else:
        return n * fact(n - 1)

e = int(input("Enter the value of 'n': "))
print(f"Factorial of {e} is {fact(e)}")
```

## Define a function to convert decimal to binary

```py
def toBinary(n):
    ans = ""
    while(n != 0):
        rem = n % 2
        ans = ans + str(rem)
        n //= 2
    return ans[::-1] # reverse the returned string

num = int(input("Enter any decimal value: "))
print(f"Binary representation of {num} is {toBinary(num)}")
```
