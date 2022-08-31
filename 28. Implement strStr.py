# Time complexity O(n), space complexity O(n)
from collections import Counter
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ndl,haystackLength = len(needle), len(haystack)
        
        if ndl == 0:
            return 0
        elif ndl > haystackLength:
            return -1
        
        
        start,end = [],[]
        
        
        for ind, ch in enumerate(haystack):
            if ch == needle[0]:
                start.append(ind)
            
            if ch == needle[-1]:
                end.append(ind)
        
        startInd, endInd = 0, 0
        
        if len(start) == 0 or len(end)==0 :
            return -1
        
        if ndl == 1 :
            return start[0]

        
        while startInd < len(start) and endInd < len(end):
            sInd = start[startInd]
            
            while endInd < len(end) and (end[endInd] <= sInd or end[endInd] - sInd + 1 < ndl):
                endInd += 1
            
            if endInd >= len(end):
                break
                
            eInd = end[endInd]
            
            if eInd - sInd + 1 == ndl:
                s, match = sInd, True
                for c in needle:
                    if c != haystack[s]:
                        match = False
                        break
                    s += 1
                if match:
                    return sInd
            startInd += 1
        
        return -1
        
        
        
        
