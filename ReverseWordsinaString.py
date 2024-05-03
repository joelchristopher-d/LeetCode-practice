class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        # print(s)
        j=""
        for i in s:
            if i!="":
                j=" "+i+j
        j.strip()
        return j.strip()
            
