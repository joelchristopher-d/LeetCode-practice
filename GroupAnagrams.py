class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str not in d:
                d[sorted_str]=[strs[i]]
            else:
                d[sorted_str].append(strs[i])

        return (list(d.values()))
