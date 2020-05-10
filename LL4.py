# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        if l1 is None and l2 is None: return None 

        head = ListNode(0)
        cur = head

        while l1 and l2:

            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next

            else:
                cur.next = l1
                l1 = l1.next

            cur = cur.next

        cur.next = l1 or l2

        return head.next
