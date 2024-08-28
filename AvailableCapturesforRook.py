class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ri=-1
        ci=-1
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=="R":
                    ri=i
                    ci=j
        # print(ri,ci)
        ans=0
        dv = [[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(len(dv)):
            t1=dv[i][0]
            t2=dv[i][1]
            while 0<=ri+t1<8 and 0<=ci+t2<8:
                if board[ri+t1][ci+t2]=="p":
                    ans+=1
                    break
                elif board[ri+t1][ci+t2]=="B":
                    break
                t1+=dv[i][0]
                t2+=dv[i][1]
        return ans
                
