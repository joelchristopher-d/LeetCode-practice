# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.POT(root,[])
    
    def POT(self,root,arr):
        if root:
            if root.left:self.POT(root.left,arr)
            if root.right:self.POT(root.right,arr)
            arr.append(root.val)
        return arr
        
