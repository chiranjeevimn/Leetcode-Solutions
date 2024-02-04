# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root = None
        stack = [(0, len(nums) - 1, None, None)]

        while stack:
            l, r, parent, is_left = stack.pop()
            if l > r:
                continue

            m = (l + r) // 2
            node = TreeNode(nums[m])

            if parent is None:
                root = node
            elif is_left:
                parent.left = node
            else:
                parent.right = node

            stack.append((l, m - 1, node, True))
            stack.append((m + 1, r, node, False))

        return root

        