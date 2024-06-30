class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for i in range(len(nums)):
        #     print(i)
            if nums[i] in hashmap:
                # print(hashmap[nums[i]],nums[i],i)
                if abs(hashmap[nums[i]]-i)<=k:
                    return(True)
            hashmap[nums[i]]=i
        return False

                
