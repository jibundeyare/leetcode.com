# [Group Anagrams - LeetCode](https://leetcode.com/problems/group-anagrams/description/)
# 49. Group Anagrams
#
# Medium
#
# Topics
# Array
# Hash Table
# String
# Sorting
#
# Given an array of strings strs, group the together. You can return the answer in any order.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
#
#     There is no string in strs that can be rearranged to form "bat".
#     The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#     The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
#
#     1 <= strs.length <= 104
#     0 <= strs[i].length <= 100
#     strs[i] consists of lowercase English letters.

# Algorithmic time complexity: O(?)
# Algorithmic space complexity: O(?)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {'strs': ["eat","tea","tan","ate","nat","bat"]},
    {'strs': [""]},
    {'strs': ["a"]},
]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for anagram in strs:
            anagram_sorted = str(sorted(anagram))

            if anagram_sorted in anagrams:
                anagrams[anagram_sorted] += [anagram]
            else:
                anagrams[anagram_sorted] = [anagram]

        return [sorted(anagram) for _, anagram in anagrams.items()]

solution = Solution()

for data in datas:
    result = solution.groupAnagrams(**data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

