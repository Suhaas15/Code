# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=fast=head

        #find the middle node
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        #reverse the second half
        prev=None
        curr=slow.next
        slow.next=None

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        
        #merge both parts alternatively
        first=head
        second=prev

        while second:
            temp1,temp2=first.next,second.next
            first.next,second.next=second,temp1
            first,second=temp1,temp2