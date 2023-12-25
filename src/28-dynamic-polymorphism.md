# Dynamic Polymorphism

Dynamic polymorphism is a programming concept in object-oriented languages like C++ where a derived class can override or redefine methods of its base class. This means that a single method call can have different implementations based on the type of object it is called on.

Dynamic polymorphism is achieved through **virtual functions**, which are member functions of a base class marked with the `virtual` keyword. When you specify a virtual function in a base class, it can be overridden in any derived class to provide a different implementation.

## Example

Here's an example in C++ demonstrating dynamic polymorphism.

```cpp
#include <iostream>

// Base class
class Shape {
  public:
    virtual void draw() { std::cout << "Drawing a shape" << std::endl; }
};

// Derived class 1
class Circle : public Shape {
  public:
    void draw() override { std::cout << "Drawing a circle" << std::endl; }
};

// Derived class 2
class Rectangle : public Shape {
  public:
    void draw() override { std::cout << "Drawing a rectangle" << std::endl; }
};

int main() {
    Shape* shape;
    Circle circle;
    Rectangle rectangle;

    // Storing the address of circle
    shape = &circle;

    // Call circle draw function
    shape->draw();

    // Storing the address of rectangle
    shape = &rectangle;

    // Call rectangle draw function
    shape->draw();

    return 0;
}
```

This code defines a base class `Shape` with a virtual function `draw`. Two derived classes `Circle` and `Rectangle` both override the `draw` function to provide their own implementations. Then in the `main` function, a pointer of type `Shape` is used to call the respective `draw` functions of `Circle` and `Rectangle` objects. The output of this program will be:

```
Drawing a circle
Drawing a rectangle
```

As you can see, using dynamic polymorphism, we can determine at runtime which `draw` method should be called based on the type of object being used.

## **Never use `malloc` in C++**

In this code calling of `f()` with the _a2_ object will cause a segmentation fault as _a2_ is instantiated using `malloc`
So don't use `malloc` use `new` keyword instead in C++

```cpp
class A {
  public:
    int x = 3;
    virtual void f() { cout << "abc"; }
};

A* a1 = new A;
A* a2 = (A*)malloc(sizeof(A));

std::cout << a1->x; // print "3"
cout << a2->x;      // undefined value!!
a1->f();            // print "abc"
a2->f();            // segmentation fault
```
