# [Longest Consecutive Sequence - LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/description/)
# 128. Longest Consecutive Sequence
#
# Medium
#
# Topics
# Array
# Hash Table
# Union-Find
#
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
# Example 3:
#
# Input: nums = [1,0,1,2]
# Output: 3
#
# Constraints:
#
#     0 <= nums.length <= 10 ** 5
#     -10 ** 9 <= nums[i] <= 10 ** 9

# Algorithmic time complexity: O(?)
# Algorithmic space complexity: O(?)

# Inspiration:
# - [Disjoint-set data structure - Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

from mylib_leetcode import test_result
from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {
        'Input': dict(nums = [100,4,200,1,3,2]),
        'Output': 4,
    },
    {
        'Input': dict(nums = [0,3,7,2,5,8,4,6,0,1]),
        'Output': 9,
    },
    {
        'Input': dict(nums = [1,0,1,2]),
        'Output': 3,
    },
    {
        'Input': dict(nums = [7,-2,9,9,1,9,8,-4,6,-6,-6,4,1,3,6,3,5,-2,3,4,-6,1,5,-9,6,1,2,-2,1]),
        'Output': 9,
    },
]

class Solution:
    def __init__(self):
        self.items = {}
        self.ranks = {}
        self.sizes = {}

    def clear(self) -> None:
        self.items = {}
        self.ranks = {}
        self.sizes = {}

    def find(self, value: int) -> int:
        if self.items[value] == value:
            self.ranks[value] = 0

            return value
        else:
            root = self.find(self.items[value])
            self.items[value] = root
            self.ranks[value] = 1

            return root

    def union(self, a: int, b: int) -> bool:
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return False

        if self.ranks[a] > self.ranks[b]:
            a, b = b, a
            a_root, b_root = b_root, a_root

        self.items[a] = b_root
        self.ranks[a] = self.ranks[b_root] + 1

        return True

    def add(self, value: int, root: int=None) -> None:
        if root is not None:
            self.items[value] = root
            self.ranks[value] = self.ranks[root] + 1

            return

        self.items[value] = value
        self.ranks[value] = 0

    def longestConsecutive(self, nums: List[int]) -> int:
        self.clear()

        for num in nums:
            neighbor_left = num - 1
            neighbor_right = num + 1

            if num in self.items:
                # it's a duplicate, just ignore
                continue
            elif neighbor_left in self.items and neighbor_right in self.items:
                neighbor_left_root = self.find(neighbor_left)
                neighbor_right_root = self.find(neighbor_right)

                # merge neighbors
                self.union(neighbor_left_root, neighbor_right_root)

                # use the same root as neighbor_left
                root = self.find(neighbor_left)
                self.add(num, root)
            elif neighbor_left in self.items:
                # use the same root as neighbor_left
                root = self.find(neighbor_left)
                self.add(num, root)
            elif neighbor_right in self.items:
                # use the same root as neighbor_right
                root = self.find(neighbor_right)
                self.add(num, root)
            else:
                self.add(num)

        max_size = 0

        for item in self.items:
            root = self.find(item)

            if root in self.sizes:
                self.sizes[root] += 1
            else:
                self.sizes[root] = 1

            if self.sizes[root] > max_size:
                max_size = self.sizes[root]

        # @debug
        # print(f'{self.items=}')
        # print(f'{self.ranks=}')
        # print(f'{self.sizes=}')
        # print()

        return max_size

solution = Solution()

for data in datas:
    result = solution.longestConsecutive(**data['Input'])
    print(f'{data=}')
    print(f'{result=}')
    test_result(result, data['Output'])
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

