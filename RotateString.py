class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal)!=len(s):return False
        low = 0
        while(low<len(goal)):
            if goal[0] == s[low]:
                if s[low:]+s[:low] == goal:return True
            low+=1
        return False
        # first = s[0]
        # index = 0
        # for i in range(len(goal)):
        #     if goal[i]==first:
        #         index = i
        #         print(index)
        #         break
        # start = len(goal)-index
        # if s[:start] == goal[index:] and s[start:]==goal[:index]:return True
        # else:return False
        return True if len(s)==len(goal) and goal in s+s else False
                
