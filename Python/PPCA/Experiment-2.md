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
