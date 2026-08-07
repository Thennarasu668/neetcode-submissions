# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,pathSum):
            if not node:
                return False
            if not node.left and not node.right:
                if pathSum + node.val == targetSum:
                    return True
            left = dfs(node.left,pathSum + node.val) 
            right = dfs(node.right,pathSum + node.val)
            return left or right
        return dfs(root,0)

            