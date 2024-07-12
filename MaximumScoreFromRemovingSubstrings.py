class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s=list(s)
        # x,y = 4,5
        t1 = "ab" if x>y else "ba"
        t2 = "ab" if x<y else "ba"
        l=[t1,t2]
        res=0
        for i in l:
            low = 0
            high = 1
            while(high<len(s)):
        #         print(s[low],s[high])
                if s[low]+s[high]==i:
                    # print(s,[low],[high])
                    res+=x if i=="ab" else y
                    # print(res)
                    s.pop(low)
                    s.pop(high-1)
                    low=0
                    high=1
                else:
                    low+=1
                    high+=1
        return res
                


# timeexceed solution
