class MergeSort:
    def __init__(self,cnt=0):
        self.cnt = cnt
    
    def merge(self,nums,low,mid,high):
        temp=[]
        left = low
        right = mid+1 
        while left<=mid and right<=high:
            if nums[left]<nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                self.cnt+=(mid-left+1)
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for i in range(low,high+1):
            nums[i]=temp[i-low]
        
        
    def mergesort(self,nums,low,high):
        if low==high:return
        mid=(low+high)//2
        self.mergesort(nums,low,mid)
        self.mergesort(nums,mid+1,high)
        self.merge(nums,low,mid,high)
        return self.cnt

ms = MergeSort()
nums = [5,3,2,4,1]
ms.mergesort(nums,0,len(nums)-1)
