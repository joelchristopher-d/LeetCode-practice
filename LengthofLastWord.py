class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        j=s.strip(" ")
        l=j.split(" ")
        return len(l[-1])
