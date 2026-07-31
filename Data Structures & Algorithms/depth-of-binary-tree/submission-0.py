# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = [float('-inf')]
        def dfs(root,path):
            if not root:
                return
            res[0] = max(res[0],path)
            dfs(root.left,path+1)
            dfs(root.right,path+1)
        dfs(root,1)
        return res[0]
            
        
        