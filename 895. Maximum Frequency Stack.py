import heapq
class FreqStack(object):

    def __init__(self):
        self.index = 0
        self.freq = {}
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.freq:
            self.freq[val] = self.freq[val] - 1
        else:
            self.freq[val] = -1
        self.index -= 1
        heapq.heappush(self.stack,(self.freq[val],self.index,val))
        
        
    def pop(self):
        """
        :rtype: int
        """
        (f, ind, val) = heapq.heappop(self.stack)
        self.freq[val] += 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
