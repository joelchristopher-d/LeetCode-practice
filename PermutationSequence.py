class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums=[]
        for i in range(1,n):
            fact*=i
            nums.append(i)
        nums.append(n)

        k-=1
        ans=""
        while(True):
            ans+= str(nums[k//fact])
            nums.remove(nums[k//fact])
            if len(nums)==0:
                break
            k%=fact
            fact//=len(nums)
        return ans
        
