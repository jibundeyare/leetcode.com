# [Minimum Cost of Buying Candies With Discount - LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/?envType=daily-question&envId=2026-06-01)
# 2144. Minimum Cost of Buying Candies With Discount
#
# Easy
#
# Topics
# Mid Level
# Array
# Greedy
# Sorting
# Biweekly Contest 70
#
# A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.
#
# The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.
#
#     For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
#
# Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.
#
# Example 1:
#
# Input: cost = [1,2,3]
# Output: 5
# Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
# The total cost of buying all candies is 2 + 3 = 5. This is the only way we can buy the candies.
# Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
# The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.
#
# Example 2:
#
# Input: cost = [6,5,7,9,2,2]
# Output: 23
# Explanation: The way in which we can get the minimum cost is described below:
# - Buy candies with costs 9 and 7
# - Take the candy with cost 6 for free
# - We buy candies with costs 5 and 2
# - Take the last remaining candy with cost 2 for free
# Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.
#
# Example 3:
#
# Input: cost = [5,5]
# Output: 10
# Explanation: Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free.
# Hence, the minimum cost to buy all candies is 5 + 5 = 10.
#
# Constraints:
#
#     1 <= cost.length <= 100
#     1 <= cost[i] <= 100

# Algorithmic time complexity: O(n * log(n))
# Algorithmic space complexity: O(n)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/comments/3282303/
# Some Test cases
datas = [
    [1, 2, 3],
    [6, 5, 7, 9, 2, 2],
    [5, 5],
    [1, 2, 3, 7],
    [6, 35, 7, 9, 2, 2, 10],
    [5, 5],
    [9],
    [7, 6, 78, 85, 23, 34, 78, 99, 56, 33, 1],
    [1, 2, 3, 4, 6, 7, 8, 9, 10, 11],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
]

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        length = len(cost)
        cost_sorted = sorted(cost)
        cost_sorted = cost_sorted[::-1]
        total_cost = 0

        for i in range(0, length, 3):
            if length - i == 1:
                total_cost += cost_sorted[i]
                break

            total_cost += cost_sorted[i] + cost_sorted[i + 1]

        return total_cost

solution = Solution()

for data in datas:
    result = solution.minimumCost(data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

