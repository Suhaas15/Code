"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dummy = Node(0,None,head,None)
        head.prev = dummy

        stack = []
        curr = head

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next=curr.child
                curr.child.prev=curr
                curr.child=None
            
            if not curr.next and stack:
                nxt=stack.pop()
                curr.next=nxt
                nxt.prev=curr

            curr=curr.next

        head=dummy.next
        head.prev=None

        return head
