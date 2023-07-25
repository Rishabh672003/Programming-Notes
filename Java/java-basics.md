# Java Basics

## 1. Java Template code

```java
pubic class Main {
    public static void main(string [] args){
        // code goes here
    }
}
```

**Now, let's go through the code step by step:**

1. **public class Main :**

- **public:** This is an access modifier that specifies the visibility of the class. In this case, it means the class Main is accessible from any other class.
- **class:** This keyword is used to define a class in Java.
- **Main:** This is the name of the class. _The name of the Java file should match the class name._

2. **public static void main(String[] args)**

- **public:** This is another access modifier that specifies the visibility of the method main(). It means the main() method can be accessed from any other class.
- **static:** This keyword indicates that the main() method belongs to the class itself, not an instance of the class. It allows the program to run without creating an object of the class.
- **void:** This is the return type of the main() method, indicating that it doesn't return any value.
- **main:** This is the name of the method. _The main() method is the entry point of a Java program, and it's executed when the program starts._
- **String[] args:** This is the parameter list of the main() method. It allows you to pass command-line arguments to the program. The args variable is an array of strings that can hold the command-line arguments.

## 2. Output

```java
System.out.println("Hello World");
```

**Now, let's go through the code step by step:**

1. **System:** System is the predefined class that provides access to standard Input / Output. and Error streams.
2. **out:** out is a public static member of System class which represents standard output.
3. **println:** println is a member of print stream class, println prints a "new line" of text in output.

## 3. Input

```java
import java.util.Scanner; // Import the Scanner class to read user input

public class UserInputExample {
    public static void main(String[] args) {

        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Read the user's input (name) as a String
        String name = scanner.nextLine();

        // Close the Scanner to release resources
        scanner.close();

        // Display the user's input
        System.out.println("Hello, " + name);
    }
}
```

**NOTE: .nextLine() reads string or character values. To accept integer or float values, we can use .nextInt() or .nextFloat()**

<hr>

## 4. Variables and Data types

#### Variables:

**Declaring variables in Java is same as that of most other programming languages like C, C++, etc.**

```java
int x; // declaration
x = 123; // assignment
int y = 123 // initialization
```

#### Primitive Data Types:

```java
int x = 123; // integer values
double y = 3.1416; // decimal values
boolean z = true; // true or false
char symbol = '@'; // single characters
String name = "Amit"; // String or sentences
```

<img src="https://miro.medium.com/v2/resize:fit:1400/1*Oooxt8zMzTOvJq4HenjWDg.png">

## Let's Add two Numbers using Input - Output

```java
import java.util.Scanner;

public class UserInputExample {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Number 1: ");
        int num1 = sc.nextInt();

        System.out.println("Enter Number 2: ");
        int num2 = sc.nextInt();

        int sum = a + b;

        sc.close();

        System.out.println("Sum of the numbers: " + sum);
    }
}
```

- **Similarly you can use other Operators (-, \*, /, %) and try it by your own!**
- **Try making a Simple Calculator using If-Else ladder or Switch-Case.**