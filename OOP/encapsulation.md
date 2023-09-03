# Encapsulation

Encapsulation is a fundamental concept in object-oriented programming (OOP). It
refers to the bundling of data and methods into a single unit, called a class.

The key idea behind encapsulation is to create a protective barrier around an
object's internal state, preventing direct access to its data from outside the
object. Instead, external entities interact with the object through well-defined
methods, which serve as the object's interface or API (Application Programming
Interface).

## Access modifiers

To achieve encapsulation in OOP, you typically use access modifiers to control
the visibility and accessibility of class members:

1. Public: Public members are accessible from anywhere, including external code.
   They form the object's public interface.

2. Private: Private members are only accessible within the class itself. They
   cannot be accessed or modified directly from external code. In python variables
   are made private by adding `__` in front of variables like `__variable` instead of using a private keyword.

3. Protected: Protected members are accessible within the class itself and its
   subclasses (derived classes). They provide a limited level of accessibility for inheritance scenarios.

4. Default (Package-private)(Only in java): Members without an explicit access modifier are
   accessible within the same package.

### Implementation of encapsulation in C++, Java and Python

#### C++

```cpp
#include <iostream>
#include <string>

class BankAccount {
private:
    std::string accountNumber;
    double balance;

public:
    BankAccount(std::string accNum, double initialBalance)
        : accountNumber(accNum), balance(initialBalance) {}

    std::string getAccountNumber() { return accountNumber; }
    double getBalance() { return balance; }
};

int main() {
    BankAccount account("1234567890", 1000.0);
    std::cout << account.getAccountNumber() << std::endl;  // Output: 1234567890
    std::cout << account.getBalance() << std::endl;  // Output: 1000.0

    return 0;
}
```

#### Java

```java
public class BankAccount {
    private String accountNumber;
    private double balance;

    public BankAccount(String accNum, double initialBalance) {
        accountNumber = accNum;
        balance = initialBalance;
    }

    public String getAccountNumber() { return accountNumber; }
    public double getBalance() { return balance; }

    public static void main(String[] args) {
        BankAccount account = new BankAccount("1234567890", 1000.0);
        System.out.println(account.getAccountNumber());  // Output: 1234567890
        System.out.println(account.getBalance());  // Output: 1000.0
    }
}
```

#### Python

```py
class BankAccount:
    def __init__(self, accNum, initialBalance):
        # __ is used to make variables private
        self.__accountNumber = accNum
        self.__balance = initialBalance

    def getAccountNumber(self):
        return self.__accountNumber

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

account = BankAccount("1234567890", 1000.0)
print(account.getAccountNumber())  # Output: 1234567890
print(account.getBalance())  # Output: 1000.0

account.deposit(500.0)
print(account.getBalance())  # Output: 1500.0

account.withdraw(200.0)
print(account.getBalance())  # Output: 1300.0

```
