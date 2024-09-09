def bubble(low,high,arr):
    if high == len(arr):return
    if low == len(arr)-1:
        high+=1
        return bubble(0,high,arr)
    if arr[low]>arr[low+1]:
        arr[low],arr[low+1] = arr[low+1],arr[low]
    bubble(low+1,high,arr)

arr = [10,1,9,8,7,6,5,4,3,2,0,1]
low = 0
high = 0
bubble(low,high,arr)
print(arr)
