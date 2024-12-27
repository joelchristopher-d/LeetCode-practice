class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        d={}
        for i in range(len(s)):
            orginal = s[i]
            replace = t[i]
            if s[i] not in d.keys():
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            else:
                mapped = d[s[i]]
                if mapped != t[i]:return False
        return True
