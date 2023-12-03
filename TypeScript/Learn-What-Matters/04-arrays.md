## TypeScript Arrays

**Table of content :**

1. Array Type Annotations.
2. Tuples.
3. Arbitary or Rest parameters.
4. Spread Opeartor Syntax.

---

### Array Type Annotations

The TypeScript type annotation for array types is fairly straightforward, we put `[]` after the element type.

In this code, names is an Array that can only contain strings:

```ts
let names: string[] = ["Amit", "Rishabh"];
```

An alternative method is to use the generic type `Array<T>` syntax, where `T` stands for the type.

```ts
let age: Array<number> = [19, 20, 21];
```

We get a type error if we try to assign an array of `numbers` to a `string[]` variable. TypeScript arrays, however, can also throw errors when elements of the wrong type are tried to be pushed.

We can also declare multidimensional arrays; arrays of arrays.

```ts
let arr: string[][] = [
  ["str1", "str2"],
  ["more", "strings"],
];
```

---

### Tuples

In TypeScript, when an array is **typed with each elements of a specific type,** it’s called a tuple.

Example :

```ts
let ourTuple: [string, number, string, boolean] = [
  "Is",
  7,
  "our favorite number?",
  false,
];
```

Tuple types specify both the **lengths** and the **orders** of compatible tuples, and will cause an error if either of these conditions are not met.

```ts
let numbersTuple: [number, number, number] = [1, 2, 3, 4];
// Type Error! numbersTuple should only have three elements.

let mixedTuple: [number, string, boolean] = ["hi", 3, true];
/* Type Error! The first elements should be
a number, the second a string, and the third 
a boolean. */
```

Tuples have fixed lengths, so we cannot access elements of a tuple with indices greater than assigned.

---

### Arbitary or Rest parameters

Type annotations for an arbitary/rest parameter are identical to type annotations for arrays.

```ts
function smush(firstString: string, ...otherStrings: string[]) {
  // rest of code
}
```

The `...otherStrings` is now treated as an array of strings.

---

### Spread Opeartor Syntax

TypeScript’s tuples pairs with JavaScript’s spread syntax (...) and is most useful for function calls that use lots of arguments.

Example :

```ts
let performMove = (move: string, reps: number): void => {
  console.log(`I do the ${move} ${reps} times !`);
};

let moves: [string, number][] = [
  ["Jump", 6],
  ["clap", 4],
  ["flip", 3],
  ["flap", 2],
];

for (let i = 0; i < moves.length; i++) {
  performMove(...moves[i]);
}
```

output:

```
I do Jump 6 times !
I do clap 4 times !
I do flip 3 times !
I do flap 2 times !
```
