## TypeScript Basics

**Table of content :**

1. What is TypeScript ?
2. Why TypeScript ?
3. How TypeScript works under the hood ?
4. Primitive Data types.
5. Type Shapes.
6. The type "`any`".
7. TypeScript Explicit Type Annotations.

---

### 1. What is TypeScript ?

TypeScript is a programming language that adds types to JavaScript.

It is a superset of JavaScript which allows us to write JavaScript with a set of tools called a type system that can spot potential bugs, clarify the structure, and help refactor our code.

---

### 2. Why TypeScript ?

JavaScript allows us to assign any value to any variable. That makes it very flexible to use, which can be good for getting started quickly with it.

But in practice, variables that are assigned values of multiple types throughout a program can be very confusing or lead to bugs.

While stricter programming languages will inform the developer when they change one area of code in a way that will break other areas, JavaScript will not, which often leads to unexpected behavior at runtime.

Hence we need TypeScript for a type safety, better code readability and increased developer productivity.

---

### 3. How TypeScript works under the hood ?

The TypeScript Compiler (**Transpiler**) `tsc` converts our TypeScript code `.ts` into JavaScript code `.js` that can be understood and executed by browsers and other JavaScript environments.

This allows you to take advantage of type safety while ensuring our code is compatible with our JavaScript environments.

---

### 4. Primitive Data types

TypeScript recognizes JavaScript’s built-in “primitive” data types:

- boolean
- number
- null
- string
- undefined

If we try to reassign a variable to a value of a different type, TypeScript will surface an error.

```ts
let order = "first";
order = 1; // error
```

Running the TypeScript code above will result in the error: `Type 'number' is not assignable to type 'string'`.

This is because TypeScript expects the data type of the variable to match the type of the value initially assigned to it at declaration.

---

### 5. Type Shapes

TypeScript knows of what type our objects are & it also knows what shapes our objects adhere to.

An object’s shape describes what properties and methods it does or doesn’t contain.

The built-in types in JavaScript have properties and methods that always exist. For example, All strings are known to have a `.length` property and `.toLowerCase()` method.

```ts
"HEY".length; // 3
"HELLO".toLowerCase(); // "hello"
```

TypeScript will let you know if your code tries to access properties and methods that don’t exist:

```ts
"HEY".toLowercase();
// Property 'toLowercase' does not exist on type '"HEY"'.
// Did you mean 'toLowerCase'?
```

---

### 6. The type "`any`"

In situations where TypeScript isn’t be able to infer a type, it will implicitly consider a variable to be of type `any`.

This generally happens when a variable is declared without being assigned an initial value.

```ts
let guess; // warning Variable 'guess' implicitly has an 'any' type.
guess = "green";
guess = 69;
```

---

### 7. TypeScript Explicit Type Annotations.

We can tell TypeScript that what type something is or will be, by using a type annotation (type declaration).

Adding a type annotation ensures that a variable can be assigned to that type only.

This can be achieved by appending a variable with a colon (`:`) and the type (e.g., `number`, `string`, or `any`).

```ts
let mustBeANumber: number; // type annotation
mustBeANumber = 69;

mustBeANumber = "sixty nine"; // Error: Type 'string' is not assignable to type 'number'
```

This can be useful when declaring a variable without an initial value.

Type annotations get removed when compiled to JavaScript.
