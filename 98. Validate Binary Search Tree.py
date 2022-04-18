# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(float("-inf"), float("inf"), root)]
        
        while stack:
            low, high, node = stack.pop()
            
            if node.val <= low or node.val >= high:
                return False
            
            if node.left:
                stack.append((low, node.val, node.left))
            if node.right:
                stack.append((node.val, high, node.right))
        
        return True
