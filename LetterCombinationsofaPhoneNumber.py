class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        if len(digits)==0:
            return res
        else:
            self.rec(digits,d,0,"",res)
            return(res)
    def rec(self,digits,d,index,text,res):
        if index>=len(digits):
            res.append(text)
            return
        string = d[digits[index]]
        for i in string:
            self.rec(digits,d,index+1,text+i,res)
