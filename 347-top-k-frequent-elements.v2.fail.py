# [Top K Frequent Elements - LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)
# 347. Top K Frequent Elements
#
# Medium
#
# Topics
# Array
# Hash Table
# Divide and Conquer
# Sorting
# Heap (Priority Queue)
# Bucket Sort
# Counting
# Quickselect
#
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
# Example 3:
#
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]
#
# Constraints:
#
#     1 <= nums.length <= 10 ** 5
#     -10 ** 4 <= nums[i] <= 10 ** 4
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# The idea was to keep the list of the five highest count and at the
# end, filter the counts dictionary using the lowest of the five highest
# count as a threshold.
# But it didn't work because we need to keep track of the number
# associated with the count to verify if we need to add a new value to
# list or update an obsolete value.
# It turns out that keeping track of the number and the count is exactly
# the previous algorithm, so fixing this is no use.
#
# Algorithmic time complexity: O(n)
# Algorithmic space complexity: O(n)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {'nums': [1,1,1,2,2,3], 'k': 2},
    {'nums': [1], 'k': 1},
    {'nums': [1,2,1,2,1,2,3,1,3,2], 'k': 2},
    # expected [1,3]
    {'nums': [5,3,1,1,1,3,73,1], 'k': 2},
]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        top_k_count = []

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if not top_k_count:
                top_k_count.append(counts[num])
            if len(top_k_count) < k and counts[num] > top_k_count[0]:
                top_k_count.append(counts[num])
                top_k_count.sort()
            elif counts[num] > top_k_count[0]:
                top_k_count[0] = counts[num]
                top_k_count.sort()

            print(f'{counts=}')
            print(f'{top_k_count=}')

        return [num for num, count in counts.items() if count >= top_k_count[0]]

solution = Solution()

for data in datas:
    result = solution.topKFrequent(**data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

