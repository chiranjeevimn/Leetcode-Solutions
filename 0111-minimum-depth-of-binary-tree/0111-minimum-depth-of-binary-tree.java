/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        // If the tree is empty, the depth is 0
        if (root == null) {
            return 0;
        }

        // If the node is a leaf, return 1
        if (root.left == null && root.right == null) {
            return 1;
        }

        // If the node has only one child, return the minimum depth of that child + 1
        if (root.left == null) {
            return minDepth(root.right) + 1;
        }
        if (root.right == null) {
            return minDepth(root.left) + 1;
        }

        // If the node has two children, return the minimum depth of the subtree rooted at that node + 1
        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}
