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

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
]

class Solution:
    def foo(self, bar):
        ...

solution = Solution()

for data in datas:
    result = solution.foo(**data)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

