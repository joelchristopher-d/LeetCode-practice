# brute:

array = [5,4,3,2,1]
array = [5,3,2,1,4]
array = [1,2,3,4,5]
pair = 0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            pair+=1
print(pair)


def Merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []
    cnt = 0
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            cnt+=(mid - left + 1)
            temp.append(arr[right])
            right+=1
        
    while left<=mid:
        temp.append(arr[left])
        left+=1
        
    while right<=high:
        temp.append(arr[right])
        right+=1
        
    for i in range(low,high+1):
        arr[i]=temp[i-low]
    return cnt

def mergesort(arr,low,high):
    cnt = 0
    if low>=high:return cnt
    
    mid = (low+high)//2
    cnt+=mergesort(arr,low,mid)
    cnt+=mergesort(arr,mid+1,high)
    cnt+=Merge(arr,low,mid,high)
    return cnt

    
arr = [5, 4, 3, 2, 1]
print(mergesort(arr,0,len(arr)-1))

