class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        t=0
        for i in num1:
            t=t*10+(ord(i)-48)
        t1=0
        for i in num2:
            t1=t1*10+(ord(i)-48)
        # print(num,num1)
        t*=t1
        s2=""
        # print(num)
        if t==0:return chr(48+t)
        while(t!=0):
            temp=t%10
            t//=10
            s2=chr(48+temp)+s2
        return s2 
