class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowstart=colstart=0
        rowend=len(matrix)
        colend=len(matrix[0])
        l=[]
        while(colstart<colend and rowstart<rowend):
            
            for i in range(colstart,colend):
                l.append(matrix[rowstart][i])
            rowstart+=1
            
            for i in range(rowstart,rowend):
                l.append(matrix[i][colend-1])
            colend-=1
        #     print(colend,colstart)
            if rowstart<rowend:
                for i in range(colend-1,colstart-1,-1):
                    l.append(matrix[rowend-1][i])
                rowend-=1
        #     print(rowend,colstart,";;")
            if colstart<colend:
                for i in range(rowend-1,rowstart-1,-1):
                    l.append(matrix[i][colstart])
                colstart+=1

        return(l)
                
