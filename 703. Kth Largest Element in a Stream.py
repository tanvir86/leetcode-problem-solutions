import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, l = k, len(nums)
        nums.sort()

        self.largestKNums = nums if l < k else [nums[i] for i in range(l-k, l)]
        # heapq.heapify(self.largestKNums)
          

    def add(self, val: int) -> int:
        if len(self.largestKNums) < self.k:
            heapq.heappush(self.largestKNums,val)
        elif val == self.largestKNums[0]:
            return val
        elif val > self.largestKNums[0] :
            heapq.heappushpop(self.largestKNums,val)
            
        return self.largestKNums[0]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
