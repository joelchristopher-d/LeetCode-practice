arr = [3,5,8,15,19]
arr = [1,2,2,3]
arr = [3, 4, 4, 7, 8, 10]
x = 4
low = 0
high = len(arr)-1
l=[0,0]
while(low<=high):
    mid = (low+high)//2
    if arr[mid] >= x:
        l[0] = arr[mid]
        high = mid - 1
    else:
        low = mid + 1
low = 0
high = len(arr)-1      
while(low<=high):
    mid = (low+high)//2
    if arr[mid] <= x:
        l[1] = arr[mid]
        low = mid + 1
        
    else:
        high = mid - 1
print(l)
