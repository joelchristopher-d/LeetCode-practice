class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[i for i in range(n)] for j in range(n)]
        rowstart=colstart=0
        rowend=len(matrix)
        colend=len(matrix[0])
        # matrix=[]
        t=1
        while(colstart<colend and rowstart<rowend):
            
            for i in range(colstart,colend):
                matrix[rowstart][i]=t
                t+=1
            rowstart+=1
            
            for i in range(rowstart,rowend):
                matrix[i][colend-1]=t
                t+=1
            colend-=1
        #     print(colend,colstart)
            if rowstart<rowend:
                for i in range(colend-1,colstart-1,-1):
                    matrix[rowend-1][i]=t
                    t+=1
                rowend-=1
        #     print(rowend,colstart,";;")
            if colstart<colend:
                for i in range(rowend-1,rowstart-1,-1):
                    matrix[i][colstart]=t
                    t+=1        
                colstart+=1

        return(matrix)
                
