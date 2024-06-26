# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0

        def DFS(node):
            if not node:
                return
            DFS(node.right)
            self.val+=node.val
            node.val=self.val
            DFS(node.left)
        DFS(root)
        return root
            
        
        
