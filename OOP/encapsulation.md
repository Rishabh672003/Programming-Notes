# Encapsulation

Encapsulation is a fundamental concept in object-oriented programming (OOP). It
refers to the bundling of data and methods into a single unit, called a class.

The key idea behind encapsulation is to create a protective barrier around an
object's internal state, preventing direct access to its data from outside the
object. Instead, external entities interact with the object through well-defined
methods, which serve as the object's interface or API (Application Programming
Interface).

## Access modifiers

To achieve encapsulation in OOP, you typically use access modifiers to control
the visibility and accessibility of class members:

1. Public: Public members are accessible from anywhere, including external code.
They form the object's public interface.

2. Private: Private members are only accessible within the class itself. They
cannot be accessed or modified directly from external code.

3. Protected: Protected members are accessible within the class itself and its
subclasses (derived classes). They provide a limited level of accessibility for
inheritance scenarios.

4. Default (Package-private): Members without an explicit access modifier are 
accessible within the same package.
