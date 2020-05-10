# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        previousNode = None
        nextNode = None
        while current:
            nextNode = current.next
            current.next = previousNode
            previousNode = current
            current = nextNode
        return previousNode
