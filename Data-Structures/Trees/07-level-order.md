## Level Order Traversal [BFS] C++ Implementation

==> We'll need two data structures, A queue and a vector of vectors.

--> The Queue will hold the roots of tree.

--> vector will hold the levels

Step 1 : Push the root node of the tree to the queue.

Step 2: Check if there exists any left or right branch for that node.

Step 3: If there exists any left or right, push them to queue.

Step 4: Once performed Step 2 & 3 for a node, push that node into the vector.

Step 5 : Now iterate over the next queue elements and take them out, and repeat from Step 2. Check for their left and right, push their left / right to the queue and finally push the previous queue elements into the vector

---

Example :

```
        -->  1
           /   \
      --> 2     3
         / \   / \
    --> 4   5 6   7
```

Step 1 :

The queue becomes :

```
1
```

Step 2, Step 3 : Root node 1 has child nodes 2 and 3 as it's left and right, so push them to the queue.

The queue becomes :

```
1 2 3
```

Step 4 :

Push Root node 1 into the vector.

The vector becomes :

```
1
```

Step 5 :

Once we've performed these operations for Node 1, take child node 2 and 3 out of the queue and check if they have any left / right child nodes.

2 and 3 have 4 5 6 7 as their child nodes, push them to the queue.

The queue becomes :

```
1 2 3 4 5 6 7
```

Now Push the child nodes 2 & 3 into the vector.

The vector becomes :

```
1, 2 3
```

Once we've performed these operations for Child nodes 2 & 3, take child node 4, 5, 6 and 7 out of the queue and check if they have any left / right child nodes.

4 5 6 7 doesn't have any child nodes to push into the queue, so push them to the vector

The vector becomes :

```
1, 2 3, 4 5 6 7
```

**So the Level order traversal prints `1 2 3 4 5 6 7`**

---

![Visualization](https://github.com/Rishabh672003/Programming-Notes/assets/53911515/596d45d5-7510-4b23-946b-215811a55ab0)

---

### Approach :

- Declare a vector of vectors (and).
- if root == NULL, return and.
- declare a queue, push the root into it.
- while the queue is not empty,
- calculate it's size to traverse.
- declare a vector to store levels (levels).
- traverse the current nodes inside the queue.
- declare a node and initialize it to q.front().
- pop the node out of the queue and check if it's left and right exists.
- If exists, push them to queue
- push the node's value into the (level) vector.
- push the (level) vector to (and) vector.

---

### Implementation :

```cpp
/* Definition for binary tree :
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left),
right(right) {}
}
*/

class Solution {
  public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>and; // vector of vector
        if (root == NULL)
            return and;
        queue<TreeNode*> q; // queue
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left != NULL)
                    q.push(node->left);
                if (node->right != NULL)
                    q.push(node->right);
                level.push_back(node->value);
            }
            and.push_back(level);
        }
        return and;
    }
};
```
