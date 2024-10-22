def countpages(arr,p):
    student = 1
    pagescount = 0
    for i in range(len(arr)):
        if pagescount+arr[i]<=p:
            pagescount+=arr[i]
        else:
            student+=1
            pagescount = arr[i]
#     print(student)
    return student

def find(arr,m):
    low = max(arr)
    high = sum(arr)
    while(low<=high):
        mid = (low+high)//2
        print(mid)
        if countpages(arr,mid)<=m:
            high = mid-1
        else:
            low = mid+1
            
    return low

arr = [25, 46, 28, 49, 24]
m = 4
find(arr,4)
