class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        l=[]
        for i in range(len(s)):
            l.append(int(s[i][-1]))
            s[i]=s[i][:len(s[i])-1]
        for i in range(len(l)):
            for j in range(len(l)-i-1):
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
                    s[j],s[j+1]=s[j+1],s[j]
        return(" ".join(s))
        
