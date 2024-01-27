# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_recursive(node, result):
            if node:
                inorder_recursive(node.left, result)
                result.append(node.val)
                inorder_recursive(node.right, result)

        result = []
        inorder_recursive(root, result)
        return result