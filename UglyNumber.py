class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:return False
        rem=0
        while(n>1):
            for i in ([2,3,5]):
                rem=n%i
        #         print(rem)
                if rem==0:
                    break
            if rem!=0:
                return False
            n//=i
        return True if rem==0 else False
                
