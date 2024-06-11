class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        l=[]
        l1=[]
        for i in arr2:
            d[i]=0
        # print(d)
        for i in arr1:
            if i in d:
                d[i]+=1
            else:
                l.append(i)
        # print(d,l)
        l.sort()
        for i in arr2:
            l1.extend([i]*d[i])
        l1.extend(l)
        return l1
                
