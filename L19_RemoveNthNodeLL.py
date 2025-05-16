# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        # current=head              #2-pass solution
        # count=0

        # while current:
        #     count+=1
        #     current=current.next
        
        # final_count = (count-n)+1
        # current = head
        # prev = None
        # count = 0

        # if final_count== 1:
        #     return head.next

        # while current:
        #     count+=1
        #     if count==final_count:
        #         prev.next=current.next
        #     prev=current
        #     current=current.next

        # return head

        slow=fast=head
        
        for i in range(n):
            fast=fast.next

        if not fast:    #special case for if we need to remove head
            return head.next
            
        while fast.next:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next

        return head
        #check dummy node approach.