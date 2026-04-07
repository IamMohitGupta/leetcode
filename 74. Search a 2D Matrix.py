class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowstart = 0
        rowend = len(matrix)-1
        while rowstart<=rowend:
            mid = (rowstart+rowend)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0]>target:
                rowend = mid-1
            else:
                rowstart = mid+1
        
        row = rowend
        colstart = 0
        colend = len(matrix[0])-1
        while colstart<=colend:
            mid = (colstart+colend)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]>target:
                colend = mid-1
            else:
                colstart = mid+1
        return False
