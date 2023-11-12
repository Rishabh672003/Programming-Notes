# Array Methods

- [Splice](#splice)
- [Slice](#slice) 
- [Concat](#concat)
- [ForEach](#foreach)
- [IndexOf/LastIndexOf](#indexof-lastindexof)
- [Includes](#includes)
- [Find(left->right) and FindLast(right->left)](#findleftright-and-findlastrightleft)
- [Filter](#filter)
- [Map](#map)
- [Sort](#sort)
- [Reverse](#reverse)
- [Split](#split)
- [Join](#join)
- [Reduce](#reduce)
- [Some](#some)
- [Every](#every)
- [CopyWithin](#copywithin)
- [Fill](#fill)
- [Flat](#flat)
- [FlatMap](#flatmap)

## Splice

Syntax: `arr.splice(index[, deleteCount, elem1, ..., elemN])`

The mentioned elements are inserted at the index.

```javascript
let arr = ["I", "study", "JavaScript", "right", "now"];

// remove 3 first elements and replace them with another
arr.splice(0, 3, "Let's", "dance");
alert(arr) // now ["Let's", "dance", "right", "now"]
```
```javascript
let arr = ["I", "study", "JavaScript", "right", "now"];

// remove 2 first elements
let removed = arr.splice(0, 2);
alert(removed); // "I", "study" <-- array of removed elements
alert(arr); // "JavaScript", "right", "now" 
```

`splice` method is also able to insert the elements at the index without any removals. For that, we need to set `deleteCount` to 0. Negative indices are allowed too (they specify the position from the end of the array).

## Slice

Syntax: `arr.slice([start], [end])`

Returns a new array containing all items from index `start` to `end` (not including `end`).

```javascript
let arr = ["t", "e", "s", "t"];

alert(arr.slice(1, 3)); // e,s (copy from 1 to 3)
alert(arr.slice(-2)); // s,t (copy from -2 till the end)
```

## Concat

Syntax: `arr.concat(arg1, arg2...)`

Creates a new array that includes values from other arrays and additional items.

```javascript
let arr = [1, 2];

// create an array from: arr and [3,4]
alert(arr.concat([3, 4])); // 1,2,3,4

// create an array from: arr and [3,4] and [5,6]
alert(arr.concat([3, 4], [5, 6])); // 1,2,3,4,5,6

// create an array from: arr and [3,4], then add values 5 and 6
alert(arr.concat([3, 4], 5, 6)); // 1,2,3,4,5,6
```

## ForEach

Syntax: 

```javascript
arr.forEach(function(item, index, array) {
     ... do something with item
});
```

```javascript
["Bilbo", "Gandalf", "Nazgul"].forEach((item, index, array) => {
    alert(`${item} is at index ${index} in ${array}`);
});
```

## IndexOf/LastIndexOf

Syntax: `arr.indexOf(item, from)` and `arr.lastIndexOf(item, from)`

Returns the index of the item if found, else -1.

```javascript
let fruits = ['Apple', 'Orange', 'Apple']

alert(fruits.indexOf('Apple')); // 0 (first Apple)
alert(fruits.lastIndexOf('Apple')); // 2 (last Apple)
```

## Includes

Syntax: `arr.includes(item, from)`

Returns true if the array has the item, else false.

```javascript
let fruits = ['Apple', 'Orange', 'Apple']
alert(fruits.includes("Apple")); // true
```

## Find(left->right) and FindLast(right->left)

Syntax: 

```javascript
arr.find(function(item, index, array) {
    // if true is returned, item is returned and iteration is stopped
    // for falsy scenario returns undefined
});
``` 
```javascript
arr.findIndex(function(item, index, array) {
    // if true is returned, item is returned and iteration is stopped
    // for falsy scenario returns undefined
});
```

```javascript
let users = [
    { id: 1, name: "John" },
    { id: 2, name: "Pete" },
    { id: 3, name: "Mary" },
    { id: 4, name: "John" }
];

// Find the index of the first John
alert(users.findIndex(user => user.name == 'John')); // 0 

// Find the index of the last John
alert(users.findLastIndex(user => user.name == 'John')); // 3
```

## Filter

Syntax: 
```javascript
let results = arr.filter(function(item, index, array) {
    // if true item is pushed to results and the iteration continues
    // returns empty array if nothing found
});
```

Example:
```javascript
let users = [
    { id: 1, name: "John" },
    { id: 2, name: "Pete" },
    { id: 3, name: "Mary" }
];

// returns array of the first two users
let someUsers = users.filter(item => item.id < 3);
alert(someUsers.length); // 2
```

## Map

Syntax: 
```javascript
let result = arr.map(function(item, index, array) {
    // returns the new value instead of item
});
```

Example:
```javascript
let lengths = ["Bilbo", "Gandalf", "Nazgul"].map(item => item.length);
alert(lengths); // 5,7,6
```

## Sort

Syntax: `arr.sort([compareFunction])`

By default, it sorts the values as strings + modifies the older string.

Use `localeCompare` for Strings:

```javascript
let countries = ['Österreich', 'Andorra', 'Vietnam'];

alert( countries.sort( (a, b) => a > b ? 1 : -1) ); // Andorra, Vietnam, Österreich (wrong)
alert( countries.sort( (a, b) => a.localeCompare(b) ) ); // Andorra,Österreich,Vietnam (correct!)
```

Use `compareFunction` for numbers:

```javascript
function compareNumeric(a, b) {
    if (a > b) return 1;
    if (a == b) return 0;
    if (a < b) return -1;
}

let arr = [ 1, 2, 15 ];
arr.sort(compareNumeric);
alert(arr);  // 1, 2, 15
```

## Reverse

Syntax: `arr.reverse()`

Reverses the order

 of the elements in the array.

```javascript
let arr = [1, 2, 3, 4, 5];
arr.reverse();
```

## Split

Syntax: `str.split(delim)`

Splits the string into an array by the given delimiter delim.

```javascript
let names = 'Bilbo, Gandalf, Nazgul';
let arr = names.split(', ');
for (let name of arr) {
  alert( `A message to ${name}.` ); // A message to Bilbo  (and other names)
}
```

## Join

Syntax: `arr.join(glue)`

Joins the array into a string using glue.

```javascript
let arr = ['Bilbo', 'Gandalf', 'Nazgul'];
let str = arr.join(';'); // glue the array into a string using ;
alert( str ); // Bilbo;Gandalf;Nazgul
```

## Reduce

Syntax: 
```javascript
arr.reduce(function(accumulator, item, index, array) {
    // ...
}, [initial]);
```

```javascript
let arr = [1, 2, 3, 4, 5];

// removed initial value from reduce (no 0)
let result = arr.reduce((sum, current) => sum + current);
alert( result ); // 15
```

## Some

Syntax: `arr.some(function(item, index, array) { // returns true if the function returns true for any array element })`

```javascript
const array = [1, 2, 3, 4, 5];
const even = (element) => element % 2 === 0; // Checks whether an element is even
console.log(array.some(even)); // true
```

## Every

Syntax: `arr.every(function(item, index, array) { // returns true if the function returns true for all array elements })`

```javascript
const isBelowThreshold = (currentValue) => currentValue < 40;
const array1 = [1, 30, 39, 29, 10, 13];
console.log(array1.every(isBelowThreshold)); // true
```

## CopyWithin

Syntax: `arr.copyWithin(target, start, end)`

Copies its elements to another position in the array, overwriting the existing values.

```javascript
let arr = [1, 2, 3, 4, 5];
arr.copyWithin(0, 3); // copy to 0th index from the 3rd index
alert( arr ); // 4,5,3,4,5
```

## Fill

Syntax: `arr.fill(value, start, end)`

Fills the array with repeating value from index start to end.

```javascript
let arr = [1, 2, 3, 4];

// Fill with 0 from position 2 until position 4
console.log(arr.fill(0, 2, 4)); // Array [1, 2, 0, 0]

// Fill with 5 from position 1
console.log(arr.fill(5, 1)); // Array [1, 5, 5, 5]
console.log(arr.fill(6)); // Array [6, 6, 6, 6]
```

## Flat

Syntax: `arr.flat(depth)`

Creates a new array with all sub-array elements concatenated into it recursively up to the specified depth.

```javascript
const arr1 = [0, 1, 2, [3, 4]];
console.log(arr1.flat()); // Array [0, 1, 2, 3, 4]

const arr2 = [0, 1, [2, [3, [4, 5]]]];
console.log(arr2.flat()); // Array [0, 1, 2, Array [3, Array [4, 5]]]
console.log(arr2.flat(2)); // Array [0, 1, 2, 3, Array [4, 5]]
console.log(arr2.flat(Infinity)); // Array [0, 1, 2, 3, 4, 5]
```

## FlatMap

Syntax: 
```javascript
arr.flatMap(function callback(currentValue[, index[, array]]) {
    // return element for new_array
}[, thisArg])
```

First maps each element using a mapping function, then flattens the result into a new array.

```javascript
const arr = [1, 2, 1];
const results = arr.flatMap((num) => (num === 2 ? [2, 2] : 1));
console.log(results); // Array [1, 2, 2, 1]
```