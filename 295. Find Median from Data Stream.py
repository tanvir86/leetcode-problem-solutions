

import heapq
class MedianFinder(object):

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxHeap) == 0 and len(self.minHeap) == 0:
            heapq.heappush(self.maxHeap,-num)
        elif len(self.maxHeap) > 0:
                if -self.maxHeap[0] < num:
                    heapq.heappush(self.minHeap,num)
                else:
                    heapq.heappush(self.maxHeap,-num)
        else:
            if self.minHeap[0] > num:
                heapq.heappush(self.maxHeap,-num)
            else:
                heapq.heappush(self.minHeap,num)
        self.keepBalance()
        
    def keepBalance(self):
        diff = len(self.maxHeap)-len(self.minHeap)
        if abs(diff)>1 :
            if diff > 0:
                heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap)) 
            else:
                heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap)) 
            

    def findMedian(self):
        """
        :rtype: float
        """
        diff = len(self.maxHeap)-len(self.minHeap)
        if diff == 0 :
            return (self.minHeap[0]-self.maxHeap[0])/2.00
        elif diff > 0 :
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()