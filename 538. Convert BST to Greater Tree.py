# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def convertToGreaterTree(node: Optional[TreeNode], carry: int):
            if not node.left and not node.right:
                node.val += carry
                return node.val
            
            if node.right:
                carry = convertToGreaterTree(node.right,carry)
            
            node.val += carry
            
            if node.left:
                return convertToGreaterTree(node.left,node.val)

            return node.val
        
        if root:
            convertToGreaterTree(root,0)
        
        return root
        
