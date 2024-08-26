class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        j=0
        while(j<len(intervals)-1):
            if intervals[j][1]>=intervals[j+1][0]:
                intervals[j]=[intervals[j][0],max(intervals[j][1],intervals[j+1][1])]
                intervals.remove(intervals[j+1])
            else:
                j+=1
        return intervals
