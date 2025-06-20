"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # temp=head                       #brute force
        # mpp={}      

        # while temp is not None:
        #     new = Node(temp.val)
        #     mpp[temp]=new
        #     temp=temp.next
        
        # temp=head
        
        # while temp is not None:
        #     copy=mpp[temp]
        #     copy.next = mpp[temp.next] if temp.next else None
        #     copy.random = mpp[temp.random] if temp.random else None
        #     temp=temp.next
        
        # return mpp[head]

        temp=head
        while temp:
            nextNode = temp.next
            copy=Node(temp.val)
            temp.next=copy
            copy.next=nextNode
            temp=nextNode
        
        temp=head
        while temp:
            copy=temp.next
            if temp.random:
                copy.random=temp.random.next
            else:
                copy.random=None
            temp=temp.next.next
        
        temp=head
        dummy=Node(-1)
        res=dummy
        while temp:
            res.next=temp.next
            res=res.next

            temp.next=temp.next.next
            temp=temp.next
        
        return dummy.next
        