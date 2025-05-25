# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def find_len(head):
            count=0
            curr=head
            while curr:
                count+=1
                curr=curr.next
            return count

        if not head or not head.next or k==0:
            return head

        length = find_len(head)
        rotations = k%length

        if rotations==0:
            return head

        tail = length - rotations - 1
        current = head

        while tail!=0:
            current=current.next
            tail-=1
        temp=current.next
        current.next = None
        
        ans = temp

        while temp.next!=None:
            temp=temp.next
        
        temp.next=head

        return ans