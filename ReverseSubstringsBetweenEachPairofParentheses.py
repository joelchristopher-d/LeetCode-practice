class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        for i in s:
            res=""
            if i == ")":
                while l and l[-1]!="(":
                    res+=l.pop()
                if l:
                    l.pop()
                for j in res:
                        l.append(j)
            else:
                l.append(i)
        return "".join(l)
        
