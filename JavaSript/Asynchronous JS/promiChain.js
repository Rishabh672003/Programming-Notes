/*
- We can chain promises and resolved values can be passed one after the another.
- resolved value of one promise is passed to .then() and the resolved value of
this .then() is passed to next .then(); and so on...

--> Every call to a .then() returns a new Promise whose value is passed to the 
    next one and so on.
    We can even create custom Promises inside .then();
*/

// let p1 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         console.log("Resolved after 2 seconds.");
//         resolve("Promise 1 fulfilled.");
//     }, 2000);
// });

// p1.then((value) => {
//     console.log(value);
//     // let p2 = new Promise((resolve, reject) => {
//     //     setTimeout(() => {
//     //         resolve("Promise 2");
//     //     }, 2000);
//     // })
//     // return p2;
//     // instead of return p2, we can replace let p2 by return p2. (SEE BELOW)
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve("Promise 2");
//         }, 2000);
//     });

// }).then((value) => {
//     console.log("Promise 2 fulfilled");
//     return 2;
// }).then((value) => {
//     console.log("Promise P resolved immediately.")
// })

function f1() {
  return new Promise((resolve, reject) => {
    console.log("Not yet Resolved.");
    setTimeout(() => {
      resolve(1);
    }, 4000);
  });
}

f1()
  .then(() => {
    console.log("Congo we're resolved now.");
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("Resolved chained promise");
      }, 2000);
    });
  })
  .then(() => {
    console.log("Promise Chained");
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("Resolved Again");
      }, 4000);
    });
  })
  .then(() => {
    console.log("Promise Chained Again.");
  });

// LoadScript function using Promises.

// const loadScript = (src) => {
//     return new Promise((resolve, reject) => {
//         let script = document.createElement("script");
//         script.type = "text/javascript";
//         script.src = src;
//         document.body.appendChild(script);
//         script.onload = () => { resolve("Script loaded!") };
//         script.onerror = () => { reject(0) };
//     });
// };

// let p1 = loadScript("https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js");
// p1.then((value) => {
//     console.log(value);
//     return loadScript("https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js")
// }).then((value) => {
//     console.log("second script loaded")
// }).catch((error) => {
//     console.log("sorry, error loading script file");
// })
