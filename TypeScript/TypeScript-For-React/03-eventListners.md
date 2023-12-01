## Type defining Event Listners

Passing a parmeter inside an event handler leds us to `type: any` error. To avoid this, we can use `React.MouseEvent` interface to handle the type of parameter.

```tsx
import { useState } from "react";

type UserProps = {
  id: number;
  title: string;
};

export default function User({ id, title }: UserProps) {
  const [newTitle, setNewTitle] = useState("");

  const handleClick = (e: React.MouseEvent) => {
    setNewTitle("New Title");
    e.preventDefault;
  };

  return (
    <div>
      <h1>{title}</h1>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}
```

**It's not only limited to MouseEvent, it can be anything that React supports.**

---

**Few other interfaces that are similar to React.MouseEvent :**

`React.FormEvent`

`React.TouchEvent`

`React.PointerEvent`

`React.DragEvent`

`React.FocusEvent`
