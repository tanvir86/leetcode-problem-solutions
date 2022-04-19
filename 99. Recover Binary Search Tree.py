# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        prev, start, first = None, None, None
        
        stack, node = [], root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            if not prev:
                prev = node
            elif not first:
                
                if prev.val > node.val:
                    start = prev
                    first = node
            else:
                if prev.val > node.val:
                    start.val,node.val = node.val,start.val
                    return None
                
            prev = node
            node = node.right
        
        if start and first:
            start.val, first.val = first.val, start.val
        

        return None
