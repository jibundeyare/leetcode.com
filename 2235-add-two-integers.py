# [Add Two Integers - LeetCode](https://leetcode.com/problems/add-two-integers/description/)
# 2235. Add Two Integers
#
# Easy
#
# Topics
# Math
#
# Given two integers num1 and num2, return the sum of the two integers.
#
# Example 1:
#
# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
#
# Example 2:
#
# Input: num1 = -10, num2 = 4
# Output: -6
# Explanation: num1 + num2 = -6, so -6 is returned.
#
# Constraints:
#
#     -100 <= num1, num2 <= 100

# Algorithmic time complexity: O(1)
# Algorithmic space complexity: O(1)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    [12, 5],
    [-10, 4],
]

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

solution = Solution()

for data in datas:
    result = solution.sum(*data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

