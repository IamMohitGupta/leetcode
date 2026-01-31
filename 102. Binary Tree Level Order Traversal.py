# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        next_queue=[]
        level = []
        result = []

        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            queue = next_queue
            result.append(level)
            level = []
            next_queue = []
        
        return result


"""

Since, we have to go level by level, we store the root in a queue first.
If something in queue, then we store its value in level list and check if it has left and right children
If it has children, they are stored in next_queue list.

This process goes on until the current queue is fully iterated ( the queue containing root )

After that, queue becomes next_queue, level list is appended to result list, level list becomes empty and next_queue list becomes empty

"""


        
