class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]
        res=[]
        for i in set(words[0]):
            f = min([j.count(i) for j in words])
            res+=f*[i]
        return res
