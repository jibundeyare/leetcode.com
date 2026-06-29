# ...
# ...
#
# Easy
# Medium
# Hard
#
# Topics
# ...
#
# ...

# Algorithmic time complexity: O(?)
# Algorithmic space complexity: O(?)

# Inspiration:
# - None
# - ...

from mylib_leetcode import test_result
from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {
        'Input': dict(),
        'Output': None,
    },
    {
        'Input': dict(),
        'Output': None,
    },
    {
        'Input': dict(),
        'Output': None,
    },
]

class Solution:
    def foo(self):
        ...

solution = Solution()

for data in datas:
    result = solution.foo(**data['Input'])
    print(f'{data=}')
    print(f'{result=}')
    test_result(result, data['Output'])
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

