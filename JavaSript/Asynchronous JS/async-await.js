/*
- There is a special async-await syntax by which we can make any function Async and then make promises await in it.
- An Async function always returns a Promise other values are wrapped in a Promise automatically.
*/

// async function f1() {
//     return 5;
//     // 5 was not a Promise but now it is wrapped in a Promise because of 'async' syntax.
// }
// f1().then((value) => { console.log(value) }); // Prints 5



async function f2() {
    let delhiWeather = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("31 Deg");
        }, 3000);
    })

    let bangloreWeather = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("29 Deg");
        }, 5000);
    })

    // delhiWheather.then(value => { console.log(value) })
    // bangloreWheather.then(value => { console.log(value) })


    console.log("Fetching Delhi Weather please wait...") // PROOF THAT FUNCTION EXECUTION STOPS HERE !
    let delhi = await delhiWeather;
    /* Delhi weather will be fulfilled first and fetch it's value, 
    Execution will be awaited(stopped) unless it is fulfilled.
    Once it is fufilled, then the function executon will continue. */
    console.log("Fetched Delhi Weather is: " + delhi);


    console.log("Fetching Banglore Weather please wait...") // PROOF THAT FUNCTION EXECUTION STOPS HERE !
    let banglore = await bangloreWeather;
    /* Once delhiWeather is fulfilled then, bangloreWeather will be fulfilled. */
    console.log("Fetched Banglore Weather is: " + banglore);

    return [delhi, banglore]; //  returns array of values.
}

let a = f2();

const cherry = async () => { console.log("Hello I am cherry & I'm not waiting here."); }
let b = cherry();
/*
output :-
Fetching Delhi Weather please wait...
Hello I am cherry
Fetched Delhi Weather is: 31 Deg
Fetching Banglore Weather please wait...
Fetched Banglore Weather is: 29 Deg
*/
// this cherry  function runs parallely with f1() no matter f1() is in await.
// cherry() will be executed just before the first 'await'.
// if we had some more functions in between, they too runs parallely.


/*
FROM LINE : 52, If we want that the cherry() functions execute after f2(), we can put entire function call
into an async function, and then if we await f2() and await cherry(); then first f1() will execute and then cherry();
*/

// const main1 = async () => {
//     let a = await f2(); // value of promise will come into a
//     let b = await cherry(); // cherry() waits here !!
//     // now a will execute first and then b.
// }
// main1();

/*
output :-
Fetching Delhi Weather please wait...
Fetched Delhi Weather is: 31 Deg
Fetching Banglore Weather please wait...
Fetched Banglore Weather is: 29 Deg
Hello I am cherry
*/