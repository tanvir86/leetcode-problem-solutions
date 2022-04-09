class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right, minLength = 0,0, float("inf")
        currentSum = 0
        
        while right < len(nums):
            currentSum += nums[right]
            if currentSum >= target:
                minLength = min(minLength, right - left + 1)
                
                while currentSum - nums[left] >= target:
                    currentSum -= nums[left]
                    left += 1
            
                minLength = min(minLength, right - left + 1)
            right += 1
        
        return 0 if minLength == float("inf") else minLength
