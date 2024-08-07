class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        for i in nums1:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        # print(hashmap)
        nums3=[]
        for i in nums2:
            if i in hashmap and hashmap[i]>0:
                hashmap[i]-=1
                nums3.append(i)
        return nums3
                
