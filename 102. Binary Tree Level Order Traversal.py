# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
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
    
    def levelOrderByBFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q, res = deque(),[]
        q.append(root)
        
        while q:
            size, listVal = len(q), []
            
            for i in range(size):
                node = q.popleft()
                
                listVal.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(listVal)
        return res
