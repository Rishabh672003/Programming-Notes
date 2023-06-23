# Introduction :

JavaScript does not use datatypes as opposed to c , c++ , Java. It has three initialisation techniques namely

- [let](https://github.com/amitsuthar69/Programming-Notes/blob/main/JavaSript/variables.md#let)
- [var](https://github.com/amitsuthar69/Programming-Notes/blob/main/JavaSript/variables.md#var)
- [const](https://github.com/amitsuthar69/Programming-Notes/blob/main/JavaSript/variables.md#const)

Semicolon " ; " is not essential to put at the end of every line but it is a good practice if you do so

---

# Arrays

```js
let arr = [1, 2, 3, 4]

//This creates an array of length 3, as the indexing starts from 0 , even though you can see four elements inside the array
```

## Adding elements in the front:

```js
let arr = [1, 2, 3, 4]
arr.unshift(-1, 0)

//You can also use

arr.concat(arr(-1, 0))

/*these techniques will add two elements in the beginning of the array
output:
[-1 , 0 , 1 , 2 , 3 , 4] */
```

---

# Functions :

### Different ways to declare a function:

```js
function fn(){ }
//OR
const fn = function(){ }
//OR
const fn => { }
```

Here "fn" is the function name

---

# **forEach** :

- Creates a function for each element of an array
- It does not return a value

```js
arr.forEach(function fn(arr) {
  console.log(arr + 2)
})
```

This will display each element of the array after adding 2 to them

---

# **Map** :

- This creates a new array consisting the functions of each element of other array

```js
let arr1 = arr.map((item) => {
  return item + 2
})
```

The values of array "arr" will increase by 2 and get returned to new array "arr1"

---

# **Filter** :

- It follows the boolean concept
- It creates a new array and puts only those values which fulfill the criteria mentioned by you

```js
let f1 = arr.filter((arr) => {
  return arr > 2
})

// This will print only those numbers present in array "arr" which are greater than 2
```
