class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToIndices = {}
        
        for i in range(len(nums)):
            if target - nums[i] in numToIndices:
                return [numToIndices[target - nums[i]],i]
            else:
                numToIndices[nums[i]] = i