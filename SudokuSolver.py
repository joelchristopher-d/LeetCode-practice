class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
        """
        Do not return anything, modify board in-place instead.
        """
    def solve(self,board):
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==".":
                    for k in range(1,10):
                        if self.isvalid(i,j,board,str(k)):
                            board[i][j]=str(k)
                            
                            if self.solve(board)==True:
                                return True
                            else:
                                board[i][j]="."
                                
                    return False
        return True


    def isvalid(self,row,col,board,c):
        for i in range(9):
            if board[i][col]==c:return False
            if board[row][i]==c:return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3]==c:return False
        return True
