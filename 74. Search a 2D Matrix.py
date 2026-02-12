class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def bin_search(l, target):
            left = 0
            right = len(l)-1
            while left <= right:
                mid = (left+right)//2
                if l[mid] == target:
                    return True
                elif l[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return False

        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                return bin_search(matrix[i], target)
        return False

"""

Approach:
Find the row where target can be found in, use binary search

"""
