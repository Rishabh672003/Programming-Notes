# Standard Template Library

The C++ Standard Template Library (STL) is a powerful feature of the C++ language that provides a set of
well-structured, generic C++ components that work together in a seamless way . It enables generic programming in C++, a
programming paradigm in which algorithms are written in terms of generic types, which are instantiated when needed for
specific types provided as parameters .

The STL is divided into three main components: containers, algorithms, and iterators.

**Containers**

Containers in STL are holder objects that store a collection of other objects (its elements). They are implemented as
class templates, which allows great flexibility in the types supported as elements. There are several types of
containers in STL:

- Sequence containers: Implement data structures that can be accessed sequentially.
- Associative containers: Implement sorted data structures that can be quickly searched.
- Unordered associative containers: Implement unsorted (hashed) data structures that can be quickly searched.
- Container adapters: Provide a different interface for sequential containers.

Here are some examples of containers:

```cpp
std::vector<int> vec;         // Vector container
std::set<int> s;              // Set container
std::map<int, std::string> m; // Map container
std::unordered_set<int> us;   // Unordered set container
std::stack<int> st;           // Stack container
std::queue<int> q;            // Queue container
```

**Algorithms**

Algorithms in STL are functions that operate on containers. They provide a way to perform common tasks like sorting,
searching, and manipulating data. Here's an example of using the `sort` algorithm with a vector:

```cpp
std::vector<int> vec = {5, 3, 2, 1, 4};
std::sort(vect.begin(), vect.end()); // Sorts the elements in a range in ascending order
std::reverse(vect.begin(), vect.end()); // Reverses the order of elements in a range
auto it = std::find(vect.begin(), vect.end(), value); // Searches for a specific element in a range and returns an iterator pointing to the first occurrence of the element
int count = std::count(vect.begin(), vect.end(), value); // Counts the number of elements in a range that match a specific value
auto max_it = std::max_element(vect.begin(), vect.end()); // Finds the maximum element in a range
auto min_it = std::min_element(vect.begin(), vect.end()); // Finds the minimum element in a range
int sum = std::accumulate(vect.begin(), vect.end(), 0); // Calculates the sum of elements in a range
bool found = std::binary_search(vect.begin(), vect.end(), value); // Determines whether a sorted range contains a specific value
std::next_permutation(vect.begin(), vect.end()); // Generates the next lexicographically greater permutation of a range
std::prev_permutation(vect.begin(), vect.end()); // Generates the previous lexicographically smaller permutation of a range
```

**Iterators**

Iterators in STL are objects that can navigate or iterate over elements in a container. They are essentially a
generalization of pointers and provide similar, but more advanced, behavior. Here's an example of using an
iterator with a vector:

```cpp
std::vector<int> vec = {1, 2, 3, 4, 5};
for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
    std::cout << *it << ' ';
}
```

The STL is highly beneficial for several reasons:

- **Reuse**: STL hides complex, tedious, and error-prone details, ensuring type-safe plug compatibility between STL
  components.
- **Flexibility**: Iterators decouple algorithms from containers, allowing for unanticipated combinations easily.
- **Efficiency**: Templates & inlining avoid virtual function overhead, and strict attention to time complexity of
  algorithms is maintained.
- **Competitive programming**: They can really help you in CP.
