## Post Order Traversal ~ Two stack iteration

**Approach :**

1. Declare Two empty stacks. Push root of the tree into st1.

2. Start the st1 iteration, pop the top most element into st2.

3. Now if the top element of st2 has a left or right, push them into st1.

4. The iteration continues, pop the top most element into st2, check if it has left or right, push the left / right into st1.

5. The iteration stops when st1 gets empty.

6. When st1 gets empty, pop out all the element from st2 into answer vector.

### Implementation

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
    vector<int> postOrderTwoStack(TreeNode* root) {

        vector<int>and;
        if (root == NULL)
            return and;

        stack<TreeNode*> st1, st2;
        st1.push(root);

        while (!st1.empty()) {

            root = st1.top();
            st1.pop();
            st2.push(root);

            if (root->left != NULL) {
                st1.push(root->left);
            }
            if (root->right != NULL) {
                st1.push(root->right);
            }
        }

        while (!st2.empty()) {
            and.push_back(st2.top()->val);
            st2.pop();
        }

        return and;
    }
}
```
