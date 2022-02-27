# Matrix transpose and then take mirror image or reverse
# O(n^2)

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        #transpose
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        
        #mirror or reverse
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
                