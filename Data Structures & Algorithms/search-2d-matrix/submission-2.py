class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row = 0

        while top <= bottom:
            mid = top + (bottom - top) // 2

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
                row = mid
                break
            elif target > matrix[mid][len(matrix[0]) - 1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1

            # if target == matrix[mid][0]:
            #     return True
            # elif target > matrix[mid][0]:
            #     top = mid + 1
            # else: # target < matrix[mid][0]
            #     bottom = mid - 1

        # left = matrix[row][0]
        # right = matrix[row][len(matrix[0]) - 1]
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
























        # leftmid


        # top = 0
        # bottom = len(matrix) - 1

        # while top <= bottom:
        #     mid = top + (bottom - top) // 2
        #     if matrix[mid][0] == target:
        #         return True
        #     elif matrix[mid][0] > target:
        #         bottom = mid - 1
        #     else:
        #         top = mid + 1
        
        # row = top - 1

        # left = 0
        # right = len(matrix[0]) - 1
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False


