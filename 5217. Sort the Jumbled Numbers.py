class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        self.hash = dict()
        self.mapping = mapping
        
        nums.sort(key=self.comparetor)
        
        return nums
    
    def comparetor(self,num):
        if num in self.hash:
            return self.hash[num]

        strNum = str(num)
        res = 0 
        for i in range(len(strNum)):
            res = 10 * res + self.mapping[int(strNum[i])]
        
        self.hash[num] = res
        return res
