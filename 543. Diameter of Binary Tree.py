# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)

                self.res = max(self.res, left+right)
            
            return max(left,right)+1

        dfs(root)
        return self.res

"""

Approach:
Apply DFS to iterate through root.left and find the lowest leaf node
Similarly for root.right

"""
