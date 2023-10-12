## Data from an API

A normal react `.tsx` code.

```tsx
async function getData() {
  const res = await fetch("some-api-with-array-of-objects");
  return res.json();
}

export default async function UserData() {
  const data = await getData(); // error: data with type any
  return (
    <div>
      {data.map((post) => (
        <h2 key={post.id}>{post.title}</h2>
      ))}
    </div>
  );
}
```

---

the `data` is of `any` type and it then leds to type error. So to avoid that and also for the sake of a good practice we can do a type defintaion for the data we'll recieve.

```tsx
type DataProps = {
  id: number;
  title: string;
  message?: string; // ? --> a data we're not sure if we have it or not
}[]; // [] --> when your api returns an array of objects.

async function getData: Promise<DataProps>() {
    // adding a Interface Promise<Type>
    // ... other code
}
```

---

### Passing data to children :

Let's say your `UserData` component renders a children component `User` and passes the data fetched from api to it.

```tsx
// Inside UserData.tsx
import User from "@/components/User"

type DataProps = {
  id: number;
  title: string;
  message?: string;
}[];

async function getData: Promise<DataProps>() {
  const res = await fetch("some-api-with-array-of-objects");
  return res.json();
}

export default async function UserData() {
  const data = await getData(); // error: data with type any
  return (
    <div>
      {data.map((post) => (
        <User key={post.id} title={post.title} />
        {/* this child component doesn't know what type of data is id and title.*/}
      ))}
    </div>
  );
}
```

In the above code, the child component `User`doesn't know what type of data is is being passed to it.

So at the time of receiving these props inside the User function, we need to define the type.

```tsx
// inside User.tsx

type UserProps = {
  id: number;
  title: string;
  toggle?: true; // an optional prop which we may or may not receive from Parent component.
};

export default function User({ id, title }: UserProps) {
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}
```
