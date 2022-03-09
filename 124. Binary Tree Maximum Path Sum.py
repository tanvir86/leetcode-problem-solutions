# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float("-inf")
        self.getMaxSum(root)
        
        return self.maxSum
    
    def getMaxSum(self,node):
        if node.left is None and node.right is None:
            self.maxSum = max(self.maxSum, node.val)
            return node.val
        
        leftMax = float("-inf") if node.left is None else self.getMaxSum(node.left)
        rightMax = float("-inf") if node.right is None else self.getMaxSum(node.right)
        
        self.maxSum = max(self.maxSum, node.val, leftMax + node.val, rightMax + node.val,leftMax + node.val + rightMax )
        
        return max(node.val, leftMax + node.val, rightMax + node.val)
