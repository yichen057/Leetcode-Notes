#
# @lc app=leetcode id=459 lang=python3
# @lcpr version=30305
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (47.67%)
# Likes:    6804
# Dislikes: 563
# Total Accepted:    584.1K
# Total Submissions: 1.2M
# Testcase Example:  '"abab"\n"aba"\n"abcabcabcabc"'
#
# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
# 
# 
# Example 1:
# 
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# 
# 
# Example 2:
# 
# Input: s = "aba"
# Output: false
# 
# 
# Example 3:
# 
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc"
# twice.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Brute Force Method
        #  1. 确定“候选子串”的特征
# 首先，我们需要缩小搜索范围。如果一个字符串 `s` 是由某个子串重复构成的，那么这个子串必须满足两个硬性条件：
# 1. **它必须是从头开始的（前缀）： 比如 `s = "abab"`, 重复的子串只能是 `"a"` 或者 `"ab"`，不可能是在中间的 `"b"` 或 `"ba"`。
# 2. **它的长度必须能整除总长度： 比如 `s` 的长度是 10，那么子串的长度只可能是 1, 2, 5。子串长度不可能是 3，因为 10 无法被 3 整除，拼不出来。
# 3. **它的长度最多是原字符串的一半：因为至少要重复 2 次，所以子串长度不能超过 `len(s) / 2`。
        n = len(s)
        # 只需枚举到一半长度. 因为任何超过长度一半的子串，哪怕只重复最小的 2 次，拼接后的总长度都会超过原字符串，因此根本不需要去检查它们。
        for i in range(1, n//2+1):
            # 子串长度必须能被总长度整除. 只有当i能整除n时, 才可能是答案
            if n % i == 0:
                # 因为前缀是从头开始的,取出前缀子串(字符串切片slicing), 冒号在前面表示从开头一直到这里, 不包含i项
                sub = s[:i] # 这是一个新的字符串对象 sub. 当你执行 s[:i] 时，Python 会在内存中开辟一块新的空间，把 s 的前 i 个字符复制进去。
                # 拼接子串并和s比对
                if sub * (n // i) == s: 
                    # 这是最消耗内存的一步。当你把 sub 重复 n // i 次时，程序会在内存中重新分配一块大小等于原字符串 s 长度（即 N）的空间，并将 sub 的内容填满这块空间。
                    # 结果： 这产生了一个全新的、长度为N的字符串（暂且叫它 temp）。
                    # 比较： 最后，程序拿这个新生成的 temp 去和原字符串 s 进行逐字符比较。
                    return True
        return False
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "abab"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "abcabcabcabc"\n
# @lcpr case=end

#

