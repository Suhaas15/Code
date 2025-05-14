# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # current=head              #Brute Force
        # node_set = set()

        # while current:
        #     if current in node_set:
        #         return True
        #     node_set.add(current)
        #     current=current.next
        
        # return False

        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
            
        return False