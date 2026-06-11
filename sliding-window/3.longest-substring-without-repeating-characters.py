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
# mock版本代码, 最优解
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

class Solution:
    # method 1: Sliding Window + Set. 本方法容易理解, 适合刚开始练 sliding window 模板。
    # TC: O(n)
    # SC: O(n)
    # sliding window模板:
    # right 扩大窗口；
    # invalid 时 left 缩小窗口: 缩小窗口不光是left指针移动, 还有要将窗口set内最左边的元素做剔除；
    # valid 后更新答案。
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            # If s[r] makes the window invalid,
            # shrink the window from the left until it is valid again.
            # set写法中左指针需要一步一步移动从而去掉重复字符: 右边加入字符, 如果重复，就左边一个一个移走, 直到当前窗口没有重复。
            # 而方法二中的dictionary由于记录了index, 所以可以直接写l = char_idx["b"] + 1一次跳到right after its previous position.
            while s[r] in chars:
                #print("while inside s[r]:", s[r])
                chars.remove(s[l])
                l += 1
                #print("while inside r:",r)
                #print("while inside set:", chars)
            #print("while outside l:", l)
            #print("while outside r:",r)
            chars.add(s[r]) # Add the new character after the window becomes valid.
            #print("while outside set:", chars)
        
            maxLen = max(maxLen, r - l + 1) # The current window s[l : r + 1] contains no duplicates.

        return maxLen

class Solution:
    # method 2: Sliding Window + Hash Map直接跳跃: 代码更短；不用 while 一步步缩窗口, 也是面试中很好的写法。
    # TC: O(n)
    # SC: O(n) in the worst case
    # 本方法是方法一的升级版, 流程如下:
    # 右边加入字符；
    # 如果重复字符在当前窗口中，
    # 左边直接跳到旧字符后面。
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        char_idx = {}  # character -> its most recent index

        for r in range(len(s)):
            # If s[r] already appears in the current window,
            # move the left pointer right after its previous position.
            # 当新加入的字符重复，而且重复字符仍在当前窗口中：
            print("r: ", r)
            print("char_idx[s[r]]:",char_idx.get(s[r]))
            print("l:",l)
            if s[r] in char_idx and char_idx[s[r]] >= l: # 注意第二个条件也要判断, 否则start可能走到string末尾后又重新回撤到前面去, eg: str = "abba"
                l = char_idx[s[r]] + 1 
                # 注意: 这里不是l = r + 1, 因为在现在的r基础上再加一, l的位置就不对了可能就超出range了, l得在之前r的位置+1, 之前的位置就是hashmap记录的value: char_idx[s[r]]
                print("inside l:",l)
            # Update the most recent index of the current character.
            char_idx[s[r]] = r
            print("after char_idx[s[r]]:",char_idx.get(s[r]))
            # The current window s[l : r + 1] has no duplicate characters.
            maxLen = max(maxLen, r - l + 1)

        return maxLen
class Solution:
    # Method 3: Same-direction two pointers: fix left, extend right 固定左指针，让右指针尽量扩. 移动左指针这里需要主动删除最左边的元素, i指针会自动跟随for循环向右移动
    # TC: O(n)
    # SC: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        j = 0
        maxLen = 0

        for i in range(len(s)):
            # Extend j while adding s[j] does not create duplication.
            while j < len(s) and s[j] not in chars:
                chars.add(s[j]) # 注意加的是s[j]不是s[i], 另外是先添加到set再j+=1
                j += 1

            # Current valid window is s[i:j].
            maxLen = max(maxLen, j - i)

            # Move the left boundary to the right for the next round.
            chars.remove(s[i]) # 这一步不能忘记!

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

