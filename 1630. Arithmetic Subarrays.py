import heapq
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        
        for i in range(len(l)):
            numSet = nums[l[i]:r[i]+1]
            heapq.heapify(numSet)
            
            first = heapq.heappop(numSet)
            second = heapq.heappop(numSet)
            
            diff = second - first
            isArithmatic = True
            
            while len(numSet) > 0:
                third = heapq.heappop(numSet)
                if diff != (third - second):
                    isArithmatic = False
                    break
                second  = third
            res.append(isArithmatic)
        return res
            
