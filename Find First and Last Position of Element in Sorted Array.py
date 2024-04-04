class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        while(high>=0):
            # print(low,high)
            if high<low:
                return[-1,-1] 
            if nums[low]==target and nums[high]==target:
                return[low,high]
            if nums[low]!=target:
                low+=1
            if nums[high]!=target:
                high-=1            
               
                      
        return [-1,-1]


        
#_______________


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
        
#         def binary_search(nums, target, is_searching_left):
#             left = 0
#             right = len(nums) - 1
#             idx = -1
            
#             while left <= right:
#                 mid = (left + right) // 2
                
#                 if nums[mid] > target:
#                     right = mid - 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     idx = mid
#                     if is_searching_left:
#                         right = mid - 1
#                     else:
#                         left = mid + 1
            
#             return idx
        
#         left = binary_search(nums, target, True)
#         right = binary_search(nums, target, False)
        
#         return [left, right]
            




