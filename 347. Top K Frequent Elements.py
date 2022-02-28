import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        elementFrq = {}
        
        for num in nums:
            if num in elementFrq:
                elementFrq[num] = elementFrq[num]+1
            else:
                elementFrq[num] = 1
        
        q = []
        
        for num in elementFrq:
            heapq.heappush(q,(-elementFrq[num],num))
        
        result = []
        
        for i in range(k):
            result.append(heapq.heappop(q)[1])
        
        return result