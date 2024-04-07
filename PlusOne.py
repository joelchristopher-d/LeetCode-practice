class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # a=0
        # for i in range(len(digits)):

        #     a+=(digits[i]*(10**(len(digits)-i-1)))
        # a+=1
        # l=[]
        # while(a!=0):    
        #     l.insert(0,a%10)
        #     a//=10

        # return l  

    
        a=1
        i=0
        l1=[]
        while(a!=0):    
            if i == len(digits):
                l1.insert(0,a%10)
                a//=10
            else:
                print(digits[i])
                a+=(digits[i]*(10**(len(digits)-i-1)))
                i+=1  
        return l1
