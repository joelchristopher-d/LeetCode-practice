# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def iot(r):
            if r is None:
                return
            else:
                iot(r.left)
                l.append(r.val)
                iot(r.right)
            return l
        
        return iot(root)
        
