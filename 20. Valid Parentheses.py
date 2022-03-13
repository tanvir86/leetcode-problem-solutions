from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = deque()
        openSet = {"(","{", "["}
        prthMap = {")":"(","}":"{", "]":"["}
        
        for i in range(len(s)):
            if s[i] in openSet:
                q.append(s[i])
            else:
                if len(q) == 0:
                    return False
                latest = q.pop()
                if prthMap[s[i]] != latest:
                    return False
        
        return True if len(q) == 0 else False
