class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        end=[]
        for i in range(0,len(grid)-2):
            a=[]
            for j in range(0,len(grid)-2):
                l=[]
                for x in range(i,i+3):
                    for y in range(j,j+3):
        #                 print(grid[x][y],end=" ")
                        l.append(grid[x][y])
                a.append(max(l))
            end.append(a)

        return end

        
