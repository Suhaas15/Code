# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node = None           #iterative

        # while head:
        #     temp=head.next
        #     head.next=node
        #     node=head
        #     head=temp
        
        # return node
        if head is None or head.next is None:
            return head
        
        new_head = self.reverseList(head.next)

        front=head.next
        front.next=head
        head.next=None

        return new_head

