## Custom TypeScript Types

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
ordersArrayTS.push([Pet.Jerboa, 3]);
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
