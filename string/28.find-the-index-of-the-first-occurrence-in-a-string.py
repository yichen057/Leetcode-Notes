#
# @lc app=leetcode id=28 lang=python3
# @lcpr version=30305
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (46.05%)
# Likes:    7373
# Dislikes: 560
# Total Accepted:    3.8M
# Total Submissions: 8.3M
# Testcase Example:  '"sadbutsad"\n"sad"\n"leetcode"\n"leeto"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
# 
# 
# Example 1:
# 
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# 
# 
# Example 2:
# 
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 方法一: 切片法
        # n, m =len(haystack), len(needle)
        # # 只需要遍历到 n - m 的位置即可，后面剩下的长度不够 needle 长了. 
        # 之所以是 n - m + 1 而不是 m + 1，是因为循环变量 i 代表的是子串的“起始位置”，我们需要保证从这个位置开始往后数，剩余的长度还够放得下整个 needle
        # Python 的 range 函数是左闭右开的。需要遍历的下标范围是：0, 1, 2, ..., n-m。为了让循环能取到 n-m 这个值，range 的结束参数必须写成 (n - m) + 1。
        # for i in range(n - m + 1):
        #     # 截取子串进行比较. Python 的切片语法 [start : end] 确实是 左闭右开 的
        # 保证子串needle的长度是(i + m) - i = m
        # 虽然这里用了切片 haystack[i : i + m]，其底层也是字符逐个比较，时间复杂度总体接近O(N * M)
        #     if haystack[i: i + m] == needle:
        #         return i
        # return -1
        # 方法二: 纯循环方法
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            # 将needle的元素逐个与haystack的字符对比
            index_needle = 0
            index_haystack = i
            while index_needle < m and haystack[index_haystack] == needle[index_needle]:
                index_haystack += 1
                index_needle += 1
            
            # 如果index_needle走到了末尾, 说明完全匹配
            if index_needle == m:
                return i
            
        return -1
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#

