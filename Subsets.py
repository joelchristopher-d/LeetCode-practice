class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            print(result,num)
            result += [curr + [num] for curr in result]
        return result




def backtrack(start, path,nums):
    print(start,result,path)
    result.append(path)
    for i in range(start, len(nums)):
        backtrack(i + 1, path + [nums[i]],nums)

result = []
backtrack(0, [],[1,2,3])
