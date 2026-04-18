# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxres = -10**9
        result = 0
        level = 0
        while queue:
            level+=1
            temp = 0
            size = len(queue)
            for i in range(size):
                x = queue.popleft()
                temp+=x.val
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            if temp > maxres:
                result = level
                maxres = temp
        return result
