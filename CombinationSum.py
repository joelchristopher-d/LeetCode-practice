class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.rec(0, candidates, target, [])

    def rec(self,ind,arr,target,res):
        if target == 0:
            return [res]
        if target < 0 or ind == len(arr):
            return []
        include = self.rec(ind, arr, target - arr[ind], res + [arr[ind]])
        exclude = self.rec(ind + 1, arr, target, res)
        return include + exclude
