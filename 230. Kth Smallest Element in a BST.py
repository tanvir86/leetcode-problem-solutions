# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder Traversal (left, node, right) will give result in increasing order value (lowest to higest)
        # So we eill do a inorder traversal
        # But we do not need to complete the whole traversal as we only need the K'th value.
        # Wo we will count the traverse node till we reach K
        
        
        stack, node = [], root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            k -= 1
            if k==0:
                return node.val
            
            node = node.right
            
        return None # we will not reach here
