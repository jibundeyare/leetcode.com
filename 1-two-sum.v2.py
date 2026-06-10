# [Two Sum - LeetCode](https://leetcode.com/problems/two-sum/description/)
# 1. Two Sum
#
# Easy
#
# Topics
# Junior
# Array
# Hash Table
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
#
#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Algorithmic time complexity: O(?)
# Algorithmic space complexity: O(?)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {'nums': [2,7,11,15], 'target': 9},
    {'nums': [3,2,4], 'target': 6},
    {'nums': [3,3], 'target': 6},
]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        nums_sorted = sorted(nums)
        indexes_sorted = indexes = sorted(range(length), key=lambda i: nums[i])

        for pointer1 in range(length):
            lower_bound = pointer1 + 1
            upper_bound = length
            previous_position = -1

            while True:
                pointer2 = (upper_bound - lower_bound) // 2 + lower_bound

                if pointer2 == previous_position:
                    break

                my_sum = nums_sorted[pointer1] + nums_sorted[pointer2]

                if my_sum < target:
                    lower_bound = pointer2
                    previous_position = pointer2
                elif my_sum > target:
                    upper_bound = pointer2
                    previous_position = pointer2
                else:
                    # my_sum == target
                    return [indexes_sorted[pointer1], indexes_sorted[pointer2]]

        return []

solution = Solution()

for data in datas:
    result = solution.twoSum(**data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

