# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        l=[]
        def dfs(node, target):
            nonlocal l
            nonlocal res
            if not node:
                return []
            l.append(node.val)
            if not node.left and not node.right:
                if node.val == target:
                    res.append(l[:])
            
            dfs(node.left, target - node.val)
            dfs(node.right, target - node.val)

            l.pop()

        dfs(root, targetSum)
        return(res)
            
