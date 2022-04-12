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
                    
                    
                        
                    
