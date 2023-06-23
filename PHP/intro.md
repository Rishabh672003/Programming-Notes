# What is PHP ?

1. PHP is a server scripting language, and a powerful tool for making dynamic and interactive Web pages.
2. PHP files can contain text, HTML, CSS, JavaScript, and PHP code.
3. PHP code is executed on the server, and the result is returned to the browser as plain HTML.
4. PHP files have extension `.php`

# What Can PHP Do?

1. PHP can generate dynamic page content.
2. PHP can create, open, read, write, delete, and close files on the server.
3. PHP can collect form data.
4. PHP can send and receive cookies.
5. PHP can add, delete, modify data in your database.
6. PHP can be used to control user-access.
7. PHP can encrypt data

# Basic PHP Syntax

A PHP script can be placed anywhere in the document.
A PHP script starts with `<?php` and ends with `?>:`

```php
<?php
// PHP code goes here
?>
```

Example:

```php
<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello World!";
?>

</body>
</html>
```

PHP is not Case Sensitive for user defined keywords, for example:

```php
<?php
ECHO "Hello World!<br>";
echo "Hello World!<br>";
EcHo "Hello World!<br>";
?>
// ECHO, echo and EcHo works same.
```

NOTE: But Variable names are Case Sensitive.

```php
$color, $COLOR, and $coLOR // are treated as three different variables:
```
