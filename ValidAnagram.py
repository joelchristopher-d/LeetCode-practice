class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = {}
        for i in range(ord("a"),ord("z")+1):
            count[chr(i)]=0
        for i in s:
            count[i]+=1
        for i in t:
            count[i]-=1
        for val in count.values():
            if val!=0:
                return False
        return True
            
