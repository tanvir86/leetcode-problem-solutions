


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if nums[left] == nums[right]:
                right = right -1
                continue
            
            if nums[left] < nums[right]:
                return nums[left]
            if left == mid or mid == right:
                return min(nums[left], nums[mid], nums[right])
            
            if nums[left] == nums[mid]:
                left = left +1
            elif nums[left]<nums[mid]: # left side sorted
                left = mid
            else:
                right = mid
                
        
        return nums[left]