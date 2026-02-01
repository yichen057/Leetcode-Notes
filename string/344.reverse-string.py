#
# @lc app=leetcode id=344 lang=python3
# @lcpr version=30305
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (80.38%)
# Likes:    9397
# Dislikes: 1212
# Total Accepted:    3.6M
# Total Submissions: 4.5M
# Testcase Example:  '["h","e","l","l","o"]\n["H","a","n","n","a","h"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
# 
# You must do this by modifying the input array in-place with O(1) extra
# memory.
# 
# 
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *


# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # method 1: use reverse()
        # s.reverse() # 原地反转, 无返回值
        
        # method 2: use two-pointer approach
        # left, right= 0, len(s)-1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

        # method 3: use range function: 因为while每次循环需要进行条件判断，而range函数不需要，直接生成数字，因此时间复杂度更低。推荐使用range
        n = len(s)
        for i in range(n // 2): # 只要控制了长度一半以内的元素, 另外一半也就控制住了, 这里无需判断奇数/偶数
            s[i], s[n-i-1] = s[n-i-1], s[i]

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

