class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w=0
        w2=0
        s=""
        while(w<len(word1) or w2<len(word2)):
            if w<len(word1):
                s+=word1[w]
            if w2<len(word2):
                s+=word2[w2]
            w+=1
            w2+=1
        return s
