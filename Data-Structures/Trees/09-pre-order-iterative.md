## Pre Order traversal ~ Iterative Approach

**Approach :**

1. Take the root and push it into the stack.
2. Start the Stack iteration, pop the top most element out and push it to the answer vector, then check if it has any left or right.
3. If left or right not NULL, first push right then left into the stack.
4. The stack iteration continues, pop the top most (left) element out and push it to the answer vector, then check if it has any left or right.
5. Continue the iteration untill the stak gets empty.

![pre-order-itr](https://github.com/Rishabh672003/Programming-Notes/assets/53911515/eb403e15-29ca-410a-913b-b9f79822c59a)

### Implementation :

```cpp
/* Defination for binary tree :
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right) {}
}
*/

class Solution {
public:
    vector<int> preorder(TreeNode *root) {

        vectro<int> ans;
        if (root == NULL) return ans;

        stack<TreeNode*> st;
        st.push(root);

        while(!st.empty()){

            root = st.top();
            st.pop();
            ans.push_back(root->val);

            if (root->right != NULL) {
                st.push(root->right);
            }
            if (root->left != NULL) {
                st.push(root->left);
            }
            
        }
        return ans;
    }
};
```
