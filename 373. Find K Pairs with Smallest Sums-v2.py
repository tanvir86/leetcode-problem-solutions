#Explanation: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
#Time Complexity O(klogk)

import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        minHeap = [(nums1[0]+nums2[0],0,0)]
        
        result, visited = [], {(0,0)}
        
        while len(minHeap) > 0 and len(result) < k:
            sumIJ ,i,j = heapq.heappop(minHeap)
            
            result.append([nums1[i],nums2[j]])
            
            if j + 1 < len(nums2) and (i,j+1) not in visited:
                heapq.heappush(minHeap,(nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))
            
            if i+1 < len(nums1) and (i+1,j) not in visited:
                heapq.heappush(minHeap,(nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))
        
        return result