## Interfaces in Typescript

**Table of content :**

1. What is an Interface?
2. Composed Types.
3. Extending Interfaces.
4. Indexed Signatures.
5. Optional Type Members.

---

### What is an Interface?

In TypeScript, there’s another way to define types with the `interface` keyword. An interface is specifically **used to create typed objects**.

Both a `type` and an `interface` can create a typed object. The syntaxes for `type` and `interface` are slightly different, since `interface` does not require an equals sign (`=`) before the typed object.

Both `type` and `interface` will enforce the typed object at compile time when typing a variable.

The biggest difference between `interface` and `type` is that `interface` can only be used to type objects, while `type` can be used to type objects, primitives, and more. **As it turns out, `type` is more versatile and functional than `interface`.**

```ts
// a type
type Mail = {
  postagePrice: number;
  address: string;
};

// an interface
interface Mail {
  postagePrice: number;
  address: string;
}
```

As an `interface` is an abject, we can nest typed object to create `Deep Types`.

Example :

```ts
interface Robot {
  about: {
    general: {
      id: number;
      name: string;
    };
  };
  getRobotId: () => string;
}
```

Within the `Robot` interface, the `general` typed object is nested inside the `about` typed object. TypeScript allows us to infinitely nest objects so that we can describe data correctly.

---

### Composed Types

As our data gets nested deeper, we’ll start to have typed objects that become unwieldy to write and read.

To solve this, TypeScript allows us to compose types. We can define multiple types and reference them inside other types.

```ts
interface About {
  general: General; // composition of General interface
}

interface Version {
  versionNumber: number;
}

interface General {
  id: number;
  name: string;
  version: Version; // composition of Version interface
}
```

---

### Extending Interfaces (Inheritance)

Like JavaScript classes, an interface can inherit properties and methods from another interface using the extends keyword. Members from the inherited interface are accessible in the new interface.

```ts
interface Shape {
  color: string;
}

// inheritance
interface Square extends Shape {
  sideLength: number;
}

const mySquare: Square = { sideLength: 10, color: "blue" };
```

---

### Indexed Signatures

When typing objects in TypeScript, sometimes it’s not possible to know the property names for an object, like when we get back information from an outside **data source/API**.

While **we may not know the exact property names** at compile-time, **we may know what the data will look like** in general. In that case, it’s useful to write an object type that allows us to include a variable name for the property name. This feature is called index signatures.

Imagine we query a map API to get a list of **latitudes** where a solar eclipse can be viewed. The data might look like:

```json
{
  "40.712776": true;
  "41.203323": true;
  "40.417286": false;
}
```

We know that all the property names will be `strings`, and all their values will be `booleans`, but **we don’t know what the property names will be**.

To type this object, we can utilize an index signature to type this object. We could write this object’s type like this:

```ts
interface SolarEclipse {
  [latitude: string]: boolean;
}
```

In the `SolarEclipse` type, there’s an index signature used for defining a variable property name of each type member.

The `[latitude: string]` syntax defines every property name within SolarEclipse as a string type will have a value of type boolean.

In the `[latitude: string]` syntax, the `latitude` name is purely for us, the developer, as a human-readable name that will show up in potential error messages later.

Example :

```json
// data from api
{
  "shopping": 150,
  "food": 210,
  "utilities": 100
}
```

```ts
// using indexed signature interface
import { getBudgetAsync } from "./api";

interface Budget {
  [category: string]: number;
}

let getBudget = async () => {
  const result: Budget = await getBudgetAsync();
  console.log(result);
};

getBudget();
```

```
output :
{ shopping: 150, food: 210, utlities: 100 }
```

---

### Optional Type Members

Every interface code within this file so far assumes that every type member is required, however, TypeScript allows us to make some type members optional.

We can denote any type member as optional using the `?` operator after the property name and before the colon (`:`), like this: `size?: string;`.

Since `.size` is optional, we added a conditional to check if it exists before trying to use the `.size` property.

```ts
interface OptionsType {
  name: string;
  size?: string; // optional
}

let listFile = (options: OptionsType) => {
  let fileName = options.name;

  if (options.size) {
    fileName = `${fileName}: ${options.size}`;
  }

  return fileName;
};
```

The optional parameter allows us to call `listFile()` with a parameter that does not include a size property at all, like this:

```ts
listFile({ name: "readme.txt" });
```

---

Wohooo..!!! <br>
Here we complete out Vanilla TypeScript notes. <br>
Now, refer [TypeScript for React](../TypeScript-For-React/) to implement some important TypeScript concepts for React or NextJs to upgrade your Frontend skills!

Made with ❤️ by [Amit](https://github.com/amitsuthar69).
