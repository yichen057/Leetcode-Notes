#
# @lc app=leetcode id=424 lang=python3
# @lcpr version=30403
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (59.68%)
# Likes:    13147
# Dislikes: 769
# Total Accepted:    1.6M
# Total Submissions: 2.7M
# Testcase Example:  '"ABAB"\n2\n"AABABBA"\n1'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
# 
# 
# Example 1:
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 方法一: 
# 固定左指针 i，
# 右指针 j 尽量往右走，while 窗口还合法: j += 1
# 直到多走到一个不合法窗口。
# j is the exclusive right boundary of the current window.
# The current window is s[i:j].
# This version may expand one character beyond a valid window,
# so we subtract 1 when the window becomes invalid.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        # j指向满足条件的子字符串的后一个位置, 即找[i, j-1]是最长的以i开头的满足不超过k次替换的substring
        j = 0  
        maxFreq = 0 
        counter = {}
        answer = 0
        for i in range(len(s)):
            while j < len(s) and j - i - maxFreq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                maxFreq = max(maxFreq, counter[s[j]])
                j += 1
            if j - i - maxFreq > k:
                # i ~ j-1 这段substring需要k+1次替换
                # i ~ j-2 这段(长度j-i-1)substring只需要k次替换
                answer = max(answer, j-i-1)
            else:
                # i ~ j - 1的substring <= k替换
                answer = max(answer, j - i)
            counter[s[i]] -= 1
            maxFreq = max(counter.values()) # O(26) = O(1), 26个字母
        return answer
# method 2: sliding window + frequency map 最好理解!
# 每次判断窗口时，都重新计算：max(count.values()
# TC: O(n), since each pointer only moves forward.
# SC: O(26) = O(1), since s contains only 26 uppercase English letters.
# I use a sliding window. For each window, I keep the most frequent character
# and replace all the other characters. Therefore, the number of replacements
# needed is window length minus the maximum frequency. If this value exceeds k,
# I shrink the window from the left. Since both pointers only move forward,
# the time complexity is O(n).
# 右指针扩张窗口；
# 窗口需要替换的字符超过 k 时，左指针收缩窗口. 所以while 窗口invalid时: l += 1
# r 已经把新字符加入窗口了。如果窗口因此不合法，就需要不断移动 l 修复窗口；而移动一次 l 不一定够，所以必须用 while，不能只用 if。
# 每次窗口合法时，更新最长长度。
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)): # r 和 l都走一遍字符串, 时间复杂度: O(n)
            # Expand the window by including the current character: s[r].
            count[s[r]] = count.get(s[r], 0) + 1

            # check the current window validility:
            # The number of replacements needed in that window = window size - frequency of the most frequent character.
            # The window is invalid if more than k characters
            # 当上述差值 <= k时, current window is valid, 移动右指针, 同时更新frequency map: count
            # 当上述差值 > k时, current window is unvalid, 移动左指针, 同时更新frequency map: count
            while (r-l+1) - max(count.values()) > k: #每次判断max(count.values())最多扫描 26 个字母, TC: O(26) = O(1)
            # r 已经把新字符加入窗口了。如果窗口因此不合法，就需要不断移动 l 修复窗口；而移动一次 l 不一定够，所以必须用 while，不能只用 if。
                # The window is invalid, so shrink it from the left. Shrink the window from the left until it becomes valid.
                # 向右移动l左指针
                count[s[l]] -= 1 # 更新frequency map, 这一步不要忘记!
                l += 1 
            # The current window is valid.
            res = max(res, r-l+1)   

        return res
# 方法二的滑动窗口模板:
# right 扩大窗口；
# invalid 时 left 缩小窗口；
# valid 后更新答案。

# 适配以下题: 
# LC 3  Longest Substring Without Repeating Characters
# LC 424 Longest Repeating Character Replacement
# LC 567 Permutation in String
# LC 76 Minimum Window Substring
# for right in range(len(s)):
#     # Add s[right] into the window.

#     while window is invalid:
#         # Remove s[left] from the window.while当前窗口不合法时, 移动左指针, 缩小窗口
#         # 此处用while不用if是因为, 左指针移动一次后, 窗口不一定立刻合法
#         left += 1

#     # Update the answer.
# method 3: # Sliding Window + Cached Maximum Frequency. 标准滑动窗口 + 缓存 maxf, add maxf variable. 用一个变量保存历史最大频率：maxf = max(maxf, count[s[r]]), 因此不需要反复扫描字典. 
# 重点理解 Method 3 中 maxf 为什么不需要随着左指针移动而减小: 本题只关心曾经能够达到的最长合法窗口长度. maxf 记录的是到目前为止，某个窗口里曾经出现过的最高字符频率。所以 maxf 只需要在加入新字符时增加，不需要在左边缩小时减少。
# maxf is the largest frequency seen while expanding the window. It may not be the exact maximum frequency after shrinking, but it is sufficient for finding the maximum valid window length.
# 本方法要点: r 加入新字符, 只在加入时更新 maxf, 窗口非法时 l 右移, 不重新计算真实 max frequency
# r 加入新字符
# 只在加入时更新 maxf
# 窗口非法时 l 右移
# 不重新计算真实 max frequency
# TC: O(n)
# SC: O(1). 虽然 Big-O 和 Method 2 一样，但 Method 3 的实际常数更小。这里每次不再调用：max(count.values()), 而是常数时间更新: maxf = max(maxf, count[s[r]])
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]]) # maxf 记录的是到目前为止，某个窗口里曾经出现过的最高字符频率。所以 maxf 只需要在加入新字符时增加，不需要在左边缩小时减少。
            # check the current window validility
            # length - frequency of the most frequent character = the number of char need to replace in that window
            # 当上述差值 <= k时, current window is valid, 移动右指针, 同时更新frequency map: count
            # 当上述差值 > k时, current window is unvalid, 移动左指针, 同时更新frequency map: count
            while (r-l+1) - maxf > k:
                # 向右移动l左指针
                count[s[l]] -= 1
                l += 1 

            res = max(res, r-l+1)   

        return res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#

