class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m,n = len(mat), len(mat[0])
        res, counted = [], set()
        
        
        for j in range(n):
            i = 0
            while i < m:
                while i in counted:
                    i+=1
                if i == m:
                    continue
                if mat[i][j] == 0 :
                    res.append(i)
                    counted.add(i)
                if len(counted) == k:
                    return res
                i+=1
        
        i = 0 
        while i < m:
            while i in counted:
                i+=1
            if i == m:
                continue
            res.append(i)
            counted.add(i)
            
            if len(counted) == k:
                return res
            i+=1
