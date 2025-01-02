class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        endstr=""
        l = {}
        for key in sorted(d, key=d.get,reverse=True):
            l[key] = d[key]
        for i in l:
            while l[i]>0:
                endstr += i
                l[i]-=1
        return endstr
