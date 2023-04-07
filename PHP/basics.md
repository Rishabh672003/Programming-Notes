# Variables and DataTypes.
1. [Variables](#Variables)
2. [DataTypes](#DataTypes)

# Variables
Creating (Declaring) PHP Variables.
In PHP, a variable starts with the ```$``` sign, followed by the name of the variable.
```php
<?php
$txt = "Hello world!";
$x = 5;
$y = 10.5;
?>
```
After the execution of the statements above, the variable ```$txt``` will hold the value ```Hello world!```,
the variable ```$x``` will hold the value ```5```, and the variable ```$y``` will hold the value ```10.5```.
Note: When you assign a text value to a variable, put quotes around the value.

Note: Unlike other programming languages, PHP has no command for declaring a variable. It is created the moment you first assign a value to it.

# Output Variables
The PHP ```echo``` statement is often used to output data to the screen.

The following example will show how to output text and a variable:
```php
<?php
$txt = "W3Schools.com";
echo "I love $txt!";
//  or
echo "I love " . $txt . "!";
?>
```
_We did not have to tell PHP which data type the variable is.PHP automatically associates a data type to the variable, depending on its value. Since the data types are not set in a strict sense, you can do things like adding a string to an integer without causing an error._
_In PHP 7, type declarations were added. This gives an option to specify the data type expected when declaring a function, and by enabling the strict requirement, it will throw a "Fatal Error" on a type mismatch._

# PHP Variables Scope
In PHP, variables can be declared anywhere in the script.
The scope of a variable is the part of the script where the variable can be referenced/used.

PHP has three different variable scopes:
1. [global](#Global_Variables)
2. [local](#Local_Variables)
3. [static](#StaticVariales)

# Global_Variables
_A variable declared outside a function has a GLOBAL SCOPE and can only be accessed outside a function:_
```php
<?php
$x = 5; // global scope

function myTest() {
  // using x inside this function will generate an error
  echo "<p>Variable x inside function is: $x</p>";
}
myTest();

echo "<p>Variable x outside function is: $x</p>";
?>
```
# Local_Variables
_A variable declared inside a function has a LOCAL SCOPE and can only be accessed inside a function:_
```php
<?php
function myTest() {
  $x = 5; // local scope
  echo "<p>Variable x inside function is: $x</p>";
}
myTest();

// using x outside the function will generate an error
echo "<p>Variable x outside function is: $x</p>";
?>
```
# DataTypes
