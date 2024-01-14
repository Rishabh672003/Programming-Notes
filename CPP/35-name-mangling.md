# Name Mangling

Name mangling in C++ is a technique used to resolve conflicts between identifiers that have the same name but belong to
different scopes or have different types. This process transforms function names into unique identifiers that can be
distinguished by the linker during the linking phase of compilation.

However, it's important to note that name mangling is platform-specific. The C++ ABI (Application Binary Interface) of
the platform you are running on defines the name mangling. There are two common C++ ABIs, which are the Itanium ABI and
Microsoft's ABI. Depending on the platform and the compiler being used, different name mangling schemes may be applied .

The C++ standard does not define a specific naming convention for mangled names, so different compilers may implement
name mangling differently. However, mangled names typically start with \_Z followed by the mangled name of the function
or variable, including namespace, classes, and name, with a length and the identifier 1.

Here's an example of name mangling in action:

```cpp
namespace MyNamespace {
class MyClass {
  public:
    void myMethod(int param);
};
} // namespace MyNamespace
```

The mangled name of `myMethod` might look something like `_ZN11MyNamespace7MyClass9myMethodEi`, which includes the
namespace (`MyNamespace`), the class (`MyClass`), the method name (`myMethod`), and the parameter type (`int`).

To understand the mangled names, you can use a tool like `c++filt`. `c++filt` is a command-line utility that comes with
the GNU Binutils package and is used to demangle C++ symbols. By piping the output of `nm` (another command-line utility
that lists symbols from object files) through `c++filt`, you can see the demangled names of the symbols.

Here's how you might use `c++filt`:

```bash
nm myprogram.o | c++filt
```

This command will print out the names of all symbols in `myprogram.o`, with the mangled names replaced by their
demangled equivalents.

Output:

```
0000000000003df0 d _DYNAMIC
0000000000003fe8 d _GLOBAL_OFFSET_TABLE_
0000000000002000 R _IO_stdin_used
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
0000000000002004 r __GNU_EH_FRAME_HDR
0000000000004010 D __TMC_END__
0000000000004010 B __bss_start
                 w __cxa_finalize@GLIBC_2.2.5
0000000000004000 D __data_start
0000000000004008 D __dso_handle
                 w __gmon_start__
                 U __libc_start_main@GLIBC_2.34
0000000000004010 D _edata
0000000000004018 B _end
000000000000112c T _fini
0000000000001000 T _init
0000000000001020 T _start
0000000000004000 W data_start
0000000000001119 T main
```
