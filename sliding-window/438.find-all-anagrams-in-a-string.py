#
# @lc app=leetcode id=438 lang=python3
# @lcpr version=30403
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (53.80%)
# Likes:    13262
# Dislikes: 378
# Total Accepted:    1.2M
# Total Submissions: 2.3M
# Testcase Example:  '"cbaebabacd"\n"abc"\n"abab"\n"ab"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
# 
# 
# Example 1:
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# Example 2:
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 本题的两个方法, 复杂度相同
# Dictionary version: TC O(n), SC O(1), SC: O(26) = O(1)
# List version:       TC O(n), SC O(1), SC: O(26) = O(1)

# 本题和LC567, LC643题很像, 都是fixed-size window, 用到sliding window方法做
# 做题模板如下
# left = 0
# window_state = ...
# result = ...

# for right in range(len(data)):
#     # 1. Add the right element into the window.
#     ...

#     # 2. If the window is too long, remove the left element.
#     if right - left + 1 > target_length:
#         ...
#         left += 1

#     # 3. When the window has the correct size,
#     #    check whether it satisfies the requirement.
#     if right - left + 1 == target_length and window_is_valid:
#         ...

# method 1. fixed-size window + list method: 题目明确只有 'a' 到 'z'的固定字符集，想写更标准/更快, 可用[0] * 26的方式做
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window = [0] * 26
        need = [0] * 26
        for ch in p:
            need[ord(ch)-ord('a')] += 1

        l = 0
        for r in range(len(s)): # 总共遍历s一次, 所以TC: O(n)
            window[ord(s[r])-ord('a')] += 1

            if r-l+1 > len(p):
                window[ord(s[l])-ord('a')] -= 1 # 而 list 版本不需要删除元素，因为所有字符位置一直都在, 只需减一即可, 0本来就是数组中的正常值
                l += 1
            if r - l + 1 == len(p) and window == need: # 每轮比较window == need, 两个 list 长度固定为 26。 比较成本是：O(26) = O(1)
                res.append(l)
        return res
    
# method 2. Fixed-size Sliding Window + Frequency Maps
# TC: O(n), because s is scanned once and dictionary comparison checks at most 26 lowercase letters.
# SC: O(1) excluding the output list, because there are only 26 lowercase English letters.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = {} # Character frequencies map in the current window
        need = {} # Character frequencies map required by p
        res = []

        for ch in p:
            need[ch] = need.get(ch, 0) + 1

        l = 0
        for r in range(len(s)):
            #print("r:", r)
            # Add the new right character into the current window.
            window[s[r]] = window.get(s[r], 0) + 1
            #print("window:", window)
            # Keep the window size no larger than len(p).
            if r - l + 1 > len(p):
                window[s[l]] -= 1
                #print("s[l]:",s[l], "window[s[l]]",window[s[l]])

                # Remove zero-frequency keys so that dictionary comparison accurately represents the current window.
                # 为什么要这么做呢？因为 Python 在对比两个字典是否相等（window == count）时，{'a': 1, 'b': 0} 和 {'a': 1} 会被认为是不相等的。只有把频次为 0 的键彻底删掉，才能保证字典的比对逻辑完全正确！
                # 用dictionary 比较时，必须删除频率为 0 的 key, 否则在python里两个字典是不相等的.
                if window[s[l]] == 0:
                    # 以下两种方法都可以删除这个 key-value pair。
                    del window[s[l]] # 当确定这个键一定在字典里，直接用del window[key]合适; 如果你尝试 del 一个不存在的键，程序会直接报错（抛出 KeyError）. 本题更推荐用 del, 因为这里目的只是删除这个键值对，不需要使用被删除的 value: removed_value = window.pop(key)。删除这个 key，同时取得它原来的 value。
                    # window.pop(s[l]) # 如果想在删除的同时拿到那个被删掉的值val = my_dict.pop('b')，或者想避免“键不存在就报错”的尴尬情况val2 = my_dict.pop('c', None)，可以使用 pop()。

                l += 1

            # If the fixed-size window has the same frequency map as p, record its starting index.
            if r - l + 1 == len(p) and window == need: # 注: {"c": 0} 如果有这样的多余 key，会导致本该匹配的窗口被错误判断为不匹配。
                #print("l:",l, "r:", r)
                res.append(l)
                #print("res:",res)
        return res

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

