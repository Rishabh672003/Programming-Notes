#include <algorithm>
#include <iostream>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
  int maxDepth(TreeNode *root) {
    if (root == NULL)
      return 0;
    int lh = maxDepth(root->left);
    int rh = maxDepth(root->right);
    return 1 + max(lh, rh); // formula
  }
  int minDepth(TreeNode *root) {
    if (root == NULL)
      return 0;

    // if the tree is a skew tree
    if (root->left == NULL && root->right != NULL) {
      return minDepth(root->right) + 1;
    } else if (root->left != NULL && root->right == NULL) {
      return minDepth(root->left) + 1;
    }

    // if a normal binary tree
    int lh = minDepth(root->left);
    int rh = minDepth(root->right);
    return 1 + min(lh, rh); // formula
  }
};

int main() {
  TreeNode *root = new TreeNode(3);
  root->left = new TreeNode(9);
  root->right = new TreeNode(20);
  root->right->left = new TreeNode(15);
  root->right->right = new TreeNode(7);

  Solution solution;

  int maxDepth = solution.maxDepth(root);
  int minDepth = solution.maxDepth(root);
  std::cout << "Max Depth of tree : " << maxDepth << std::endl;
  std::cout << "Min Depth of tree : " << minDepth << std::endl;

  return 0;
}
