```js
const p1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Resolved.");
  }, 3000);
});

//The first argument of .then() is a function that runs when the promise is resolved and receives the result.

//The second argument of .then() is a function that runs when the promise is rejected and receives the error.

p1.then(
  function (result) {
    /* handle a successful result */
    console.log(result);
  }, // shows "Resolved"
  function (error) {
    /* handle an error */
    console.log(error);
  }, // doesn't run if there's no error
);

/* If we’re interested only in successful completions, 
then we can provide only one function argument to .then()
or 
If we’re interested only in errors, then we can use .catch(errorHandlingFunction), 
which is exactly the same. */

// p1.catch(value); // shows "Error: Whoops!" after 1 second.

function f1() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ name: "amit", age: 19 });
    }, 3000);
  });
}
f1().then((value) => {
  // getting the resolved value
  console.log(value);
});

function f2() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      reject(new Error("An Error Occurred."));
    }, 3000);
  });
}
f2().catch((err) => {
  // catching the error
  console.log(err);
});
```
