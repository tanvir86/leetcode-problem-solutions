
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left,right, i = None, head, 1
        
        while right.next is not None:
            i += 1
            right = right.next
            
            if i == n + 1:
                left = head
            elif i > n+ 1:
                left = left.next
        
        if left is None:
            return head.next
        else:
            left.next = left.next.next
            return head