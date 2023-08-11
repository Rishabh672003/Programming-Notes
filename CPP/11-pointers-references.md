# Pointers

A pointer is a variable that stores the memory address of another variable (or function). It points to the location of the variable in memory, and it allows you to access or modify the value indirectly. Here's a general format to declare a pointer:

```cpp
dataType *pointerName;
```

**Initializing a pointer:**

```cpp
int num = 10;
int *ptr = &num;  // Pointer 'ptr' now points to the memory address of 'num'
```

**Accessing value using a pointer:**

```cpp
int value = *ptr; // Value now contains the value of the variable that 'ptr' points to (i.e., 10)
```

## References

A reference is an alias for an existing variable, meaning it's a different name for the same memory location. Unlike pointers, references cannot be null, and they must be initialized when they are declared. Once a reference is initialized, it cannot be changed to refer to another variable.

Here's a general format to declare a reference:

```cpp
dataType &referenceName = existingVariable;
```

**Example:**

```cpp
int num = 10;
int &ref = num; // Reference 'ref' is now an alias of 'num'
```

Modifying the value of `ref` will also modify the value of `num` because they share the same memory location.

**Note:** References are generally used when you want to pass a variable by reference in function arguments or when you want to create an alias for a variable without the need for pointer syntax.

### Pointers and how to use and operate on them

```cpp
int a = 0;
int* address = &a;

cout << address << endl; // will out put memory address of a
cout << *address << endl; // will output 0 as the pointer is derefrenced
cout << &address << endl; // will output the memory address of pointer
cout << *address + 1 << endl; // will output 1
cout << address + 2
     << endl; // will output memory_adress + n*(memory byte of int)
cout << address + 'a'
     << endl; // will output memory_adress + n*(memory byte of char)

// pointers and how they interact with arrays
int prime[5] = {2, 3, 5, 7, 11};

// all will return the memory address of first element of the array
cout << "Result using &prime = " << &prime << endl;
cout <<"Result using prime = " <<  prime << endl;
cout <<"Result using &prime[0] = " <<  &prime[0] << endl;

// will return the second elements memory address
cout << "after adding one: " << &prime[0] + 1 << endl;

// will return the second element as the pointer is dereferenced
// this can be used to loop around the array
cout << "after adding one: " << *(&prime[0] + 1) << endl;

for(int i = 0; i < 5; i++){
    cout << *(prime + i)  << " ";
}
```

### References and some of there uses

```cpp
int &b = a; // reference of a is b

// references are aliases to original variable and can be called by
// functions using call by reference which changes the og variable
auto point = [&a]() { return a += 2; };
point();
cout << a << endl; // will output 2 now
```

- [Pointers in C explained](https://www.freecodecamp.org/news/pointers-in-c-are-not-as-difficult-as-you-think/)
