#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30403
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (48.91%)
# Likes:    13074
# Dislikes: 524
# Total Accepted:    1.5M
# Total Submissions: 3.1M
# Testcase Example:  '"ab"\n"eidbaooo"\n"ab"\n"eidboaoo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of
# s2.
# 
# 
# Example 1:
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 本题要点如下
# 1. 本题和LC3和LC424不同, substring的长度不是不断变化找最长的, 而是窗口长度固定位len(s1) + 频率是否匹配
# 2. 比较的是frequency而不是比较字符串, permutation类似Anagram, 只要字母及其字符频率完全相同即可, 顺序不重要 -> 所以需要知道s1 中每个字母出现几次, 当前窗口中每个字母出现几次. 如果这两个 frequency array 完全相同, 即窗口频率==s1频率时，就找到了排列, 当前窗口就是一个排列。
# 3. string里只包含小写字母：a到z共26个字母 
# 本题需要展示的是: 
# 1. 你识别出这是 permutation → frequency count；
# 2. 你识别出 permutation 长度固定 → fixed-size sliding window；
# 3. 你能维护窗口频率并正确判断；
# 4. 你能分析出 O(n) 时间、O(1) 空间。
# 5. 出现 permutation / anagram + 找某个 substring → 想 fixed-size sliding window + frequency count
# 做题:模板
# 先建立第一个长度为 len(s1) 的窗口
# 如果频率相等:
#     return True
# 右边加入一个字符
# 左边移出一个字符
# 继续判断频率是否相等

# sliding window 模板
# right 扩大窗口
# invalid 时 left 缩小窗口
# valid 后更新答案

# 本题将上述模板的更加具象化:
# right 扩大窗口
# 窗口长度超过固定大小时，left 移出一个字符
# 窗口大小正确且 frequency 匹配时，返回 True

# LC 567. Permutation in String
# Pattern: Fixed-size Sliding Window + Frequency Arrays
#
# Recognition:
# - "permutation" -> compare character frequencies
# - Any permutation of s1 has fixed length len(s1)
# - Therefore, slide a fixed-size window over s2
#
# Window:
# - l and r define the current substring s2[l : r + 1]
# - Add s2[r]
# - If window size > len(s1), remove s2[l] and move l
# - If window size == len(s1) and window == need, return True
#
# TC: O(n), since we scan s2 once and compare arrays of fixed size 26.
# SC: O(1), since both frequency arrays have fixed size 26.
class Solution:
    # Method 1: Fixed-size Sliding Window + Frequency Arrays (one for loop), 更推荐!
    # TC: O(n), because the right pointer scans s2 once, where n is the length of s2. 总时间复杂度是O(26) = O(1)
    # SC: O(1), because the arrays always store 26 lowercase English letters.需要比较两个长度为26的数组O(26) = O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = len(s1)
        need = [0] * 26
        window = [0] * 26

        # Build the target frequency array for s1.
        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        # print("need:",need)

        # sliding window portion:
        l = 0

        for r in range(len(s2)):
            # Expand the window by adding the current right character: include s2[r] in the current window.
            window[ord(s2[r]) - ord('a')] += 1

            # Keep the window size no larger than m=len(s1).
            if r - l + 1 > m:
                window[ord(s2[l]) - ord('a')] -= 1 # 注意里面的ord(s2[l])是l不让r
                l += 1

            # A fixed-size window with the same frequency is a permutation of s1.
            if r - l + 1 == m and need == window:
                return True

        return False
class Solution:
    # Method 2: Fixed-size Sliding Window + Frequency Arrays (two for loops)
    # TC: O(n), because each window comparison checks only 26 letters.
    # SC: O(1), because the two arrays always have length 26.
# m = len(s1), n = len(s2)
# 先建立 need 和第一窗口：O(m)
# 滑动 s2 后续窗口：O(n - m)
# 每次比较两个长度 26 的数组：O(26) = O(1)
# 总计：O(m + n)；由于 m <= n，所以也可以写 O(n)。
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = len(s1)
        need = [0] * 26      # Frequency of characters in s1
        window = [0] * 26    # Frequency of characters in the current window of s2

        # Build the frequency arrays for s1 and the first window in s2.
        for i in range(m):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # Check the first window.
        # 检查的是：第一个窗口 s2[0:m]。
        if need == window:
            return True

        # Slide the fixed-size window through s2.
        for r in range(m, len(s2)):
            # Add the new character entering from the right.
            window[ord(s2[r]) - ord('a')] += 1

            # Remove the old character leaving from the left.
            left_char = s2[r - m]
            window[ord(left_char) - ord('a')] -= 1

            # Same character frequencies means this window is a permutation of s1.
            #检查的是：负责除第一处以外的所有窗口, 每次向右滑动后产生的新窗口。
            if need == window:
                return True

        return False

# # method 3: sliding window + frequency arrays + 引入额外变量matches
# class Solution:
#     # Sliding Window + Matches Counter
#     # TC: O(n)
#     # SC: O(1)
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         m = len(s1)
#         s1_count = [0] * 26
#         window_count = [0] * 26

#         # Build frequency arrays for s1 and the first window.
#         for i in range(m):
#             s1_count[ord(s1[i]) - ord('a')] += 1
#             window_count[ord(s2[i]) - ord('a')] += 1

#         # Count how many letter frequencies already match.
#         matches = 0
#         for i in range(26):
#             if s1_count[i] == window_count[i]:
#                 matches += 1
        
#         # sliding window portion
#         l = 0

#         for r in range(m, len(s2)):
#             # Before sliding, check the current window.
#             if matches == 26:
#                 return True

#             # Add the new right character into the window.
#             right_index = ord(s2[r]) - ord('a')
#             window_count[right_index] += 1

#             if window_count[right_index] == s1_count[right_index]:
#                 matches += 1
#             elif window_count[right_index] == s1_count[right_index] + 1:
#                 matches -= 1

#             # Remove the old left character from the window.
#             left_index = ord(s2[l]) - ord('a')
#             window_count[left_index] -= 1

#             if window_count[left_index] == s1_count[left_index]:
#                 matches += 1
#             elif window_count[left_index] == s1_count[left_index] - 1:
#                 matches -= 1

#             l += 1

#         return matches == 26



# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

