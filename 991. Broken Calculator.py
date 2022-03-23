class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        
        res = 0
        
        while startValue != target:
            if startValue > target:
                res += startValue - target
                target = startValue
            elif target%2 == 0:
                res += 1
                target /= 2
            else:
                res += 1
                target += 1
        
        return res
