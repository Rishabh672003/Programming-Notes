```js
/*
Promise API Is nothing but some Promise Class methods.
1. Promise.all() : if we want all the values at same time, when every promise is resolved, we use promise.all()
   but, promise.all() only works for all resolved values and fails if any of the promise gets rejected.
   So if still we want to get the values, even if any of the promise is rejected, we use promise.allSettled()
2. Promise.allSettled() : if any of the promise is rejected, we ccan still get other values by using this method.

3. Promise.race() : outputs only the first resolved or rejected promise.

4. Promise.any() ;Only Waits for the first resolved promise(Not Rejected) to be fullfill,
   and it's result becomes outcome. Thus, Aggergates error if somehow all the promises are rejected.
5. Promise.resolve(value) : makes a resolved promise with given value.

6. Promise.reject(error) : mkaes a rejected promise with given error.
*/

function f1() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Value 1 Resolved.");
    }, 2000);
  });
}

function f2() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // resolve("Value 2 Resolved.")
      reject(new Error("Error Occured"));
    }, 4000);
  });
}

function f3() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Value 3 Resolved.");
    }, 6000);
  });
}

// f1().then(value => { console.log(value); }); // Resolves in 2 secs independently.
// f2().then(value => { console.log(value); }); // Resolves in 4 secs independently.
// f3().then(value => { console.log(value); }); // Resolves in 6 secs independently.

/*
In real world, we dont know when the promise going to be resolved !! So if we want all the values,
at same time when every promise is resolved, we use promise.all()
*/

// let promise_all = Promise.all([f1(), f2(), f3()]);
// now when all the values get resolved (i.e; at 6 secs), the values will be arrayed.

// let promise_all = Promise.allSettled([f1(), f2(), f3()]);
// still we've have values, eventhough value2 is rejected.

// let promise_all = Promise.race([f1(), f2(), f3()]);
// prints only the first / fastest resolved promise.

let promise_all = Promise.any([f1(), f2(), f3()]);

promise_all.then((value) => {
  console.log(value);
});
```
