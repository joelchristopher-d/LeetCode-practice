class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def NCR(r,c):
            ans=1
            for i in range(c):
                ans*=(r-i)
                ans//=(i+1)
            return ans
        l=[]
        rowIndex+=1
        for i in range(1,rowIndex+1,1):
            l.append(NCR(rowIndex-1,i-1))
        return l
