# Classes and objects

In C++, a class is a user-defined data type that encapsulates data and methods (functions) that operate on that data. Classes are used to define objects, which are instances of the class.

For example, if we are creating a banking program, we can give our class the following characteristics:
name: BankAccount
attributes: accountNumber, balance, dateOpened
behavior: open(), close(), deposit()

The class specifies that each object should have the defined attributes and behavior. However, it doesn't specify what the actual data is; it only provides a definition.

Once we've written the class, we can move on to create objects that are based on that class.
Each object is called an instance of a class. The process of creating objects is called instantiation.

## An example of classes, methods and objects in C++

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
