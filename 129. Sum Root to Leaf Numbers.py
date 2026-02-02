# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, curr):
            if not node:
                return 0
            else:
                curr = curr*10 + node.val
            
            if not node.left and not node.right:
                return curr
            else:
                return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)

"""

Approach:
Remeber, when tree problem, recurrsion highly likely.
Traverse down the tree, if not null, multiply curr*10 and add node.val
Do the same forleft and right children

"""
