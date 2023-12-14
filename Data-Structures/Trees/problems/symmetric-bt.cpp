#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

/*
A symmetric binary tree is a binary tree where the left and right subtrees of
the root node are mirror images of each other.
*/

class Solution {
  public:
    bool isSymmetric(TreeNode* root) {
        return root == NULL || helper(root->left, root->right);
    }
    bool helper(TreeNode* left, TreeNode* right) {
        if (left == NULL || right == NULL)
            return left == right;
        if (left->val != right->val)
            return false;
        return helper(left->left, right->right) &&
               helper(left->right, right->left);
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(3);

    Solution solution;
    bool isSymmetric = solution.isSymmetric(root);

    if (isSymmetric) {
        cout << "The tree is symmetric." << endl;
    } else {
        cout << "The tree is not symmetric." << endl;
    }

    return 0;
}
