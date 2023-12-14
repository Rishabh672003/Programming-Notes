#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

/*
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges
between them.
*/

class Solution {
  public:
    int diameter = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return diameter;
    }
    int height(TreeNode* node) {
        if (!node)
            return 0;
        int lh = height(node->left);
        int rh = height(node->right);
        diameter = max(diameter, lh + rh);
        return 1 + max(lh, rh);
    }
};

int main() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution solution;

    int result = solution.diameterOfBinaryTree(root);

    cout << "Diameter of the binary tree: " << result << endl;

    delete root->left;
    delete root->right->left;
    delete root->right->right;
    delete root;

    return 0;
}
