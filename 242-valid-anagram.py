# [Valid Anagram - LeetCode](https://leetcode.com/problems/valid-anagram/description/)
# 242. Valid Anagram
#
# Easy
#
# Topics
# Hash Table
# String
# Sorting
#
# Given two strings s and t, return true if t is an of s, and false otherwise.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
#
#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.

# Algorithmic time complexity: O(n)
# Algorithmic space complexity: O(1)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {'s': "anagram", 't': "nagaram"},
    {'s': "rat", 't': "car"},
]

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}

        for s_letter, t_letter in zip(s, t):
            if s_letter not in letters:
                letters[s_letter] = 1
            else:
                letters[s_letter] += 1

            if t_letter not in letters:
                letters[t_letter] = -1
            else:
                letters[t_letter] -= 1

        for count in letters.values():
            if count != 0:
                return False

        return True

solution = Solution()

for data in datas:
    result = solution.isAnagram(**data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

