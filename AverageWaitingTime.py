class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t=0
        temp=0
        for i in customers:
            t = i[0] if t<=i[0] else t
            t+=i[1]
            temp+= (t-i[0])
        return (temp/len(customers))
