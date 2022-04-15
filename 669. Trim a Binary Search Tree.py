# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        # first find the new root
        # For this we will find the first element whose value is inside the given bound
        
        newRoot = root
        
        while newRoot is not None and (newRoot.val < low or newRoot.val > high):
            if newRoot.val < low:
                newRoot = newRoot.right
            elif newRoot.val > high:
                newRoot = newRoot.left
        
        if newRoot is None:
            return None
        
        # Now we need to trim the left and right sub tree of this new root
        
        # Trimming Left subtree: 
        #       If we keep going to left we will find the values which is lowest than our lower bound value
        #       and if a node value is inside our bound then right tree of that node also inside our bound
        
        
        if newRoot.val == low:
            newRoot.left = None
        
        prev = newRoot
        current = newRoot.left
        
        while current is not None:
            if current.val == low:
                current.left = None
                break
            elif current.val > low:
                prev = current
                current = current.left
            else:
                current = current.right
                prev.left = current

        
        # Trimming right subtree: 
        #       If we keep going to right we will find the values which is highest than our high bound value
        #       and if a node value is inside our bound then left tree of that node also inside our bound
        
        if newRoot.val == high:
            newRoot.right = None
        
        prev = newRoot
        current = newRoot.right
        
        while current is not None:
            
            if current.val == high:
                current.right = None
                break
            elif current.val < high:
                prev = current
                current = current.right
            else:
                current = current.left
                prev.right = current
        
        return newRoot
    
    
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def prune(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            if node.val < low: # all left node deleted. Consider only right node
                return prune(node.right)
            elif node.val > high: # all right node delete. Consider only left node
                return prune(node.left)
            
            node.left = prune(node.left)
            node.right = prune(node.right)
            
            return node
        
        return prune(root)
