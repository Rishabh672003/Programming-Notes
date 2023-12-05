## Generic Types. (Important)

**Table of content :**

1. What are generics?
2. Generic Functions.

---

### What are generics ?

TypeScript’s generics are ways to create **collections of types** that share certain formal similarities and ahave relationship between them. They often create a general rule to be followed.

To define a generic type alias, use the `type` keyword followed by the alias name and angle brackets `<...>` containing a symbol for the generic type and assign it a custom definition. The symbol can be any alphanumeric character or string.

Here’s an example:

```ts
type Family<T> = {
  parents: [T, T];
  mate: T;
  children: T[];
};
```

This code defines a collection of object type, with a general type for every value of `T`. The generic `Family<T>` cannot actually be used as a type in a type annotation.

Instead, we must substitute `T` with some type of our choosing, let's choose `string`. Then, `Family<string>` is exactly the same as the object type given by setting `T` to :

```ts
// a non-generic alias
string: {
  parents: [string, string],
  mate: string,
  children: string[]
}
```

As we can see, **instead of being specific about the type of Family to be a string or number, We are being more General to the type** of Family.

This also creates a **relationship between the types**.

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

Imagine we wanted to create a function that returns arrays filled with a certain value :

```js
let getFilledArray = (value: string, n: number): string[] => {
  return Array(n).fill(value);
};
getFilledArray("cheese", 3);
```

Here, `getFilledArray('cheese', 3)` evaluates to `['cheese', 'cheese', 'cheese']`.

No problem, right? Well, what **if we're unknown to the type of value** being passed in the `getFilledArray` function. What if someone passes a `boolean` value instead of a string but still we want our code to give correct output.

Then, do we have to write a separate type annotation for every type of value? Nope. Here, we are rescued by generic functions!

```ts
type getFilledArray<T, N>(value: T, n: N): T[] => {
  return Array(n).fill(value);
}
```

This still evaluates to `['cheese', 'cheese', 'cheese']`, but now it not only works for string, but also works for value of any type!
In this case, the type of `value` and return type would be same i.e; `T` mans they both are related to each other. On the other hand the type of n i.e; `N` is an independent type.

---

```ts
// this example will clear the concept of generics :
let createArrayPair = <T, N>(item1: T, item2: N): [T, N] => {
  return [item1, item2];
};

/* Here we've specified relatonship between 
the inputs and the return value. */
```
