
# Two Pointer Approch
# Explanation: https://www.code-recipe.com/post/container-with-most-water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left, right = 0, len(height)-1
        
        while left < right:
            minHeight = min(height[left], height[right])
            maxArea = max(maxArea, minHeight*(right-left))
            
            if minHeight == height[left]:
                left = left +1
            else:
                right = right-1
            
        
        return maxArea