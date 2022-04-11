class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) 
        ans = [[ 0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                newRow = ((n*i + j + k)//n) % m
                newCol = (n*i + j + k)%n
                
                ans[newRow][newCol] = grid[i][j]
        return ans
        
