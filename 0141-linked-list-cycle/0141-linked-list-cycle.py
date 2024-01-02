# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = head
        while first and first.next:
            head = head.next
            first = first.next.next
            if head is first:
                return True
        return False