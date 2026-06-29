# [Valid Sudoku - LeetCode](https://leetcode.com/problems/valid-sudoku/description/)
# 36. Valid Sudoku
#
# Medium
#
# Topics
# Array
# Hash Table
# Matrix
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
#
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.
#
# Example 1:
#
# ![36-Sudoku-by-L2G-20050714.svg.png](36-Sudoku-by-L2G-20050714.svg.png)
#
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
# Example 2:
#
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
# Constraints:
#
#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit 1-9 or '.'.

# Algorithmic time complexity: O(?)
# Algorithmic space complexity: O(?)

# Inspiration:
# - None
# - ...

from mylib_leetcode import test_result
from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {
        'Input': dict(board =
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        ),
        'Output': True,
    },
    {
        'Input': dict(board = 
            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        ),
        'Output': False,
    },
]

class Solution:
    width = 9
    height = 9

    def getSubmatrixInex(self, x: int, y: int) -> int:
        x_mod = x % 3
        y_mod = y % 3

        return (y // 3 ) * 3 + x // 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        verify_columns = [set() for _ in range(self.width)]
        verify_rows = [set() for _ in range(self.width)]
        verify_submatrix = [set() for _ in range(self.width)]

        for y in range(self.height):
            for x in range(self.width):
                # skip non value symbol '.'
                if board[y][x] == '.':
                    continue

                # check if value is in column
                if board[y][x] in verify_columns[x]:
                    print('foo')
                    return False
                else:
                    verify_columns[x].add(board[y][x])

                # check if value is in row
                if board[y][x] in verify_rows[y]:
                    print('bar')
                    return False
                else:
                    verify_rows[y].add(board[y][x])

                # check if value is in submatrix
                submatrix_index = self.getSubmatrixInex(x, y)

                if board[y][x] in verify_submatrix[submatrix_index]:
                    return False
                else:
                    verify_submatrix[submatrix_index].add(board[y][x])

        return True

solution = Solution()

for data in datas:
    result = solution.isValidSudoku(**data['Input'])
    print(f'{data=}')
    print(f'{result=}')
    test_result(result, data['Output'])
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

