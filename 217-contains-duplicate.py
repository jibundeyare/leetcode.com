# [Contains Duplicate - LeetCode](https://leetcode.com/problems/contains-duplicate/description/)
# 217. Contains Duplicate
#
# Easy
#
# Topics
# Array
# Hash Table
# Sorting
#
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
#
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.
#
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Constraints:
#
#     1 <= nums.length <= 10 ** 5
#     -10 ** 9 <= nums[i] <= 10 ** 9

# Algorithmic time complexity: O(n)
# Algorithmic space complexity: O(n)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True

            nums_set.add(num)

        return False

solution = Solution()

for data in datas:
    result = solution.containsDuplicate(data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

