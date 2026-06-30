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
    # Wrong Answer
    {
        'Input': dict(nums = [7,-2,9,9,1,9,8,-4,6,-6,-6,4,1,3,6,3,5,-2,3,4,-6,1,5,-9,6,1,2,-2,1]),
        'Output': 9,
    },
]

class Leaf():
    def __init__(self, value: int, root: Leaf=None):
        self._value = value
        self._size = 1

        if root:
            self._root = root
        else:
            self._root = self

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @size.deleter
    def size(self):
        del self._size

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root

    @root.deleter
    def root(self):
        del self._root

    def __str__(self):
        if self._root == self:
            root = 'self'
        else:
            root = self.root.value

        return f'{self._value=} {self._size=} root={root}'

class Solution:
    def merge(self, trees: dict, a: int, b: int) -> None:
        leaf_a = trees[a]
        leaf_b = trees[b]

        # merge a into b
        # but, if tree b is smaller than tree a, merge b into a
        if leaf_b.root.size < leaf_a.root.size:
            leaf_a, leaf_b = leaf_b, leaf_a

        # sum up a and b sizes into b
        leaf_b.root.size = leaf_a.root.size + leaf_b.root.size

        # (optional) reset a size to 1 because it's not a root anymore
        leaf_a.root.size = 1

        # replace occurences of a with b
        leaf_a.root.root = leaf_b.root
        leaf_a.root = leaf_b.root

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        trees = {}
        max_size = 1

        for num in nums:
            neighbor_left = num - 1
            neighbor_right = num + 1

            if num in trees:
                # it's a duplicate, just ignore
                continue
            elif neighbor_left in trees and neighbor_right in trees:
                # this value is a junction between two trees, we can merge them
                # merge neighbor_left tree and neighbor_right tree
                self.merge(trees, neighbor_left, neighbor_right)

                # use the same root as neighbor_left
                root = trees[neighbor_left].root
                trees[num] = Leaf(num, root)
                root.size += 1

                if root.size > max_size:
                    max_size = root.size
            elif neighbor_left in trees:
                # use the same root as neighbor_left
                root = trees[neighbor_left].root
                trees[num] = Leaf(num, root)
                root.size += 1

                if root.size > max_size:
                    max_size = root.size
            elif neighbor_right in trees:
                # use the same root as neighbor_right
                root = trees[neighbor_right].root
                trees[num] = Leaf(num, root)
                root.size += 1

                if root.size > max_size:
                    max_size = root.size
            else:
                trees[num] = Leaf(num)

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

