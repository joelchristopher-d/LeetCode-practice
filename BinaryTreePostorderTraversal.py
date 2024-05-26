# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.post(root, [])

    def post(self,root,l):
        if root is None:
            return 
        else:
            
            self.post(root.left,l)            
            self.post(root.right,l)
            l.append(root.val)
        return l
