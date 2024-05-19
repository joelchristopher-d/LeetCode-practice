class Solution:
    def reverseVowels(self, s: str) -> str:
        word=list(s)
        low=0
        high=len(s)-1
        v = ["a","e","i","o","u","A","E","I","O","U"]
        while(low<high):
            if word[low] in v and word[high] in v:
                word[low],word[high]=word[high],word[low]
                low+=1
                high-=1
            if word[low] not in v:
                low+=1
            if word[high] not in v:
                high-=1
        return "".join(word)
        
