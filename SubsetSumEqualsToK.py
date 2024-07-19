def sumsubset(ind,arr,target,dp):
    if target==0:return True
    if ind==0:return arr[0]==target
    if dp[ind][target]!=-1:return dp[ind][target]
    NotTake = sumsubset(ind-1,arr,target,dp)
    Take = False
    if(arr[ind]<=target):Take=sumsubset(ind-1,arr,target-arr[ind],dp)
    dp[ind][target]=Take or NotTake
    return dp[ind][target]


arr=[3,0,0,1,2,3]
ind=len(arr)
k=1
dp=[[-1 for i in range(k+1)] for i in range(ind)]
sumsubset(ind-1,arr,k,dp)
