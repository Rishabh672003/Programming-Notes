# Linked Lists.

**Table of content :**

1. Why do we need Linked list ?
2. What is a Linked List ?
3. Structure of a Linked List.
4. Linked List Terminologies.
5. Depiction of a Linked list.

---

### Why do we need Linked list ?

Before konwing the defination, let's first know its need.

We need a data structure which is dynamic in nature, means it should not have a fixed size. The size could be changed during the run-time.

An **array** with size 10 will be allocated a fixed 10 sized in memory and hence it cannot span or contract during the run-time.

A **vector** can span double to its size if extra elements are meant to be added, but it ultimately wastes the remaining allocated memory.

Hence we need an optimal data structure which can grow or shrink on run time with no memory waste.

---

### What is a Linked List ?

A Linked list is a **Linear** but **Non-contiguous** Data Structure. Unlike arrays, hey are **Dynamic** in nature.

Linked list elements are randomly placed in the heap memory and hence **cannot be indexed**.

---

### Structure of a Linked List

**If Linked list elements are non-contiguous, then how do they form a linear collection?**

This is only possible because, in a Linked list, each member element is linked to the other with a reference to its memory location, means each linked list element stores its **data** and also a pointer to point the **memory address** of its next element.

**But there's no Primitive or Collective data type which can hold two things at a time!**

So we need to create a **Self Defined data type (a struct or a class)**, which can hold two values, the data (of any type) and a pointer to point a memory address at the same time.

Let's call this self defined data type a **NODE**. Now each node will have two halves, the first half will store data, the other half will store a pointer. A single node may look like a capsule with two halves:

```
  [ Data | Pointer* ]
```

---

### Linked List Terminologies

1. **Head node** : The first node of Linked list is the head node and acts as a starting point for most of the opertions.
2. **Tail node** : The last node of Linked list which points to the NULL Pointer 0x0.

---

### A depiction of a Linked list in heap memory :

![Linked-List-1](https://github.com/amitsuthar69/assets/blob/main/linked-lists/linked-list-1.png?raw=true)
