## The `tsconfig.json` file

The `tsconfig.json` is a TypeScript configuration file used by the `tsc` to specify **compiler options** and settings for our TypeScript project and is always placed in the root of your project.

It's a JSON-formatted file that allows us to customize the compiler's behavior and control various aspects of the compilation process.

---

A sample `tsconfig.json` file :

```json
{
  "compilerOptions": {
    "target": "es2017",
    "module": "commonjs",
    "strictNullChecks": true
  },
  "include": ["**/*.ts"]
}
```

- `"compilerOptions"` is a nested object that contains the rules for the TypeScript compiler to enforce.
  - `"target": "es2017"` means the project will be using the 2017 version of EcmaScript standards for JavaScript.
  - `"module": "commonjs"` means this project will be using the common JavaScript syntax to import and export modules.
  - `"strictNullChecks": true` ensures that variables can only have `null` or `undefined` values if they are **explicitly** assigned those values.
- `"inculde": ["**/*.ts"]` determines what files the compiler applies the rules to.

  In this case `["**/*.ts"]` means the compiler should check every single file that has a `.ts` extension.

---

We can now use the command `tsc` without any arguments in your terminal!

The compiler will automatically recognize from our `tsconfig.json` file, what specific files to run on.

We can still provide specific files like `tsc fileName.ts` if that’s the only file you want the compiler to check.
