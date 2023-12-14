#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
  public:
    // a function to check if tree is balanced or not on basis of it's height.
    bool isBalanced(TreeNode* root) { return dfsHeight(root) != -1; }

    /* a function to calculate height of tree, if this function returns -1,
      the tree is not balanced. The tree will always be balanced if this
      function returns some non-negative height */

    int dfsHeight(TreeNode* root) {
        if (root == NULL)
            return 0;

        int lh = dfsHeight(root->left);
        if (lh == -1)
            return -1;

        int rh = dfsHeight(root->right);
        if (rh == -1)
            return -1;

        // for a balanced BT, height(left sub-tree) - height(right sub-tree) <=
        // 1
        if (abs(lh - rh) > 1)
            return -1;

        return max(lh, rh) + 1;
    }
};

int main() {
    Solution solution;

    TreeNode* balancedTree = new TreeNode(1);
    balancedTree->left = new TreeNode(2);
    balancedTree->right = new TreeNode(3);
    balancedTree->left->left = new TreeNode(4);
    balancedTree->left->right = new TreeNode(5);
    balancedTree->right->left = new TreeNode(6);
    balancedTree->right->right = new TreeNode(7);

    bool isBalancedResult = solution.isBalanced(balancedTree);
    cout << "tree balanced? " << (isBalancedResult ? "Yes" : "No") << endl;
    return 0;
}
