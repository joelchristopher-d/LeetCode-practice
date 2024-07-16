class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def counter(w):
            count=[0 for i in range(26)]
            for i in w:
        #         print(i)
                count[ord(i)-ord("a")]+=1
            return count

        counterlist=[0 for i in range(26)]
        temp=[]
        for i in words2:
            temp=counter(i)
            for j in range(len(temp)):
                counterlist[j]=max(temp[j],counterlist[j])
        # print(counterlist)
        l=[]
        for i in words1:
            temp=counter(i)
            for j in range(len(temp)):
                if temp[j]<counterlist[j]:
                    break
            if j == 25:
                l.append(i)
        return l
