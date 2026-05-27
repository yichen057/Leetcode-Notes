#
# @lc app=leetcode id=1513 lang=python3
# @lcpr version=30403
#
# [1513] Number of Substrings With Only 1s
#
# https://leetcode.com/problems/number-of-substrings-with-only-1s/description/
#
# algorithms
# Medium (57.41%)
# Likes:    1233
# Dislikes: 42
# Total Accepted:    161.6K
# Total Submissions: 281.5K
# Testcase Example:  '"0110111"\n"101"\n"111111"'
#
# Given a binary string s, return the number of substrings with all characters
# 1's. Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
# 
# Example 2:
# 
# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
# 
# 
# Example 3:
# 
# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Method 1: Counter连续1计数方法
class Solution:
    # TC: O(n), because we scan the string once.
    # SC: O(1), because we only use two integer variables.
    def numSub(self, s: str) -> int:
        current_ones = 0 # 以当前这个位置结尾的全 1 子串数量。
        answer = 0
        mod = 10 ** 9 + 7

        for ch in s:
            if ch == "1":
                # current_ones represents the number of all-ones
                # substrings ending at the current position.
                current_ones += 1
                answer = (answer + current_ones) % mod 
                # 在 Python 里，最后统一取模也可以通过；在一些整数有范围限制的语言里，比如 Java 或 C++，循环中及时取模更安全。
            else:
                # A '0' breaks the current consecutive ones sequence.
                current_ones = 0 # 遇到 0 要重置, 是因为全1子串必须连续. 遇到 0，连续的 1 被打断，需重新开始统计。
        
        return answer 
# Method 2: Same-direction two pointer method: 固定起点 i，用不回头的右指针 j 找到所有以 i 开头的合法全零子串。 
# TC: O(n), because both i and j only move from left to right.
# SC: O(1), because we only use constant extra variables.
class Solution:
    def numSub(self, s: str) -> int:
        if not s:
            return 0
        
        # i: the start index of an all-zero substring
        # j: the first position that cannot be included in the all-zero substring
        # starting from i. The valid range is [i, j).
        j = 1
        answer = 0
        mod = 10 ** 9 + 7

        for i in range(len(s)):
            # print("i:",i)
            # print("s[i]:",s[i])
            # Only a character "1" can be the starting point of a substring containing only ones.
            if s[i] != "1":
                continue
            # Make sure j is at least one position after i and never moves backward.
            # 如果j已在更右边, 则保留当前位置j; 如果j落在i前的位置, 则至少移动到i+1
            j = max(j, i + 1)
            print("max j:",j)
            # Extend j while the substring still contains only "1". j最后落在不含1的位置
            while j < len(s) and s[j] == "1": # 注意: 这里是while让j满足条件下循环+1, 而不是单独一个if条件判断!
                j += 1
                # print("inner j:", j)

            # There are j - i all-one substrings starting at index i.
            answer +=  j - i # 这里无需j-i+1, 因为j指向的是"0"不是"1"
        #     print("answer:",answer)
        # print("final ans:", answer % mod)
        return answer % mod

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "0110111"\n
# @lcpr case=end

# @lcpr case=start
# "101"\n
# @lcpr case=end

# @lcpr case=start
# "111111"\n
# @lcpr case=end

#

