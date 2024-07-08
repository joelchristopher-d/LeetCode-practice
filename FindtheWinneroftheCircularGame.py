class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def newind(curr,steps,lent):
            new=curr+steps-1
            if new>=lent:
                new%=lent
            return new
        def ans(arr,curr):
            lent=len(arr)
            if lent==1:
                return arr[0]
            else:
                arr.pop(curr)
                return ans(arr,newind(curr,k,lent-1))
        return ans([i for i in range(1,n+1)],newind(0,k,n))
        
