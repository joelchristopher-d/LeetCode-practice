from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    high = len(a)-2
    maxi = a[-1]
    l=[a[-1]]
    while(high>=0):
        if maxi<a[high]:
            l.append(a[high])
            maxi = a[high]
        high-=1
    return l
