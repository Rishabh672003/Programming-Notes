console.log('Start')

function loginUser(email, password) {
    setTimeout(() => {
        // console.log("Now we have the data!"); // to check what's going on.
        return { userEmail: email }
    }, 5000)
}

const user = loginUser('abc@xyz.com', 123456)
console.log(user)

console.log('End')

/*
output :-
Start
undefined
End

We need to pass a callback function inorder to fetch the data.
*/
console.log('\n')
console.log('Start')

function loginUser2(email, password, callback) {
    // passing a callback as third argument.
    setTimeout(() => {
        console.log('Now we have the data!') // to check what's going on.
        callback({ userEmail: email, userPass: password })
    }, 5000)
}

function getVideo(email, callback) {
    setTimeout(() => {
        callback(['video1', 'video2', 'video3'])
    }, 2000)
}

const user2 = loginUser2('abc@xyz.com', 123456, (user2) => {
    console.log(user2)
    getVideo(user2.userEmail, (videos) => {
        console.log(videos)
    })
})
console.log('End')

/*
output :-
Start
End
Now we have the data!
{ userEmail: 'abc@xyz.com', userPass: 123456 }
[ 'video1', 'video2', 'video3' ]
*/

/*
- It defines a function loginUser2 that simulates an asynchronous operation using setTimeout.
- After the delay of 5 seconds, it logs "Now we have the data!" and invokes the callback function
  with an object containing the userEmail property set to the provided email parameter.
- The loginUser2 function is called with an email, password, and a callback function.
- The callback function logs the user2 object to the console.
*/

// adding more and more callback is called a "Callback Hell"and is quite had to read.

// Promises are used to fix these callback hell
