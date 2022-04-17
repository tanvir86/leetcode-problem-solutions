# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        newRoot,prev, node = None, None, root
        stack = []
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            if stack:
                node = stack.pop()
                if prev:
                    prev.right = node
                    prev = node
                else:
                    newRoot, prev = node, node
                
                node.left = None
                
                temp = node.right
                node.right = None
                node = temp
        
        return newRoot
