## Component Props

In react, native tags has a lot of attributes and typing each of is not a good idea.

This below `Button` component has 3 button props for now (but it can be many) :

```tsx
const Home = () => {
  const handleClick = () => {};
  return (
    <div>
      <Button type="submit" onClick={handleClick} autoFocus={true} />
    </div>
  );
};

type ButtonProps = {
  type: "submit" | "reset" | "button";
  autoFocus?: boolean;
  onClick: () => void;
};

const Button = ({ type, autoFocus, onClick }: ButtonProps) => {
  return <button>Click me!</button>;
};
```

Instead of specifying types of individual properties, React helps us to deal this situation with a helper type, `React.ComponentProps<"...">` type. In the angle brackets, we can specify what tag it should be.

```tsx
type ButtonProps = React.ComponentProp<"button">;

const Button = ({ type, autoFocus, onClick }: ButtonProps) => return <button>Click me!</button>;
```

A hell lot of lines are taken away from our Button component as we have grouped the property types of a native button tag into a `React.ComponentProp<>` type.

We can also combine this ComponentProp with other custom prop types using **intersection (`&`)**:

```tsx
type ButtonProps = React.ComponentProp<"button"> & {
    backgroundColor?: "red" | "blue";
}

const Button = ({ type, autoFocus, onClick, backgroundColor }: ButtonProps) => return <button>Click me!</button>;
```

---

We can make our code more cleaner yet using `...rest` operator (passing arbitary number of parameters) of TypeScript.

```tsx
type ButtonProps = React.ComponentProp<"button">;

const Button = ({ type, ...rest }: ButtonProps) => return <button type={type} {...rest} >Click me!</button>;
```

The `...rest` allows all the other props to be extracted here without specifically mentioning each of them. All the other properties are now stored into the rest **array**.
