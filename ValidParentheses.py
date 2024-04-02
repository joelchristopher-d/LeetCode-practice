class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i in "({[":
                l.append(i)
            else:
                if not l or (i==")" and l[-1]!="(") or (i=="}" and l[-1]!="{") or (i=="]" and l[-1]!="["):
                    return False
                l.pop()
        return True if len(l)==0 else False
        
