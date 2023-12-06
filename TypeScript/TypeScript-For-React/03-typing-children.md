## Typing Children (React.ReactNode)

What is `ReactNode`?

`ReactNode` is a union type in React that represents any valid child element that can be passed to a component as a prop.

Using ReactNode for the children prop of your components has several benefits like Type safety, Readability, Performance, etc.

Using ReactNode :

```tsx
const MyComponent = (props: { children: React.ReactNode }) => {
  return <div>{props.children}</div>;
};
```

...to be continued.
