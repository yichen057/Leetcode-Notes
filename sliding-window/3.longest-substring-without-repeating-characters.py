#
# @lc app=leetcode id=3 lang=python3
# @lcpr version=30403
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (39.05%)
# Likes:    45097
# Dislikes: 2219
# Total Accepted:    9.5M
# Total Submissions: 24.3M
# Testcase Example:  '"abcabcbb"\n"bbbbb"\n"pwwkew"'
#
# Given a string s, find the length of the longest substring without duplicate
# characters.
# 
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and
# "cab" are also correct answers.
# 
# 
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# Substring（子串）：必须是原字符串中连续的一段字符。本题涉及substring
# Subsequence（子序列）：可以不连续，但字符的相对顺序必须不变。
# @lc code=start
    
class Solution:
    # Sliding Window + Hash Map
    # TC: O(n)
    # SC: O(min(n, charset_size)), which is O(n) in the worst case. 
    # 意思是字典 char_idx 最多存储的字符数量，既不会超过字符串长度 n，也不会超过所有可能字符的总数量 charset_size。所以取两者中更小的那个。
    # If s consists of lowercase English letters only, SC: O(1), cus only have 26 letters.
     """
        Sliding Window + Hash Map

        TC: O(n)
            The end pointer scans each character once.
            The start pointer only moves forward and never moves backward.

        SC: O(min(n, charset_size))
            The dictionary stores the most recent index of each character
            in the string. In the worst case, it may store O(n) characters.
        """
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}  # character -> its most recent index
        start = 0      # left boundary of the current window
        maxLen = 0     # length of the longest valid window

        for end in range(len(s)):
            current_char = s[end]

            # If the character already exists in the current window,
            # move start right after its previous occurrence.
            if current_char in char_idx and char_idx[current_char] >= start:
                # if的第二个判断条件很重要, 反例是s = "abba", 当end pointer 指向第二个a, 如果此处不判断或者判断仅为end>=start, 那么此时end = 3, start=2, 然而start = start = char_idx[current_char] + 1 = 4已经超出窗口外了
                # 所以应该判断char_idx["a"] >= start, 代入 0 >=2是false, 所以start不应该移动, 当前窗口就是"ba", 长度为2
                start = char_idx[current_char] + 1

            # Record the latest index of the current character.
            char_idx[current_char] = end

            # Calculate the length of the current valid window.
            maxLen = max(maxLen, end - start + 1)

        return maxLen

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

