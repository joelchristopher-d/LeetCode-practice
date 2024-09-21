from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.
    a.sort()
    temp = a[0]
    count = 1
    maxi = 0
    for i in range(1,len(a)):
        if temp == a[i]:
            continue
        if temp+1 == a[i]:
    #         print(arr[i])
            count+=1    
        else:
            count=1
        temp=a[i]
        maxi=max(count,maxi)
    return maxi
