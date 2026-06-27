# [Encode and Decode Strings - LeetCode](https://leetcode.com/problems/encode-and-decode-strings/description/)
# 271. Encode and Decode Strings
#
# Medium
#
# Topics
# Array
# String
# Design
#
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# String encode(List<String> strs) {
#     // ... your code
#     return encoded_string;
# }
#
# Machine 2 (receiver) has the function:
#
# List<String> decode(String encoded_string) {
#     // ... your code
#     return decoded_strs;
# }
#
# So Machine 1 does:
#
# String encoded_string = encode(strs);
#
# and Machine 2 does:
#
# List<String> decoded_strs = decode(encoded_string);
#
# decoded_strs in Machine 2 should be the same as the input strs in Machine 1.
#
# Implement the encode and decode methods.
#
# Example 1:
#
# Input: strs = ["Hello","World"]
# Output: ["Hello","World"]
#
# Explanation:
#
# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);
#
# // Machine 1 ---encoded_string---> Machine 2
#
# List<String> decoded_strs = solution.decode(encoded_string);
#
#
# Example 2:
#
# Input: strs = [""]
# Output: [""]
#
# Constraints:
#
#     0 <= strs.length < 100
#     0 <= strs[i].length < 200
#     strs[i] contains any possible characters out of 256 valid ASCII characters.
#
# Follow up: Could you write a generalized algorithm to work on any possible set of characters?

# Algorithmic time complexity: O(?)
# Algorithmic space complexity: O(?)

from pprint import pprint
from timeit import default_timer as timer

# start benchmark
start = timer()

datas = [
    {'strs': ["Hello","World"]},
    {'strs': [""]},
]

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ''

        for my_str in strs:
            length = len(my_str)
            result += str(length) + ':' + my_str

        return result

    def decode(self, s: str) -> List[str]:
        s_length = len(s)
        strs = []
        i = 0

        while i < s_length:
            length = ''

            # read until separator char
            while s[i] != ':':
                length += s[i]
                i += 1

            length = int(length)
            my_str = s[i+1:i+1+length]
            strs.append(my_str)

            i = i+1+length

        return strs

solution = Solution()

for data in datas:
    encoded_string = solution.encode(**data)
    result = solution.decode(encoded_string)
    print(f'{data=}')
    print(f'{result=}')
    print()

# stop benchmark
end = timer()
duration = end - start
print(f'{duration=}')

