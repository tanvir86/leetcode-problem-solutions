# Explanation: https://leetcode.com/problems/interval-list-intersections/discuss/647482/Python-Two-Pointer-Approach-%2B-Thinking-Process-Diagrams
# Time O(N+M)
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        lengthA, lengthB = len(firstList), len(secondList)
        if  lengthA == 0 or lengthB == 0:
            return []
        
        i,j,result = 0,0,[]
        
        while i< lengthA and j<lengthB:
            aStart, aEnd = firstList[i][0],firstList[i][1]
            bStart, bEnd = secondList[j][0],secondList[j][1]
            
            if self.isCrissCrossExist(aStart, aEnd, bStart, bEnd):
                result.append(self.getCrossSection(aStart, aEnd, bStart, bEnd))
            
            if aEnd >= bEnd:
                j = j + 1
            else:
                i = i + 1
        
        return result
                    
    def isCrissCrossExist(self, aStart, aEnd, bStart, bEnd):
        return aStart <= bEnd and bStart <= aEnd
        
    def getCrossSection(self, aStart, aEnd, bStart, bEnd):
        return [ max(aStart,bStart), min(aEnd,bEnd) ]
            
