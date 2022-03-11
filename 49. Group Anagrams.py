class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        result, length = [], 0
        bucketMap = dict()
        
        for i in range(len(strs)):
            key = self.getStringOfCounter(strs[i])

            if key in bucketMap:
                result[bucketMap[key]].append(strs[i])
            else:
                result.append([strs[i]])
                bucketMap[key] = length
                length += 1
        return result
                
        
    
    def getStringOfCounter(self, string):
        counter = [0 for i in range(26)]
        
        startAsci = ord('a')
        
        for i in range(len(string)):
            counter[ord(string[i]) - startAsci] += 1
            
        return str(counter)
