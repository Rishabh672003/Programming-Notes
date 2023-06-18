# JavaScript Variables
Variables are Containers for Storing Data. 

JavaScript Variables can be declared in 4 ways:

- Automatically
- Using ```var```
- Using ```let```
- Using ```const```
---
# Autmatically
```js
x = 5;
y = 6;
z = x + y;
// x, y, and z are undeclared variables. They are automatically declared when first used.
```
# var
```js
var x = 5;
var y = 6;
var z = x + y;
```
# let 
```js
let price1 = 5;
let price2 = 6;
let total = price1 + price2;
```
# const
```js
const x = 5;
const y = 6;
let z = x + y;
// These are constant values and cannot be changed. Hwoever 'c' cnanged be changed as it is 'let'.
```
---
# When to Use var, let, or const?
1. Always declare variables
2. Always use const if the value should not be changed
3. Always use const if the type should not be changed (Arrays and Objects)
4. Only use let if you can't use const
5. Only use var if you MUST support old browsers.
---
# JavaScript Identifiers
All JavaScript variables must be identified with unique names.

These unique names are called identifiers.

Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume).

The general rules for constructing names for variables (unique identifiers) are:
- Names can contain letters, digits, underscores, and dollar signs.
- Names must begin with a letter.
- Names can also begin with $ and _ .
- Names are case sensitive (y and Y are different variables).
- Reserved words (like JavaScript keywords) cannot be used as names.
---
# One Statement, Many Variables
You can declare many variables in one statement.

Start the statement with let and separate the variables by comma:
```js
let person = "John Doe", carName = "Volvo", price = 200;
```
A declaration can span multiple lines:
```js
let person = "John Doe",
carName = "Volvo",
price = 200;
```
