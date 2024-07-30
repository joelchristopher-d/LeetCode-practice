class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(numRows):
            ans=1
            l1=[]
            for j in range(i+1):
                l1.append(ans)
                ans*=(i-j)
                ans//=(j+1)
            l.append(l1)
        return l
