
# O(n^2) Solution

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        nums.sort()
        for i in range (len(nums)):
            
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            target = 0 - nums[i]
            low, high = i+1,len(nums)-1
            
            while low < high:
                if nums[low] + nums[high] == target:
                    result.append([nums[i], nums[low], nums[high]])
                    
                    while low < high and nums[low] == nums[low+1]:
                        low = low + 1
                    while low < high and nums[high] == nums[high - 1]:
                        high = high - 1
                        
                    low, high = low +1, high-1
                    
                elif (nums[low] + nums[high]) < target:
                    low = low + 1
                else:
                    high = high -1
            
        return result