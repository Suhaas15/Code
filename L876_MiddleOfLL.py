# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        pos=0
        while current.next:
            current=current.next
            pos+=1
        
        mid = (pos+1)//2

        current=head
        pos=0
        while current:
            if pos==mid:
                return current
            current=current.next
            pos+=1
        
        