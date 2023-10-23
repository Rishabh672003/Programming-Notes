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
  int sumOfLeftLeaves(TreeNode *root) {
    if (root == NULL)
      return 0;

    int sum = 0;

    // checking if the root has a left leaf
    if (root->left != NULL && root->left->left == NULL &&
        root->left->right == NULL) {
      sum += root->left->val;
    }

    sum += sumOfLeftLeaves(root->left);
    sum += sumOfLeftLeaves(root->right);

    return sum;
  }
};

int main() {
  TreeNode *root = new TreeNode(3);
  root->left = new TreeNode(9);
  root->right = new TreeNode(20);
  root->right->left = new TreeNode(15);
  root->right->right = new TreeNode(7);

  Solution solution;

  int result = solution.sumOfLeftLeaves(root);
  std::cout << "Sum of left leaves: " << result << std::endl;

  return 0;
}
