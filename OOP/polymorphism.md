# Polymorphism

Polymorphism is a fundamental concept in object-oriented programming (OOP) that
allows objects of different classes to be treated as objects of a common
superclass. It enables you to write code that can work with objects of different
types, providing flexibility and extensibility.

In simple words polymorphism allows you to over-ride methods made in the
superclass in the inherited classes made from the superclass.

## Implementations in C++, Java and Python

### In C++

```cpp
#include <iostream>

class Animal {
public:
    // virtual keyword is what allows the methods to be overridden in C++
    // other wise it wont be able to be polymorphised
    virtual void makeSound() {
        std::cout << "The animal makes a sound" << std::endl;
    }
};

class Dog : public Animal {
public:
    void makeSound() override {
        std::cout << "The dog barks" << std::endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        std::cout << "The cat meows" << std::endl;
    }
};

int main() {
    Animal* animal1 = new Dog();
    Animal* animal2 = new Cat();

    animal1->makeSound(); // Output: The dog barks
    animal2->makeSound(); // Output: The cat meows

    delete animal1;
    delete animal2;

    return 0;
}

```

### In java

```java
class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

class Dog extends Animal {
    public void makeSound() {
        System.out.println("The dog barks");
    }
}

class Cat extends Animal {
    public void makeSound() {
        System.out.println("The cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();

        animal1.makeSound(); // Output: The dog barks
        animal2.makeSound(); // Output: The cat meows
    }
}

```

### In python

```py
class Animal:
    def makeSound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def makeSound(self):
        print("The dog barks")

class Cat(Animal):
    def makeSound(self):
        print("The cat meows")

animal1 = Dog()
animal2 = Cat()

animal1.makeSound() # Output: The dog barks
animal2.makeSound() # Output: The cat meows

```
