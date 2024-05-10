class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        stack={}
        low=0
        high=len(arr)-1
        while(low!=len(arr)-1):
            if low==high:
                low+=1
                high=len(arr)-1
                
            else:
                stack[arr[low]/arr[high]]=[arr[low],arr[high]]
                high-=1
        dicti=stack
        l=sorted(dicti)
        return stack[l[k-1]]



class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        vals = []
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                vals.append((arr[i]/arr[j], arr[i], arr[j]))
        vals.sort()
        return vals[k-1][1:]
