# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use a queue for iterative traversal
        queue = deque([(p, q)])
        
        while queue:
            node_p, node_q = queue.popleft()
            
            # Check if both nodes are None
            if not node_p and not node_q:
                continue
            
            # Check if one of the nodes is None or their values are not equal
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            
            # Enqueue the left and right children for both nodes
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))
        
        return True
