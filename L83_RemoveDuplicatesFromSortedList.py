# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        nxt = cur.next
        while cur:
            while nxt and nxt.val == cur.val:
                nxt = nxt.next
            cur.next = nxt
            cur = cur.next

        return head
