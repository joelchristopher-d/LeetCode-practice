class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        self.combo(0,candidates,target,[],ans)
        return ans
            
    
    def combo(self,ind,arr,target,ds,ans):
        if target==0:
    #         print(ds)
            ans.append(list(ds))
            return 
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:return
                
            ds.append(arr[i])
            self.combo(i+1,arr,target-arr[i],ds,ans)
            ds.pop()
            
