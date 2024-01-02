# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = cur = ListNode(0); val = 0;
        while l1 or l2 or val:
            if l1: val += l1.val; l1 = l1.next;
            if l2: val += l2.val; l2 = l2.next
            cur.next = cur = ListNode(val%10); val //= 10
        return ret.next