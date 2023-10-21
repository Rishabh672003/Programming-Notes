## Post Order Traversal ~ One Stack Iteration

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
    vector<int> postOrderOneStack(TreeNode *root){
        vector<int> ans;
        if (root == NULL) return ans;

        TreeNode *curr = root;
        TreeNode *temp = NULL;
        stack<TreeNode*> st;

        while(curr != NULL || !st.empty()){
            if (curr != NULL){
                st.push(curr);
                curr = curr->left;
            }
            else {
               temp = st.top()->right;
               if (temp == NULL) {
                temp = st.top();
                st.pop();
                ans.push_back(temp);
                while (!st.empty() && temp = st.top()->right){
                    temp = st.top();
                    st.pop();
                    ans.push_back(temp);
                }
               }
               else {
                curr = temp;
               }
            }
        }
    }
}
```
