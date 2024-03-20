class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=sorted(nums1+nums2)
        l1=0
        return float(f"{l[(len(l)-0)//2]:.5f}" if len(l)%2!=0 else f"{(l[(len(l)-0)//2]+l[((len(l)-0)//2)-1])/2:.5f}")
        
