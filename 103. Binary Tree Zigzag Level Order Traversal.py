# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        level = 0
        level_order = []
        res=[]
        while queue:
            for i in range(len(queue)):
                x = queue.pop(0)
                if level%2==0:
                    level_order.append(x.val)
                else:
                    level_order.insert(0, x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            level+=1
            res.append(level_order)
            level_order = []
        return res

  """

  Always append left and then right child, for odd level, just insert at 0

  """
