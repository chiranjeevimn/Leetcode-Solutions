# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head

        while n:
            while n.next and n.val == n.next.val:
                n.next = n.next.next
            n = n.next

        return head