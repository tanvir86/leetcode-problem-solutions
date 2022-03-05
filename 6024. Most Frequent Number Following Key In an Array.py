class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        counter = dict()
        
        target, frequency = float("inf"), 0
        
        for i in range(0, len(nums)-1,1):
            if nums[i] == key:
                if nums[i+1] in counter:
                    counter[nums[i+1]] += 1
                else:
                    counter[nums[i+1]] = 1
                if counter[nums[i+1]] > frequency:
                    target = nums[i+1]
                    frequency = counter[nums[i+1]]
        
        return target
