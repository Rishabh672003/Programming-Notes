## Typed Props in React

**Table of content :**

1. Inline Typed Props.
2. Type alias for Props.
3. Optional Props.
4. Union Literals in Prop Types.
5. CSSProprties Type.

In react, it's common that out functional component expects some external `props` in it. By default, those porps are typed `any` but then we loose the type safety of our props and that's something we don't want.

Hence it's necessary to correctly type props while extracting them into a component.

Below given is a typical javascript react app :

```tsx
export default function Home() {
  const handleClick = () => {};
  return (
    <div>
      <h2>Typed Props</h2>
      <Button onClick={handleClick} fontSize={24} bgColor="#57863f" />
    </div>
  );
}

// warning : fontSize, onClick and bgColor are implicitly typed any
export default function Button({ fontSize, bgColor, onClick }) {
  return (
    <div>
      <button onClick={onClick} classname={`bg-${bgColor}`}>
        this is a Buttton
      </button>
    </div>
  );
}
```

As we know that props are objects, we need to type each property in them. In the above example, **the component Button accepts destructured props which are implicitly typed to `any`**.

To type that prop object, we can use inline object type annotations.

```tsx
// no warning
export default function Button({
  fontSize,
  bgColor,
  onClick,
}: {
  foneSize: number;
  bgColor: string;
  onClick: () => void;
}) {
  return (
    <div>
      <button onClick={onClick} classname={`bg-${bgColor}`}>
        this is a Buttton
      </button>
    </div>
  );
}
```

Well this annotation avoid the implicit `any` warning and our props are type safe now. But still it's so messed up and looks so repetitive and ugly!

---

### Type alias for Props

To clear this clutter, we can use object type alias to make our prop types look good.

```tsx
type ButtonProps = {
  fontSize: number;
  bgColor: string;
  onClick: () => void;
};

export default function Button({ fontSize, bgColor, onClick }: ButtonProps) {
  return (
    <div>
      <button classname={`bg-${bgColor}`}>this is a Buttton</button>
    </div>
  );
}
```

This component now looks good.

---

### Optional Props

If we're not sure about an incoming prop or if we missed some props to pass into our component, we can still type those unsured props using **Optional type members** syntax.

```ts
// Here the `isActive` prop is typed optionally.

type ButtonProps = {
  fontSize: number;
  bgColor: string;
  isActive?: boolean;
};
```

---

### Return Type

By Default, `TSX` functional components has an implicit return type of `React.JSX.Element`. Hence we can avoid explicit typing of it as typescript infers it for us.

---

### Union Literals in Prop Types.

In our `ButtonProps`, we can also be more specific about the type of properties by using **Literal type unions**.

```ts
type ButtonProps = {
  bgColor: "red" | "blue" | "green";
  fontSize: number;
  isActive?: boolean;
};
```

Now the `string` type of our `bgColor` is more specific and limited to `red` `blue` or `green`.

If multiple properties do share same union literals, then we can also extract them out. to makt it less repetetive

```ts
type Color = "red" | "blue" | "green";

type ButtonProps = {
  bgColor: Color;
  fontColor: Color;
  fontSize: number;
  isActive?: boolean;
};
```

---

### CSSProprties Types

For now, all our props are CSS poroperties and we could have 100 of them so we can't type them all individually. Here React help us with it's `React.CSSProperties` type.

Here's how we can use it :

```tsx
export default function Home() {
  return (
    <div>
      <h2>Typed Props</h2>
      <Button
        style={{
          backgroundColor: "red",
          fontSize: 24,
          padding: "1rem 2rem",
          borderRadius: 8,
          borderColor: "transparent",
        }}
      />
    </div>
  );
}

type ButtonProps = {
  style: React.CSSProperties;
};

export default function Button({ style }: ButtonProps) {
  return (
    <div>
      <button style={style}>this is a Buttton</button>
    </div>
  );
}
```

The Style object in Button component can now have any number of props and we don't have to worry about styling them as `React.CSSProprties` handles everything.
