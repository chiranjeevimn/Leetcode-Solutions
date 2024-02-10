#include <stdbool.h>
bool hasPathSum(struct TreeNode* root, int targetSum) {
    // Base case: If the current node is NULL, return false
    if (root == NULL) {
        return false;
    }

    // Check if the current node is a leaf and the target sum is reached
    if (root->left == NULL && root->right == NULL && root->val == targetSum) {
        return true;
    }

    // Recursively check the left and right subtrees
    bool leftResult = hasPathSum(root->left, targetSum - root->val);
    bool rightResult = hasPathSum(root->right, targetSum - root->val);

    // Return true if either the left or right subtree has a valid path
    return leftResult || rightResult;
}
