class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = cnt2 = 0
        el1 = el2 = 0
        for i in range(len(nums)):
            if cnt1 == 0 and el2 != nums[i]:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and el1 != nums[i]:
                cnt2 = 1
                el2 = nums[i]
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = cnt2 = 0
        for i in nums:
            if el1 == i:
                cnt1+=1
            elif el2 == i:
                cnt2+=1
        l=[]
        if cnt1 > len(nums)//3:
            l.append(el1)
        if cnt2 > len(nums)//3:
            l.append(el2)
        return l




        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res = []
        for i in d:
            if d[i]> len(nums)//3:
                res.append(i)
        return res
