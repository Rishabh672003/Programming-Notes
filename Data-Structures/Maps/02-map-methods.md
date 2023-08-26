## STL Map Methods

1. **Insertion:**

   `mapName[key] = value` - Inserts a key-value pair into the map.

   i`nsert({key, value})` - Inserts a key-value pair into the map.

2. Access:

   `mapName[key]` - Accesses the value associated with the given key.

   `at(key)` - Accesses the value associated with the given key (throws an exception if the key is not present).

3. **Search:**

   `find(key)` - Searches for a key in the map and returns an iterator pointing to it.

   `count(key)` - Returns the number of occurrences of a key (0 or 1 in a map).

4. **Deletion:**

   `erase(key)` - Removes the element with the given key from the map.

   `clear()` - Removes all elements from the map.

5. **Size and Empty Check:**

   `size()` - Returns the number of elements in the map.

   `empty()` - Checks if the map is empty.

6. **Iterators:**

   `begin()` - Returns an iterator pointing to the first element.

   `end()` - Returns an iterator pointing just beyond the last element.
   You can use iterators to traverse through the map's elements.

7. **Range-based Loop:**

   You can use a range-based loop to iterate through the map's elements easily.

8. **Value Modification:**

   You can modify the value associated with a key directly using the key as an index.

9. **Bounds:**

   `lower_bound(key)` - Returns an iterator to the first element with a key not less than the given key.

   `upper_bound(key)` - Returns an iterator to the first element with a key greater than the given key.

10. **Key Comparison:**

    `key_comp()` - Returns a function that compares keys.

    `value_comp()` - Returns a function that compares values.

11. **Swapping:**

    `swap(map2)` - Swaps the contents of two maps.
