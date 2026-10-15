# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # lets put the base case here i.e when we reverse the base case in a Null 

        if not head:
            return None

        newhead = head

        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newhead