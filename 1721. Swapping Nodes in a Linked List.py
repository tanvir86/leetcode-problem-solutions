# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        fast, slow, current = None, None, head
        
        for i in range(1,k):
            current = current.next
            
        fast = current
        slow = head
        
        while current.next is not None:
            slow = slow.next
            current = current.next
            
        temp = slow.val
        slow.val = fast.val
        fast.val = temp
        
        return head
