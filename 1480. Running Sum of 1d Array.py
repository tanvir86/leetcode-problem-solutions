class Solution:
    # Runtime: 63 ms, Memory Usage: 14 MB
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        return nums
    # Runtime: 37 ms, Memory Usage: 14.1 MB
    def runningSum2(self, nums: List[int]) -> List[int]:
        s = 0
        return [s:=s+v for _,v in enumerate(nums)]
