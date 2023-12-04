## Custom TypeScript Types

**Table of content :**

1. Enum Types.
2. Object Types.
3. Type Aliases.
4. Function Types.
5. Generic Types.
6. Generic Functions.

---

### Enums Types

An enum, short for **enum**erated type, is a special data type that consists of a set of named constants which are used to represent **a set of possible options or choices**.

Example :

```js
enum Direction {
  North,
  South,
  East,
  West
}
```

The code above defines the enum `Direction`, representing four compass directions : `Direction.North`, `Direction.South`, `Direction.East`, and `Direction.West`. Any other values, like `Direction.Southeast`, are not allowed.

Now this enum type can be used in a type annotation like any other type.

Here's what I mean :

```ts
let whichWayToGo: Direction; // creating a variable with Type Direction

whichWayToGo = Direction.North; // No error.

whichWayToGo = Direction.Southeast; // Type error: Southeast is not a valid value for the Direction enum.

whichWayToGo = West; // Wrong syntax, we must use Direction.West instead.
```

---

Another Example :

```ts
// craeting an enum of pets
enum Pet {
  Hamster,
  Rat,
  Cat,
  Dog,
}

// assigning an enum value to a variable of type enum.
const petOnSale: Pet = Pet.Cat;

// creating a 2D array, where the type of first element is Pet and other is a number.
const ordersArray: [Pet, number][] = [
  [Pet.Rat, 2],
  [Pet.Cat, 1],
  [Pet.Hamster, 2],
  [Pet.Dog, 50],
];

// ordering a pet that does not exist.
ordersArray.push([Pet.Jerboa, 3]);
// Type error : Property 'Jerboa' does not exist on type 'typeof Pet'.
```

---

### Object Types

TypeScript’s object types are extremely useful, as they allow us extremely fine-level control over variable types in our programs.

They’re also the most common custom types, so we’ll have to understand them if we want to read other people’s programs.

Here's a Type annotation for an object :

```ts
let person: {
  name: string;
  age: number;
};
```

Trying to assign a value to person that doesn’t have `name` and `age` properties of the specified types will lead to a type error.

```ts
let person: { name: string; age: number };

person = { name: "Amit", age: "Twenty" };
// Type error: age property has the wrong type.
```

TypeScript has no restrictions on the types of an object’s properties. They can be enums, arrays, and even other object types!

Example :

```ts
let company: {
  companyName: string;
  boss: { name: string; age: number };
  employees: { name: string; age: number }[];
  bestEmployee: { name: string; age: number };
  moneyEarned: number;
};
```

In the above code, `company` is the base object. `companyName` is of type `string`, `boss` and `bestEmployee` are objects and `employees` is an array.

One more detailed example which will help us understand the use of Object Types more clearly :

```ts
// a funcion which take an object as a parameter
let happyBirthday = (person: {
  name: string;
  age: number;
  giftWish: string;
}) => {
  let output = "";
  output += "Happy Birthday " + person.name + "! ";
  output += "You are now " + person.age + " years old! ";
  output += "Your birthday wish was " + person.giftWish;
  console.log(output);
};

// an array of objects
let birthdayBabies: {
  name: string;
  age: number;
  giftWish: string;
}[] = [
  { name: "Liam", age: 10, giftWish: "karate skills" },
  { name: "Olivia", age: 12, giftWish: "a bright future" },
  { name: "Ava", age: 9, giftWish: "$0.25" },
];

birthdayBabies.forEach(happyBirthday);
```

---

### Type Aliases

Recall our earlier company example :

```ts
let company: {
  companyName: string;
  boss: { name: string; age: number };
  employees: { name: string; age: number }[];
  employeeOfTheMonth: { name: string; age: number };
  moneyEarned: number;
};
```

There’s so much needless repetition here! (And the more times we repeat something, the more opportunity there is for typos.) This can be cleaned up with type aliases!!

**Type Aliases are alternative custom type names that we choose for convenience**. We use the syntax `type <alias name> = <type>`

Example :

```ts
type MyString = string; // creating an alias
let myVar: MyString = "Hi"; // myVar is of type MyString
```

Hence we can avoid repetetions using custom aliases! Here's a better `company` object literal :

```ts
// alias for a Person object
type Person = { name: string; age: number };

// a cleaner & readable version
let company: {
  companyName: string;
  boss: Person;
  employees: Person[];
  employeeOfTheMonth: Person;
  moneyEarned: number;
};
```

Another example :

