# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, curr):
            nonlocal total
            if not node:
                return
            curr = curr*2 + node.val
            if not node.left and not node.right:
                total+=curr
                return
            dfs(node.left, curr)
            dfs(node.right, curr)
        
        dfs(root, 0)
        return total
