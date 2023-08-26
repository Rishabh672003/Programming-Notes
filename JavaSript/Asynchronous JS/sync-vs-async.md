```js
// Synchronous Code : Code that runs in order; top-down.
// Asynchronous Code : Code that runs in parallel with other code.

// sync codee :-
console.log("START");
function f1() {
  console.log("We're in an other function.");
  console.log("Doing some stuff.");
}
f1();
console.log("END");
console.log("\n");
// Code executes line by line (top-down)
/*
output:
START
We're in an other function.
Doing some stuff.
END
*/

// Async code :-
console.log("START");
setTimeout(() => {
  console.log("We're in Timeout");
}, 3000);
console.log("END");
/*
output:
START
END
We're in Timeout
*/
```
