# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        track = {}

        curr = head

        while curr:

            if not track:
                track[curr] = curr.val
            else:
                if curr in track:
                    return True
                else:
                    track[curr] = curr.val
            
            curr = curr.next
        
        return False
        