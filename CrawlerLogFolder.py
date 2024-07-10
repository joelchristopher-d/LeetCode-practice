class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder=0
        for i in logs:
            if i == "./":
                pass
            elif i=="../":
                folder= (folder-1) if folder>0 else folder
            else:
                folder+=1
        return folder
        
