# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def diameterOfBinaryTreeHelper(node):
            if not node:
                return 0

            # Calculate the diameter at the current node
            current_diameter = height(node.left) + height(node.right)

            # Recursively calculate the diameter in the left and right subtrees
            left_diameter = diameterOfBinaryTreeHelper(node.left)
            right_diameter = diameterOfBinaryTreeHelper(node.right)

            # Return the maximum of the three values
            return max(current_diameter, max(left_diameter, right_diameter))

        # Call the helper function with the root of the binary tree
        return diameterOfBinaryTreeHelper(root)