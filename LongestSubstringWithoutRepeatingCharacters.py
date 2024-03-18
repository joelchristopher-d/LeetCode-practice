class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        l2=[]
        while(l!=len(s)):
            li = []
            for i in range(l,len(s)):
                if s[i] not in li:
                    li.append(s[i])
                else:
                    break
            # print(li)
            l+=1
            l2.append(len(li))
        return max(l2) if len(l2)>0 else 0
        
