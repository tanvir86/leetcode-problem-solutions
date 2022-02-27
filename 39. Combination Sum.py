
# recursion with backtracking
# ToDO: Time & Space complexity?

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.totalCombinations(0,candidates,target,[],[])
        
    def totalCombinations(self,ind,candidates,target,result,running):
        if target < 0 or ind >= len(candidates):
            return result
        if target==0:
            result.append(running[:])
            return result
        
        for i in range(ind,len(candidates)):
            if target < candidates[i]:
                return result
            running.append(candidates[i])
            self.totalCombinations(i,candidates,target-candidates[i],result,running)
            running.pop()
            
        return result