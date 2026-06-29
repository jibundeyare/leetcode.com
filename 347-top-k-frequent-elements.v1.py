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
]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        top_k = {}

        for num in nums:
            # count each element
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            # keep track of the top k counts
            if len(top_k) < k:
                # fill the top k counts
                top_k[num] = count[num]
            elif num in top_k:
                # update the count if the number is already in the top k
                top_k[num] = count[num]
            else:
                # search if the current count can replace a smaller one in the top k
                for top_k_num, top_k_count in top_k.items():
                    if count[num] > top_k_count:
                        # found a count that can be replaced
                        # delete the smaller count, add the greater one and stop searching
                        del top_k[top_k_num]
                        top_k[num] = count[num]
                        break

        return [num for num, count in top_k.items()]

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

