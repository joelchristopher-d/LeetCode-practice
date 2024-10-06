arr = [3,5,8,15,19]
# arr = [1,2,2,3]
x = 4
low = 0
high = len(arr)-1
index = -1
while(low<=high):
    mid = (low+high)//2
    print(arr[mid],mid)
    if arr[mid] >= x:
        index = mid
        high = mid - 1
    else:
        low = mid + 1
print(index)
