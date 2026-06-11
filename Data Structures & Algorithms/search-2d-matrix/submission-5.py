class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        curr_row = 0

        while top <= bottom:
            mid = top + (bottom - top) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                top = mid + 1
            else:
                curr_row = mid
                break
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[curr_row][mid] == target:
                return True
            elif matrix[curr_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False



