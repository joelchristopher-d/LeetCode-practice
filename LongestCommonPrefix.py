class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            for j in range(len(strs)-i-1):
                if len(strs[j])>len(strs[j+1]):
                    strs[j],strs[j+1]=strs[j+1],strs[j]
        comm = strs[0]
        for i in range(1,len(strs)):
            if comm == "": return comm
            else:
                comm = self.common(comm,strs[i])
        return comm
            
    def common(self,str1,str2):
        left = 0
        right = len(str1)
        while(str1[0:right]!=str2[0:right]):
            right-=1
            if right <=0:
                return ""
        # print(str1[0:right])
        return str1[0:right]
        
