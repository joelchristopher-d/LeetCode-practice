class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small=arrays[0][0]
        big=arrays[0][-1]
        maxd=0
        for i in range(1,len(arrays)):
            print(maxd,small,big)
            arr=arrays[i]
            maxd=max(maxd,arr[-1]-small,big-arr[0])
            small = min(small,arr[0])
            big = max(big,arr[-1])
        return maxd
                
        
        res=0
        for i in arrays:
            a=min(i)
            for j in arrays:
                if i!=j:
                    b=max(j)
                    res=max(res,abs(a-b))
        return res
        
