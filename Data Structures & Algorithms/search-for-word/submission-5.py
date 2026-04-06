class Solution:
    def exist(self, board: List[List[str]], word: str):


        def backtrack(row, col, index):
            if index == len(word):
                return True
            if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) 
                or board[row][col] != word[index] 
                or board[row][col] == "#"
            ):
                return False

            temp = board[row][col]
            board[row][col] = "#"
            

            found = (
            backtrack(row + 1, col, index + 1) or
            backtrack(row - 1, col, index + 1) or
            backtrack(row, col + 1, index + 1) or
            backtrack(row, col - 1, index + 1)
            )
            board[row][col] = temp
            return found





        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False























# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
        

#         def backtrack(i, j, index):
#             if index == len(word):
#                 return True


#             if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "#" or board[i][j] != word[index]:
#                 return False

#             temp = board[i][j]
#             board[i][j] = "#"


#             found = (backtrack(i + 1, j, index + 1) or
#             backtrack(i, j + 1, index + 1) or
#             backtrack(i - 1, j, index + 1) or
#             backtrack(i, j - 1, index + 1))

#             # restore cell

#             board[i][j] = temp

#             return found



#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if backtrack(i, j, 0):
#                     return True
#         return False