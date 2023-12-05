## Convert an Array to a Linked List

### Algorithm :

1. Create a head node and assign the first array element to it.
2. Create an another node "mover" which then points to head.
3. Start iteration from 1 to array size.
4. For each iteration,

   - Create a temp node and assign its `data` to the `i`th element of current array.

   - Now we want our head node to point the next nodes, but we can't have multiple heads, so we'll take help of mover node.

     Make the mover node point the next node, cause the mover ultimately points head node.

   - Now shift the mover node to temp node.

5. Return head of the Linked List.

---

### Implementation :

```cpp
Node* convertArrToLL(vector<int> &arr){
    Node* head = new Node(arr[0]);
    Node* mover = head;
    for (int i = 1; i < arr.size(); i++){
        Node* temp = new Node(arr[i]);
        mover->next = temp;
        mover = temp;
    }
    return head;
}
```

---

### Depiction

![arr2LL](https://github.com/amitsuthar69/assets/blob/main/linked-lists/arr2LL.png?raw=true)
