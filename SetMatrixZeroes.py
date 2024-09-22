class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    zero.append(i)
                    zero.append(j)
        for i in range(0,len(zero),2):
            self.makezero(zero[i],zero[i+1],matrix)
    def makezero(self,row,col,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i== row or j == col:
                    matrix[i][j]=0
        
