class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
          nums1[m+j] = nums2[j]
        # nums1.sort()
        for i in range(len(nums1)):
            for j in range(len(nums1)-1):
                if nums1[j]>nums1[j+1]:
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
        
