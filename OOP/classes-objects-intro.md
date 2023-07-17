# Classes and objects

In C++, a class is a user-defined data type that encapsulates data and methods (functions) that operate on that data. Classes are used to define objects, which are instances of the class. 
Note: This is not a case in purely OOP languages like Python or Java where Class and objects are the core of the language itself and not specifically a separate data type.

For example, if we are creating a banking program, we can give our class the following characteristics:
name: BankAccount
attributes: accountNumber, balance, dateOpened
behavior: open(), close(), deposit()

The class specifies that each object should have the defined attributes and behavior. However, it doesn't specify what the actual data is; it only provides a definition.

Once we've written the class, we can move on to create objects that are based on that class.
Each object is called an instance of a class. The process of creating objects is called instantiation.

### An example of classes, methods and objects in C++

```cpp
#include <iostream>

using namespace std;

class BankAccount {
private:
  string account_number;
  double balance;
  string date_opened;

public:
  BankAccount(string account_number, double balance, string date_opened) {
    this->account_number = account_number;
    this->balance = balance;
    this->date_opened = date_opened;
  }

  void open() { cout << "Bank account opened" << endl; }

  void close() { cout << "Bank account closed" << endl; }

  void deposit(double amount) {
    balance += amount;
    cout << "Deposited " << amount << " to bank account" << endl;
  }

  void withdraw(double amount) {
    if (amount > balance) {
      cout << "Insufficient funds" << endl;
    } else {
      balance -= amount;
      cout << "Withdrew " << amount << " from bank account" << endl;
    }
  }
};

int main() {
  BankAccount account("1234567890", 1000, "2023-01-01");

  account.open();
  account.deposit(500);

  // this will give an error as balance is private
  cout << account.balance << endl;
  account.close();
  return 0;
}
```

## Differences of C++ from Java/Python

In C++ Its similar to how things work in purely OOP languages like Python/Java only difference is in them everything is an object like whenever they get a variable assignment the instantiate the variable as an object of a class corresponding to type of data they are assigned.

Other difference are as follows -
![image](https://github.com/Rishabh672003/Programming-Notes/assets/53911515/496fa56d-fb29-442e-ae96-7fbab4a8f62a)

### Code example in python

```py
class Person:
    """
    The self keyword in Python is a reference to the current instance of the class.
    It is used to access the attributes and methods of the class from within an instance method.
    self is just a convention and not a reserved word
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))


person = Person("Bard", 100)
person.say_hello()

```

### Code example in java

```java
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void sayHello() {
        System.out.println("Hello, my name is " + this.name + " and I am " + this.age + " years old.");
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("Bard", 100);
        person.sayHello();
    }
}
```
