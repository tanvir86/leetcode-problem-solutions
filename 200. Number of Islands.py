class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        
        setMap = [0] * (n*m)
        groupCount = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    ind = self.getIndexFromRC(n,row,col)
                    setMap[ind] = ind
                    groupCount += 1
                    if row > 0 and grid[row-1][col] == "1":
                        groupCount -= self.union(setMap,ind, self.getIndexFromRC(n,row-1,col))
                        
                    if col > 0 and grid[row][col-1] == "1":
                        groupCount -= self.union(setMap,ind,self.getIndexFromRC(n,row,col-1))

        return groupCount
    
    
    def find(self, setMap: List[int], ind: int) -> int:
        if setMap[ind] == ind:
            return ind
        
        group = self.find(setMap, setMap[ind])
        setMap[ind] = group
        return group
    def union(self, setMap: List[int], u: int, v: int) -> int:
        groupU = self.find(setMap, u)
        groupV = self.find(setMap, v)
        
        if groupU == groupV:
            return 0
        
        setMap[groupU] = groupV
        return 1
    
    def getIndexFromRC(self,n: int, row: int, col: int) -> int:
        return n*row + col
