class Solution:
    def numSteps(self, s: str) -> int:
        i = int(s,2)
        res=0
        while(i!=1):
            if i%2==0:
                i//=2
            else:
                i+=1
            res+=1
        return res        



# def binaryToDecimal(binary):
 
#     decimal, i = 0, 0
#     while(binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary//10
#         i += 1
#     print(decimal)
