class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        def poss(arr,m,k,day):
            c=0
            nob=0
            for i in arr:
                if i<=day:
        #             print(day,c)
                    c+=1
                else:            
                    nob+=c//k
        #             print(nob)
                    c=0
            nob+=c//k
        #     print("-",nob)
            return nob>=m

        low=min(bloomDay)
        high=max(bloomDay)
        for i in range(low,high+1):
        #     print(i)
            if poss(bloomDay,m,k,i):
                return i
        return -1
                
