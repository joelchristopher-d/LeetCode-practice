class Solution:
    def decimal_to_binary(self,num):
        if num >= 1:
            return self.decimal_to_binary(num // 2) + str(num % 2)
        return ''

    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            t=self.decimal_to_binary(i)
            a=0
            for j in t:
                if j=="1":
                    a+=1
            l.append(a)
        return l
            
