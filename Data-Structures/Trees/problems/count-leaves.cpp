#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
  public:
    int countLeaves(TreeNode* root) {

        if (root == NULL)
            return 0;
        if (root->left == NULL && root->right == NULL)
            return 1;

        int leftLeaves = countLeaves(root->left);
        int rightLeaves = countLeaves(root->right);

        return leftLeaves + rightLeaves;
    }
};

int main() {
    // Create a sample binary tree
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution solution;

    int result = solution.countLeaves(root);
    cout << "Sum of left leaves: " << result << std::endl;

    return 0;
}
