arr = [2, 4, 6, 8, 8,8,8 ,11, 13]    
x = 8
low = 0
high = len(arr)-1
first = -1
while(low<=high):
    mid = (low+high)//2
    if x == arr[mid]:
        first = mid
        high = mid - 1
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
last = -1
low = 0
high = len(arr)-1
while(low<=high):
    mid = (low+high)//2
    if x == arr[mid]:
        last = mid
        low = mid + 1
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
print(last-first+1)
