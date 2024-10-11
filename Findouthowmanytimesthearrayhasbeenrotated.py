arr = [3,4,5,6,7,1,2,2,2,2,3,3,3,3,3]
low = 0
high = len(arr)-1
mini = float("inf")
index = -1
while(low<=high):
    mid = (low+high)//2 
    if low != mid and mid!= high:
        if arr[low]==arr[mid] and arr[mid]==arr[high]:
            low+=1
            high-=1
            continue
    if arr[low]<=arr[high]:
        if arr[low]<mini:
            index = low
            mini = arr[low]
#             break
    if arr[low]<=arr[mid]:
        if arr[low]<mini:
            index = low
            mini = arr[low]
        low = mid+1
    else:
        if arr[mid]<mini:
            index = mid
            mini = arr[mid]
        high = mid-1
        
print(index,mini)
