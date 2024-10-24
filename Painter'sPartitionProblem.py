def findLargestMinDistance(boards:list, k:int):
    low = max(boards)
    high = sum(boards)
    while(low<=high):
        mid = (low+high)//2
        if board(boards,mid)>k:
            low = mid+1
        else:
            high = mid-1
    return low
    # Write your code here
    # Return an integer
def board(arr,size):
    painter = 1
    boards = 0
    for i in arr:
        if boards + i <=size:
            boards+=i
        else:
            boards = i
            painter+=1
    return painter
