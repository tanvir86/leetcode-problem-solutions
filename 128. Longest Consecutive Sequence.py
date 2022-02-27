
#Timecomplixity O(n)
#Space complexity O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashSet = set(nums)
            
        maxCount = 0
        
        for num in nums:
            if num-1 not in hashSet: #find whether this num can be start of a sequence
                count = 1
                current = num
                
                while current+1 in hashSet: #find the lenngth of sequence starting with num
                    count = count + 1
                    current = current + 1
                maxCount = max(maxCount,count)
        
        return maxCount
            