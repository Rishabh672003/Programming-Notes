# Variables and DataTypes.

1. [Variables](#Variables)
2. [DataTypes](#DataTypes)

# Variables

Creating (Declaring) PHP Variables.
In PHP, a variable starts with the `$` sign, followed by the name of the variable.

```php
<?php
$txt = "Hello world!";
$x = 5;
$y = 10.5;
?>
```

After the execution of the statements above, the variable `$txt` will hold the value `Hello world!`,
the variable `$x` will hold the value `5`, and the variable `$y` will hold the value `10.5`.
Note: When you assign a text value to a variable, put quotes around the value.

Note: Unlike other programming languages, PHP has no command for declaring a variable. It is created the moment you first assign a value to it.

# Output Variables

The PHP `echo` statement is often used to output data to the screen.

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
3. [super global](#Super_Global_Variables)

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

# Super_Global_Variables

_Some predefined variables in PHP are "superglobals", which means that they are always accessible,
regardless of scope - and you can access them from any function, class or file without having to do anything special._

The PHP superglobal variables are:

1. [$GLOBALS](#globals)
2. [$\_SERVER](#_server)
3. [$\_REQUEST](#_request)
4. [$\_POST](#_post)
5. [$\_GET](#_get)

# $GLOBALS

_$GLOBALS is a PHP super global variable which is used to access global variables from anywhere in the PHP script (also from within functions or methods).
PHP stores all global variables in an array called $GLOBALS[index]. The index holds the name of the variable.
The example below shows how to use the super global variable $GLOBALS:_

```php
<?php
$x = 75;
$y = 25;

function addition() {
  $GLOBALS['z'] = $GLOBALS['x'] + $GLOBALS['y'];
}

addition();
echo $z;
?>
```

# $\_SERVER

_$\_SERVER is a PHP super global variable which holds information about headers, paths, and script locations.
The example below shows how to use some of the elements in $\_SERVER:_

```php
<?php
echo $_SERVER['PHP_SELF'];       // Returns the filename of the currently executing script
echo "<br>";

echo $_SERVER['SERVER_NAME'];    // Returns the name of the host server (such as www.w3schools.com)
echo "<br>";

echo $_SERVER['SERVER_ADDR'];    // Returns the IP address of the host server
echo "<br>";

echo $_SERVER['HTTP_HOST'];      // Returns the Host header from the current request
echo "<br>";

echo $_SERVER['HTTP_REFERER'];   // Returns the complete URL of the current page (ot all user-agents support it)
echo "<br>";

echo $_SERVER['REQUEST_METHOD']; // Returns the request method used to access the page (such as POST)
echo "<br>";

echo $_SERVER['SCRIPT_NAME'];    // Returns the path of the current script
echo "<br>";

echo $_SERVER['SCRIPT_URI'];     // Returns the URI of the current page
?>
```

# $\_REQUEST

PHP $\_REQUEST is a PHP super global variable which is used to collect data after submitting an HTML form.
The example below shows a form with an input field and a submit button. When a user submits the data by clicking on "Submit", the form data is sent to the file specified in the action attribute of the <form> tag.
In this example, we point to this file itself for processing form data. If you wish to use another PHP file to process form data, replace that with the filename of your choice. Then, we can use the super global variable $\_REQUEST to collect the value of the input field:

```php
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // collect value of input field
  $name = $_REQUEST['fname'];
  if (empty($name)) {
    echo "Name is empty";
  } else {
    echo $name;
  }
}
?>

</body>
```

# $\_POST

POST is a PHP super global variable which is used to collect form data after submitting an HTML form with method="post".
$_POST is also widely used to pass variables.
The example below shows a form with an input field and a submit button. When a user submits the data by clicking on "Submit", the form data is sent to the file specified in the action attribute of the <form> tag. In this example, we point to the file itself for processing form data._

```php
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // collect value of input field
  $name = $_POST['fname'];
  if (empty($name)) {
    echo "Name is empty";
  } else {
    echo $name;
  }
}
?>

</body>
```

# $\_GET

PHP $_GET is a PHP super global variable which is used to collect form data after submitting an HTML form with method="get".
$\_GET can also collect data sent in the URL.
Assume we have an HTML page that contains a hyperlink with parameters:

```cpp
<a href="test_get.php?subject=PHP&web=W3schools.com">Test $GET</a>
```

When a user clicks on the link "Test $GET", the parameters "subject" and "web" are sent to "test_get.php", and you can then access their values in "test_get.php" with $\_GET.
The example below shows the code in "test_get.php":

```cpp
<?php
echo "Study " . $_GET['subject'] . " at " . $_GET['web'];
?>
```

---

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];

    // Database Connection
    $conn = new mysqli('localhost', 'root', '', 'portfolio');
    if ($conn->connect_error) {
        die('Connection Failed: ' . $conn->connect_error);
    } else {
        $stmt = $conn->prepare("INSERT INTO portfolio (name, email, subject, message) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $name, $email, $subject, $message);
        $stmt->execute();
        echo "Message Sent Successfully!";
        $stmt->close();
        $conn->close();
    }
}
?>
```
