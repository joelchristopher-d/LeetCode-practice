class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            left = right = 0
            res = []
            n1 = len(nums1)
            n2 = len(nums2)
            while left<n1 and right<n2:
                if nums1[left]<=nums2[right]:
                    res.append(nums1[left])
                    left+=1
                else:
                    res.append(nums2[right])
                    right+=1
            while left<n1:
                res.append(nums1[left])
                left+=1
            while right<n2:
                res.append(nums2[right])
                right+=1
                    
            return res[len(res)//2] if len(res)%2!=0 else (res[len(res)//2]+res[(len(res)//2)-1])/2
                