```ts
// an alias of type tuple
type Coord = [number, number, string, number, number, string];

let bermudaTraingle: Coord = [40, 43.2, "N", 73, 59.8, "W"];
let pyramidGiza: Coord = [25, 0, "N", 71, 0, "W"];
```

---

Difference between :

```ts
let person1: {name: string; age: number};
let person2 = {name: string; age: number};
```

The difference between `let person1: {name: string; age: number};` and `let person2 = {name: string; age: number};` is that the former declares a **type alias** for an object type, while the latter **directly creates an object** of that type.

In the first statement, `let person1: {name: string; age: number};`, we are defining a **type alias** called `person1`. **This declaration does not create an actual object**; it only **defines the shape of an object** that can be created later.

In the second statement, `let person2 = {name: string; age: number};`, we are **creating an actual object** of the type `person1`.

---

### Function Types

In TypeScript is that we can precisely control the kinds of functions assignable to a variable. We do this using function types, which specify the **argument types** and **return type** of a function.

Here’s an example of a function type that is only compatible with functions that take in two string arguments and return a number :

```ts
type StrToNum = (arg0: string, arg1: string) => number;
```

We must never be tempted to omit the **parameter names** or the **parentheses around the parameters** in a function type annotation, even if there is only one parameter.

Function types are most useful when applied to callback functions.

Example :

```ts
// This is a function type alias
type NumberArrayToNumber = (numberArray: number[]) => number;

// This function uses a function type alias
let sumAll: NumberArrayToNumber = function (numbers: number[]) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
};

// This function also uses the same function type alias
let computeAverage: NumberArrayToNumber = function (numbers: number[]) {
  return sumAll(numbers) / numbers.length;
};

console.log(computeAverage([5, 10, 15])); // Prints 10
```

---

### Generic Types.

TypeScript’s generics are ways to create **collections of types** that share certain formal similarities.

To define a generic type alias, use the `type` keyword followed by the alias name and angle brackets `<...>` containing a symbol for the generic type and assign it a custom definition. The symbol can be any alphanumeric character or string.

Here’s an example:

```ts
type Family<T> = {
  parents: [T, T];
  mate: T;
  children: T[];
};
```

This code defines a collection of object types, with a different type for every value of `T`. The generic `Family<T>` cannot actually be used as a type in a type annotation.

Instead, we must substitute `T` with some type of our choosing, let's choose `string`. Then, `Family<string>` is exactly the same as the object type given by setting `T` to :

```ts
string: {
  parents: [string,string],
  mate: string,
  children: string[]
}
```

In general, writing generic types with `type typeName<T>` allows us to use `T` within the type annotation as **a type placeholder**. Later, when the generic type is used, **T is replaced with the provided type**.

Another Example :

```ts
// A generic Family
type Family<T> = {
  parents: [T, T];
  children: T[];
};

// two type aliases for Species
type Human = { name: string; job: string };
type Dog = { name: string; tailWagSpeed: number };

// a human family which uses Family generics with Human alias
let humanFamily: Family<Human> = {
  parents: [
    { name: "Mom", job: "software engineer" },
    { name: "Dad", job: "web3 engineer" },
  ],
  children: [{ name: "kohli", job: "cricketer" }],
};

// a dog family which uses Family generics with Dog alias
let dogFamily: Family<Dog> = {
  parents: [
    { name: "Momo", tailWagSpeed: 3 },
    { name: "Dado", tailWagSpeed: 100 },
  ],
  children: [{ name: "Puppin", tailWagSpeed: 0.001 }],
};
```

---

### Generic Functions

Similar to typed functions, we can also use generics to create collections of typed functions.

Imagine we wanted to create a function that returns arrays filled with a certain value, the JavaScript would be :

```js
let getFilledArray = (value, n) => {
  return Array(n).fill(value);
};
```

Here, `getFilledArray('cheese', 3)` evaluates to `['cheese', 'cheese', 'cheese']`. No problem, right? Well, we run into a problem when we try to specify the function’s return type.

We know it should be an array of whatever value‘s type is—do we have to write a separate type annotation for every type of value? Nope. Here, we are rescued by generic functions!

```ts
type getFilledArray<T>(value: T, n: number): T[] => {
  return Array(n).fill(value);
}
```

This still evaluates to `['cheese', 'cheese', 'cheese']`, but the function is now **correctly typed and less prone to errors**. The function `getFilledArray<string>` is precisely the same as if we had written it in its type annotation.

```ts
getFilledArray(value: string, n: number): string[]
```