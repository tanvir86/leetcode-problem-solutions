class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left,right = 0, len(s)-1
        
        if left == right:
            return True
        
        while left < right:
            if s[left] != s[right]:
                return self.checkPalindrome(s,left,right-1) or self.checkPalindrome(s,left+1,right)
            
            left += 1
            right -= 1
        return True
    
    def checkPalindrome(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
