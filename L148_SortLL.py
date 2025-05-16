# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow=fast=head
        prev = None

        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        prev.next=None
        left=head
        right=slow

        #recursively sort both halves
        left=self.sortList(left)
        right=self.sortList(right)

        #merge
        return self.merge(left,right)

    def merge(self,left : ListNode,right : ListNode) -> ListNode:
        dummy=ListNode(0)
        current=dummy

        while left and right:
            if left.val < right.val:
                current.next=left
                left=left.next
            else:
                current.next=right
                right=right.next
            current=current.next
            
        current.next=left if left else right

        return dummy.next 

        
        