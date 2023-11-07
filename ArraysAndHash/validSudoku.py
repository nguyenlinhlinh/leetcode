# https://leetcode.com/problems/valid-sudoku/
# Idea create a set and add each filled cell in sudoku to set
# row:(r, nbr), col: (c, nbr), box: (boxRow, boxCol, nbr)
# Time complexity: O(9^2) = O(n^2)
# Space complexity: O(9^2) = O(n^2) if all cell are filled.
class Solution:
    def isValidSudoku(self, board):
        exist = set()
        for r in range(9):
            for c in range(9):
                nbr = board[r][c]
                if nbr != ".":
                    row = (r, nbr)
                    col = (nbr, c)
                    box = (r//3, c//3, nbr)
                    if row in exist or col in exist or box in exist:
                        return False
                    exist.add(row)
                    exist.add(col)
                    exist.add(box)
        return True