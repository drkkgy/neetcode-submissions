# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:



        if not head or not head.next:

            return head

        reverse_head = self.reverseList(head.next)

        head.next.next = head
        # We do this to stop the internal cycle 
        # e.g 1 -> 2 -> 3 -> None
        #  3 -> 2 done by  head.next.next = head
        # but then 2 -> 3 still exisit right so it becomes 3 -> 2 -> 3 
        #  we break that with the line below head.next = None
        head.next = None

        return reverse_head


        
        