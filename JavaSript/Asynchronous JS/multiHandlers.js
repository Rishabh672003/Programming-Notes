function f1() {
    return new Promise((resolve, reject) => {
        console.log("Not yet Resolved.");
        setTimeout(() => {
            resolve(1);
        }, 4000);
    })
}

f1().then(() => {
    console.log("Congo we're resolved now.");
});

f1().then(() => {
    console.log("Congo we're resolved again.");
})

// This is not same as Promise Chaining !!!!
/*
- In Promise chaining, we return a new promise everytime we want add an another .then(), those promises 
  passes the result to each other.
- Multiple handlers doesn't passes the result to each other; instead they process it independently.
*/