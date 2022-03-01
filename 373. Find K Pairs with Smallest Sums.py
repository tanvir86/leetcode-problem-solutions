
# 
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        maxHeap = []
        
        for num1 in nums1:
            
            flag = False
            for i in range(len(nums2)):
                num2 = nums2[i]
                length = len(maxHeap) 
                if length < k:
                    maxHeap.append((-num1-num2,[num1,num2]))
                    if length == k-1:
                        heapq.heapify(maxHeap)
                else:
                    if num1+num2 < -1 * maxHeap[0][0]:
                        heapq.heappushpop(maxHeap, (-num1-num2,[num1,num2]))
                    else:
                        if i == 0:
                            flag = True
                        break
            if flag:
                break
        
        result = []
        
        for i in range(k):
            if len(maxHeap) == 0:
                break
            result.append(heapq.heappop(maxHeap)[1])
        
        return result
