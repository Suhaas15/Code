from typing import List,Optional
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap=[]

        #add head of each list to heap
        for node in lists:
            if node:
                heapq.heappush(min_heap,(node.val,id(node),node))
        
        #dummy head for result
        dummy=ListNode(0)
        current=dummy

        #extract min and push its next
        while min_heap:
            val,_,node=heapq.heappop(min_heap)
            current.next=node
            current=current.next
            if node.next:
                heapq.heappush(min_heap,(node.next.val,id(node.next),node.next))
        
        return dummy.next