// using promises to resolve a callback hell.

/* Promise : Promising a Data Fetch from a network.
SYNTAX :-  let promise = new Promise(function (resolve, reject) { });
Fulfillment is done either in Resolve or Reject.
*/

// Promise is mostly used for parallel execution.


// --- RESOLVE ---
let promise1 = new Promise((resolve, reject) => {
    console.log("Promise_1 is Pending...")
    setTimeout(() => {
        console.log("Promise_1 resolved after 3 secs!");
        resolve(true);
    }, 3000);
});


// --- REJECT ---
let promise2 = new Promise((resolve, reject) => {
    console.log("Promise_2 is Pending...")
    setTimeout(() => {
        console.log("Promise_2 rjected!");
        reject(new Error("Oops! an Error Occured!"));
    }, 3000);
});

console.log(promise1, promise2);

const p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("got the user1");
        resolve({ name: "amit" });
    }, 3000);
});
p1.then(value => {
    console.log(value);
});

const p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        // resolve({ name: "amit" });
        reject(new Error("User2 not found!")); // making a custom error with a message by our own.
    }, 3000);
});
p2.catch(err => {
    console.log(err); // shows error log
    console.log(err.message); // shows only the message in new Error
});
console.log("\n");




// Rewriting the callbak hell userData code with help of promises :-

console.log("Start");

function loginUser(email, password) { // No ugly callbacks needed.
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("Now we have the data!"); // to check what's going on.
            resolve({ userEmail: email, userPass: password }); //resolve is invoked this time instead of a callback.
        }, 5000);
    })
};

function getVideo(email) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(['video1', 'video2', 'video3']);
        }, 2000);
    })
};

loginUser('amit', 'ababab')
    // it retrieves the user's email from the resolved Promise and calls the getVideo function with that email.
    .then(user => getVideo(user.email))

    // The getVideo function returns a Promise that resolves to an array of videos.
    .then(detail => console.log(detail));