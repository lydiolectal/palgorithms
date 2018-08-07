# https://leetcode.com/problems/valid-sudoku/description/

import unittest

def isValidSudoku(board):
    rows, columns, squares = {}, {}, {}

    for i in range(9):
        rows[i] = set()
        columns[i] = set()
        squares[i] = set()

    for r in range(9):
        for c in range(9):
            curr = board[r][c]
            if curr == ".": continue
            row, col = r // 3, c // 3
            index = row * 3 + col
            if curr in rows[r] or curr in columns[c] or curr in squares[index]:
                return False
            rows[r].add(curr)
            columns[c].add(curr)
            squares[index].add(curr)

    return True

class TestSudoku(unittest.TestCase):

    def test_valid(self):
        board =  \
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(isValidSudoku(board))
    
    def test_invalid(self):
        board = \
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

        self.assertFalse(isValidSudoku(board))


