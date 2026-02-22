# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(node, target):
            if not node:
                return TreeNode(target)
            if target > node.val:
                node.right = dfs(node.right, target)
            else:
                node.left = dfs(node.left, target)
            return node

        return dfs(root, val)
