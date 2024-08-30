class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.Partition(0,s,[],res)
        return res

    def Partition(self,ind,s,path,res):
        if ind==len(s):
    #         print(res)
            res.append(list(path))
            return
        
        for i in range(ind,len(s)):
            if self.isPalindrome(ind,i,s):
                path.append(s[ind:i+1])
                self.Partition(i+1,s,path,res)
                path.pop()
            
            
    def isPalindrome(self,low,high,s):
        while(low<=high):
            if s[low]!=s[high]:
                return False
            low+=1
            high-=1
        return True
        
