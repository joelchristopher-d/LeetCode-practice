class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=score[0:]
        s.sort(reverse=True)
        print(score)
        d={}
        di = {0:"Gold Medal",1:"Silver Medal",2:"Bronze Medal"}
        for i in range(0,len(s)):
            j = score.index(s[i])
            if i>=3:
                score[j]=f"{i+1}"
            else:
                score[j]=di[i]

        return score
                        
