# Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that
allows you to create new classes based on existing ones. With inheritance, you
can define a new class (called the "subclass" or "derived class") that inherits
properties and behaviors from an existing class (called the "superclass" or
"base class").

For example, let's say we have a class called Animal. The Animal class has the
properties name, age, and species. The Animal class also has the methods eat(),
sleep(), and move().

We can create a derived class called Dog that inherits the properties and
methods of the Animal class. The Dog class can also have its own properties and
methods. For example, the Dog class might have the property breed.

When we create a new Dog object, the object will have all of the properties and
methods of the Animal class, plus the properties and methods of the Dog class.

Inheritance is a powerful tool that can be used to improve the readability,
maintainability, and reusability of code.

## Example code in C++

```cpp
#include <iostream>

using namespace std;

class Animal {
public:
  string name;
  int age;
  string species;

  void bark() {
    cout << "Woof!" << endl;
  }
};

class Dog : public Animal {
public:
  string breed;

  Dog(string name, int age, string species, string breed) {
    this->name = name;
    this->age = age;
    this->species = species;
    this->breed = breed;
  }
};

int main() {
  Dog dog("Spot", 5, "Canine", "Golden Retriever");
  cout << dog.name << endl; // Spot
  cout << dog.age << endl; // 5
  cout << dog.species << endl; // Canine
  cout << dog.breed << endl; // Golden Retriever
  dog.bark(); // Woof!
}

```

## Example code in Java

```java
class Animal {
  String name;
  int age;
  String species;

  void bark() {
    System.out.println("Woof!");
  }
}

class Dog extends Animal {
  String breed;

  public Dog(String name, int age, String species, String breed) {
    super(name, age, species);
    this.breed = breed;
  }
}

public class Main {
  public static void main(String[] args) {
    Dog dog = new Dog("Spot", 5, "Canine", "Golden Retriever");
    System.out.println(dog.name); // Spot
    System.out.println(dog.age); // 5
    System.out.println(dog.species); // Canine
    System.out.println(dog.breed); // Golden Retriever
    dog.bark(); // Woof!
  }
}
```

## Example code in python

```py

class Animal:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species

  def bark(self):
    print("Woof!")

class Dog(Animal):
  def __init__(self, name, age, species, breed):
    super().__init__(name, age, species)
    self.breed = breed

if __name__ == "__main__":
  dog = Dog("Spot", 5, "Canine", "Golden Retriever")
  print(dog.name) # Spot
  print(dog.age) # 5
  print(dog.species) # Canine
  print(dog.breed) # Golden Retriever
  dog.bark() # Woof!
```

