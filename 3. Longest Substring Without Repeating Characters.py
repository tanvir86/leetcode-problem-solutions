class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        
        maxLen, start = 1,0
        substring = dict()
        substring[s[0]] = 0
        
        for i in range(1, len(s)):
            if s[i] in substring and substring[s[i]] >= start:
                maxLen = max(maxLen, i - start)
                start = substring[s[i]] + 1
                
            substring[s[i]] = i
        maxLen = max(maxLen, len(s) - start)
        return maxLen
