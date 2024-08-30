class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["." for i in range(n)] for j in range(n)]
        ans=[]
        self.placeQ(0,board,ans,n)
        return ans


    def isSafe(self,col,row,board,n):
            tempcol = col
            temprow = row
            
            while row>=0 and col>=0:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            
            col = tempcol
            row=temprow
            
            while col>=0:
                if board[row][col]=="Q":
                    return False
                col-=1
                
            col = tempcol
            row=temprow
            
            while row<n and col>=0:
                if board[row][col]=="Q":
                    return False
                col-=1
                row+=1
            return True


    def placeQ(self,col,board,ans,n):
        if col==n:
            temp=[]
            for i in board:
                temp.append("".join(i))
            ans.append(temp)
            return
        
        for row in range(n):
            if self.isSafe(col,row,board,n):
                board[row][col]="Q"
                self.placeQ(col+1,board,ans,n)
                board[row][col]="."
            
