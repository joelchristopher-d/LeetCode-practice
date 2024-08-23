class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,10)]
        ans=[]
        self.combo(0,candidates,n,[],ans,k)
        return ans
        
    def combo(self,ind,arr,target,ds,ans,k):
        if target==0 and len(ds)==k:
    #         print(ds)
            ans.append(list(ds))
            return 
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:return
                
            ds.append(arr[i])
            self.combo(i+1,arr,target-arr[i],ds,ans,k)
            ds.pop()
        
