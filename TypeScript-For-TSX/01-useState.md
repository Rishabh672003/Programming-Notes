## TypeScript in useState

Consider below example where we try to set state of an useState with a mismatched type which results in an error.

```tsx
"use client";
import {useState} form "react"

export default function UserPost(){
    const [title, setTitle] = useState("");
    const changeTitle = () => {
        setTitle(10); // error, type "number" is not assignable to a parametr of type setStateAction<string>
    }
    return (
        <div>
            <h1>{title}</h1>
        </div>
    )
}
```

The `error, type "number" is not assignable to a parametr of type setStateAction<string>` states that the state is expecting a "string" type parameter but we are passing a number which is not acceptable.

Also lets assume that you're **fetching some data from an api** and you don't have the data yet, so passing a `null` to `setTitle` will also result into an error.

```tsx
const changeTitle = () => {
  setTitle(null); // error, type "null" is not assignable to a parametr of type setStateAction<string>
};
```

---

To avoid this, we can specify the type while initializing a state.

```tsx
// ...other code
const [title, setTitle] = useState<string | null>("");
const changeTitle = () => {
  setTitle(null); // no error
};
// ...other code
```

here `useState<string | null>("")` handles the case for the data is it's a `null` and you can replace this `null` with any other type.
