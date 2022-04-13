
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        grid = [[1 for j in range(n)] for i in range(n)]
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        i,j, prev = -1, n, 0
        
        while i < j:
            r,c = i+1,i
            # print(i,j,r,c)
            for dirs in directions:
                nr,nc = r+dirs[0], c + dirs[1]
                while ((dirs[0] == -1 and nr > i+1) or (dirs[0] != -1 and nr > i)) and nr < j and nc < j and nc > i:
                    # print(nr,nc)
                    grid[nr][nc] = prev + 1
                    prev += 1
                    nr,nc = nr+dirs[0], nc + dirs[1]
                r,c = nr-dirs[0], nc - dirs[1]
            i += 1
            j -= 1
            
        return grid
