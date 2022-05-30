from collections import deque 
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        
        n,m = len(heights), len(heights[0])
        
        cost = { (j,i):float("inf") for i in range(m) for j in range(n)}
        
        qeue = deque([(0,0)])
        cost[(0,0)] = 0
        
        while qeue:
            (r,c) = qeue.popleft()
            current_cost = cost[(r,c)]
            
            for [ra,ca] in dir:
                nr, nc = r + ra, c + ca
                
                if 0 <= nr < n and 0 <= nc < m:
                    new_cost = max(current_cost, abs(heights[r][c] - heights[nr][nc]))
                    if new_cost < cost[(nr,nc)]:
                        cost[(nr,nc)] = new_cost
                        qeue.append((nr,nc))
        
        
        return cost[(n-1,m-1)]
