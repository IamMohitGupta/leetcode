# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node:
                return False
            
            curr_sum += node.val

            if not node.left and not node.right:
                return curr_sum == targetSum

            else:
                return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

        return dfs(root,0)
            

"""

Approach:
Traverse the tree using Depth-First Search while carrying the running sum of the current root-to-node path. 
At each node, update the path sum by adding the node’s value. When a leaf node is reached, check if the accumulated sum equals the target. 
If any root-to-leaf path satisfies this condition, return true; otherwise, continue searching other paths. 
Each path is evaluated independently without using shared/global state.

"""
