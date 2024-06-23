class Solution:
    def add(self,l):
        maxi=0
        for i in l:
            for j in l:
                if abs(i-j)>maxi:
                    maxi=abs(i-j)
        return maxi

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        r=l=maxlen=0
        while(r<len(nums)):
            s=self.add(nums[l:r+1])
        #     print(s)
            if(s>limit):
                l+=1
                s=self.add(nums[l:r+1])
            if s<=limit:
        #         print(s,l,r)
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
         
