class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        s2=""
        for i in s:
            if (ord(i.lower())>47 and ord(i.lower())<58) or (ord(i.lower())>96 and ord(i.lower())<123):
                s1+=i.lower()
                s2=i.lower()+s2

        return s1==s2
                
