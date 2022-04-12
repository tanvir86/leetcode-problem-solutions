class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        prev, running = [], [0 for i in range(len(board[0])) ]
        
        
        for i in range(len(board)):
            prev = running[::]
            
            for j in range(len(board[0])):
                running[j] = board[i][j]
                neighbors = 0
                
                if i != 0:
                    neighbors += prev[j]
                    if j>0:
                        neighbors += prev[j-1]
                    if j < len(board[0])-1:
                        neighbors += prev[j+1]
                
                if j > 0:
                    neighbors += running[j-1]
                if j < len(board[0])-1:
                    neighbors += board[i][j+1]
                
                
                if i < len(board)-1:
                    neighbors += board[i+1][j]
                    if j>0:
                        neighbors += board[i+1][j-1]
                    if j < len(board[0])-1:
                        neighbors +=  board[i+1][j+1]
                        
                
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 0
                elif neighbors == 3:
                    board[i][j] = 1
                    
                
        return board
                    
        
        
    def gameOfLifeInPlace(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
                      \ | /
        8 directions: - - -  
                      / | \
        Clockwise Rotations: (i-1,j-1), (i-1,j), (i-1,j+1),(i, J+1),(i+1,j+1), (i+1,j), (i+1,j-1),(i,j-1)
        
        if changed to 0; 1 -> 0; new val 2
        if changed to 1: 0 -> 1; new val -1
        """
        
        directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        m,n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                aliveNgbr = 0
                
                for r,c in directions:
                    nr,nc = i+r, j+c
                    if nr < 0 or nc < 0 or nr == m or nc == n:
                        continue
                    if board[nr][nc] > 0:
                        aliveNgbr += 1
                        
                
                if board[i][j] == 1:
                    if aliveNgbr < 2 or aliveNgbr > 3:
                        board[i][j] = 2
                elif aliveNgbr == 3:
                    board[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
                    
                
        return board
                        
                    
