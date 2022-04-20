# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        def levelOrderTraverse(node: TreeNode, level: int) -> None:
            if len(res) < level:
                res.append([])
            
            res[level-1].append(node.val)
            
            if node.left:
                levelOrderTraverse(node.left, level+1)
            
            if node.right:
                levelOrderTraverse(node.right, level+1)
        
        levelOrderTraverse(root,1)
        
        return res
