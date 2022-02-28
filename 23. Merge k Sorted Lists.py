

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minHeap = []
        
        for linkedList in lists:
            if linkedList is not None:
                heapq.heappush(minHeap,(linkedList.val, linkedList))
        
        head,tail = None, None
        
        while len(minHeap) > 0:
            current = heapq.heappop(minHeap)[1]
            if current.next is not None:
                heapq.heappush(minHeap,(current.next.val, current.next))
                current.next = None
            
            if head is None:
                head = current
                tail = current
            else:
                tail.next = current
                tail = current
            
        return head