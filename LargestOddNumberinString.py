class Solution(object):
    def largestOddNumber(self, num):
        n=len(num)
        for i in range(n):
            if(int(num[n-i-1])%2!=0):
                return str(num[0:n-i])
        return ""
        
        
