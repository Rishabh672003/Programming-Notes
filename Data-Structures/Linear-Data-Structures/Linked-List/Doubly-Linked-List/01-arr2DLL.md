## Convert array to DLL

### Algorithm

1. Create a `head` node and assign it to arrays's first element.
2. Create a `prev` pointer to keep a track of just previous node. Initially, prev will point to head.
3. Start iteration form 1 to array size, during each iteration do these :
   - Create a `temp` node and assign it the `i`th value of array. The `temp`'s next will point to `null` where as the `temp`'s back will point to `prev` node.
   - For now the scenario is, the temp's back is connected to previous node, but still te prev node is disconnected to the temp node. So connect the prev node to temp node by pointing it to temp.
   - Now as we've a brand new node, bring the prev node ahead (to the temp node.)
4. Return the `head` node in the end.

---

### Implementation

```cpp
Node* arr2DLL(vector<int> &arr){
    Node* head = new Node(arr[0]);
    Node* prev = head;
    for (int i = 1; i < arr.size(); i++){
        Node* temp = new Node(arr[i], nullptr, prev);
        prev->next = temp;
        prev = temp;
    }
    return head;
}
```

---

### Depiction

![arr2DLL](https://github.com/amitsuthar69/assets/blob/main/linked-lists/arr2Dll.png?raw=true)
