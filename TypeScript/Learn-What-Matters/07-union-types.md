## Typescript Union Types

**Table of content :**

1. What are union types?
2. Type Narrowing.
3. Common property conflict.
4. Union in arrays.
5. Union with Literal types.

---

### What are union types?

TypeScript allows us to combine specific types together as a union type. This ccombined types can be anything among primitive or custom types.

A Union Type is a composite of selected types separated by a vertical bar, `|`.
We can create union types like this :

```ts
let unionType: string | number;

unionType = "Two"; // string type
unionType = 2; // number type
```

This `unionType` variable can only be a string or a number and nothing else.

---

### Type Narrowing

Type narrowing is when TypeScript can figure out what type a variable can be at a given point in our code. Type narrowing allows us to use unions, then perform type-specific logic without TypeScript getting in the way.

To do this, we could implement a type guard. A type guard is a conditional that checks if a variable is a certain type, like this:

```ts
function formatValue(value: string | number) {
  // type guard for type string
  if (typeof value === "string") {
    console.log(value.toLowerCase());
  }
  // type guard for type number
  if (typeof value === "number") {
    console.log(value.toFixed(2));
  }
}

formatValue("AMIT");
formatValue(69);
```

```
amit
69.00
```

Hence by type narrowing, we can perform different logic for differnt types in the same scope.

But NOTE that, any type specific property used outside the `if` block will raise cross type method usage error `Property 'blabla' does not exist on type 'blabla'.`

**TypeScript can infer the function’s return type, there’s no need for us to manually define it.**

TypeScript can recognize the `else` block of an `if/else` statement as being the opposite type guard check of the `if` statement’s type guard check.

Example :

```ts
let formatPadding = (padding: string | number) => {
  if (typeof padding === "string") {
    return padding.toLowerCase();
  } else {
    return `${padding}px`;
  }
};
```

---

**Using in with Type Guards :**

Instead of using `typeof`, we can still perform type narrowing using the `in` opertor. The in operator checks if a property exists on an object itself or anywhere within its prototype chain.

Example :

```ts
type Tennis = {
  serve: () => void;
};

type Soccer = {
  kick: () => void;
};

function play(sport: Tennis | Soccer) {
  if ("serve" in sport) {
    return sport.serve();
  }

  if ("kick" in sport) {
    return sport.kick();
  }
}
```

---

### Common property conflict

When we put type members in a union, TypeScript will only allow us to use the **common methods and properties** that **all members** of the union share.

Example :

```ts
type Goose = {
  isPettable: boolean;
  hasFeathers: boolean;
};

type Moose = {
  isPettable: boolean;
  hasHoofs: boolean;
};

const pettingZooAnimal: Goose | Moose = {
  isPettable: true,
};

console.log(pettingZooAnimal.isPettable); // print true
console.log(pettingZooAnimal.hasHoofs); // TypeScript error
```

---

### Unions in Arrays

TypeScript allows us to declare a union of an array of different types.

To create a union that supports multiple types for an array’s values, wrap the union in parentheses (string | number), then use array notation [].

eg : `let myArray: (number | string)[] = [1, '1']`

For instance, we can represent time in TypeScript with a number or a string type.

```ts
const dateNumber = new Date().getTime();
const dateString = new Date().toString();

const timesList: (string | number)[] = [dateNumber, dateString];
```

---

### Union with Literal types

You can declare a union type consisting of literal types, such as string literals, number literals or boolean literals. These will create union types that are more specific and have distinct states.

```ts
type Color = "green" | "yellow" | "red";
```

---

Example :

```ts
type Status = "idle" | "downloading" | "complete";

let downloadStatus = (status: Status) => {
  if (status === "idle") {
    console.log("Download");
  }
  if (status === "downloading") {
    console.log("Downloading...");
  }
  if (status === "complete") {
    console.log("Your download is complete!");
  }
};

downloadStatus("complete");
```

```
Your download is complete!
```
