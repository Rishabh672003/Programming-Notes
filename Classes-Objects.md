# Classes and objects

In C++, a class is a user-defined data type that encapsulates data and methods (functions) that operate on that data. Classes are used to define objects, which are instances of the class.

For example, if we are creating a banking program, we can give our class the following characteristics:
name: BankAccount
attributes: accountNumber, balance, dateOpened
behavior: open(), close(), deposit()

The class specifies that each object should have the defined attributes and behavior. However, it doesn't specify what the actual data is; it only provides a definition.

Once we've written the class, we can move on to create objects that are based on that class.
Each object is called an instance of a class. The process of creating objects is called instantiation. 

## Abstraction

Data abstraction is the concept of providing only essential information to the outside world. It's a process of representing essential features without including implementation details.

A good real-world example is a book: When you hear the term book, you don't know the exact specifics, i.e.: the page count, the color, the size, but you understand the idea of a book - the abstraction of the book. 

Abstraction means, that we can have an idea, or a concept that is completely separate from any specific instance.
It is one of the fundamental building blocks of object oriented programming.

![image](https://user-images.githubusercontent.com/53911515/223426844-2df8ab7a-d211-413c-a9ca-d6c77c4668e8.png)
