

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if mid == left or mid == right:
                return min(nums[left],nums[mid], nums[right])
            
            if nums[left] <= nums[right]:
                return nums[left]
            
            if nums[left] < nums[mid]: #left side sorted
                left = mid
            else:
                right = mid