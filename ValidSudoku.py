class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # a=0
        for i in range(len(board)):
            l=[]
            l1=[]
            for j in range(len(board[i])):
        #         print(board[j][i],end="")
                if board[i][j] in l:
                    return False
                    # print(board[i][j],False)
                    # break
                elif board[i][j]!=".":
                    l.append(board[i][j])
                    # a=1
                    # print(True)
                if board[j][i] in l1:
                    # print(False)
                    return False
                elif board[j][i]!=".":
                    l1.append(board[j][i])
            # if len(l1)==0 or len(l)==0:
            #     return False
            # elif a==0:
            #     return True
        #     print()

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                l=[]
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y]!=".":
                            if board[i+x][j+y] in l:
                                return(False)
                            else:
                                l.append(board[i+x][j+y])
        return True
                
