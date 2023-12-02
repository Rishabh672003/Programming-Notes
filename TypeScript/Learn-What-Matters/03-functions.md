## Functions in TypeScript

**Table of content :**

1. Unexpected JavaScript Behaviour.
2. Parameter Type Annotations.
3. Optional Parameters.
4. Default Parameters.
5. Explicit Return types.
6. Documenting Functions. (optional)

---

In JavaScript, functions don't really know what type of arguments are being passed in them!

This can lead to unexpected behavior when functions are called with arguments of different types than expected.

Here's what I mean :

```js
const sum = (a, b) => a + b;
console.log(sum(10, 20)); // prints 30
console.log("This is ", "crazy!"); // prints This is crazy!
```

The parameters `a` and `b` are expected to be a number and the `sum` function is supposed to add two **numbers**.

However, the function is also called with two string arguments, and it simply concatenates them instead of adding them (which is actually not possible).

---

### Here's when **Parameter Type Annotations** comes into picture.

In TypeScript, function parameters may be given type annotations with the same syntax as variable declarations `:` a colon next to the name.

The type annotations ensure that the parameters are of the correct type

```js
const sum = (a: number, b: number) => a + b;

console.log(sum(10, 20)); // prints 30

console.log("Won't run ", "this time!");
// Error: argument "Won't run" and "this time!" is not assignable to parameter of type 'number'
```

Parameters that we do not provide type annotations for are assumed to be of type `any`, the same way variables are.

---

### Optional Parameters

TypeScript normally gives an error if we don’t provide a value for all arguments in a function. This isn’t always desirable; sometimes we’d like to skip providing values.

```ts
const greet = (name: string) => {
  console.log(`Hello, ${name || "Anonymous"}!`);
};

greet("Anders"); // Prints: Hello, Anders!
greet(); // Error: Expected 1 arguments, but got 0.
```

When the code snippet above is compiled to JavaScript, the `greet()` function will correctly print **'Hello, Anonymous!'**.

That’s because in JavaScript, when no arguments are passed in, `name` gets a false value of `undefined`, which means that

```
name || 'Anonymous' evaluates as
undefined || 'Anonymous' = 'Anonymous'.
```

Hence, indicate that a parameter is intentionally optional, we add a `?` after its name, before colon.

This tells TypeScript that the parameter is allowed to be `undefined` and doesn’t always have to be provided.

```ts
const greet = (name?: string) => {
  console.log(`Hello, ${name || "Anonymous"}!`);
};
greet(); // print : Hello Anonymous
```

---

### Default Parameters

Just like other programming languages, TypeScript too supports Default Paramters (parameters being assigned a default value at the time of function declaration).

```ts
const greet = (name = "Anonymous") => {
  console.log(`Hello, ${name}!`);
};
// prints Hello Anonymous
```

The function `greet()` can only receive a `string` or `undefined` as its name parameter.

Any other type provided as an argument will be considered as a type error.

---

### Explicit Return types

If we'd like to be explicit about what type a function returns, we can add an explicit type annotation **after its closing parenthesis**.

Here, we use the same syntax as other type annotations, a `:` followed by the type.

TypeScript will produce an error for any return statement in that function that doesn’t return the right type of value.

```ts
const greet = (name?: string): string => {
  if (name) {
    return `Hello, ${name}!`;
  }

  return 2 + 2;
  // Typescript Error: Type 'number' is not assignable to type 'string'.
};
```

In The line `(name?: string): string`, the annotation `:string` inside the parenthesis determines the type of parameter whereas, outside the parenthesis determines the return type for the function `greet()`

It is often preferred to use type annotations for functions, even when those functions don’t return anything.

If there's no returned value, we must treat the return type as `void`. A proper type annotation for this function would look like this:

```ts
const logGreeting = (name: string): void => {
  console.log(`Hello, ${name}!`);
};
```

---

### Documenting Functions (Special Comments)

Documentation comments are especially useful for documenting functions.

We place a function’s documentation comment in the code directly above the function declaration.

We can use `@param` to describe each of the function’s parameters, and we can use `@returns` to describe what the function returns

Syntax :

```ts
/**
 * This is a documentation comment
 */
```

Example :

```ts
/**
 * Returns the sum of two numbers.
 *
 * @param x - The first input number
 * @param y - The second input number
 * @returns The sum of `x` and `y`
 */
const getSum = (x: number, y: number): number => x + y;
```
