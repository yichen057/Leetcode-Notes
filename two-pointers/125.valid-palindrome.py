#
# @lc app=leetcode id=125 lang=python3
# @lcpr version=30403
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (53.28%)
# Likes:    11717
# Dislikes: 8650
# Total Accepted:    5.4M
# Total Submissions: 10.2M
# Testcase Example:  '"A man, a plan, a canal: Panama"\n"race a car"\n" "'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# 
# Example 1:
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# 
# 
# Example 2:
# 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# 
# 
# Example 3:
# 
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
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
# 本题要求: 
# 1. 忽略大小写
# 2. 忽略非字母数字字符
# 3. 只比较 alphanumeric characters
# 使用相向双指针, 因为每个字符最多被左右指针扫描一次，没有创建新的字符串。所以时间和空间复杂度如下:
# Time Complexity: O(n)
# Space Complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum(): # ignore non-alphanumeric /ˌælfənuːˈmerɪk/ characters on the left跳过左边非字母数字
                l += 1
            while l < r and not s[r].isalnum(): # ignore non-alphanumeric characters on the right跳过右边非字母数字
                r -= 1
            if s[l].lower() != s[r].lower(): # 比较时统一小写
                return False
            l += 1
            r -= 1
        return True
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

