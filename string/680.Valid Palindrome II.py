#
# @lc app=leetcode id=680 lang=python3
# @lcpr version=30202
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (43.33%)
# Likes:    8702
# Dislikes: 498
# Total Accepted:    1M
# Total Submissions: 2.3M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
# 先找“第一处不同”；然后尝试删左或删右其中一边；只要有一个删法能让剩下的区间是回文，就返回 True。    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s is None: # 只排除None无输入的情况
            return False
        # 注意: 此处主要不写if not s, 因为这句话包含None和空字符串"", 然而空字符串也属于回文. 
        
        left, right = self.findDifference(s, 0, len(s)-1)
        # if left < right, 说明找到一对left不等于right, 则不是回文, if left >= right, 说明遍历过后left==right,是回文
        if left >= right:
             return True
        
        # 第一次遇到left与right不等时, 对于left!=right的情况, 最多删一个字符: 要么跳过左边这个字符看剩下的是否回文, 要么跳过右边这个字符看剩下的是否回文
        # 反斜杠 \：行连接符，让长语句换行更美观（也可以用括号包起来就不需要 \ 了）。
        return self.isPalindrome(s, left + 1, right) or \
               self.isPalindrome(s, left, right - 1) 
    
    # 检查区间 [left, right] 是否是严格回文（这一步不再允许删除）。
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        left, right = self.findDifference(s, left, right)
        return left >= right
    
    # 从两端向中间走，找到第一对不相等字符的下标；若始终没差异，返回最终的相遇位置。
    def findDifference(self, s:str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return left, right # 这里return的是left<right时, 一旦发现left与right不同的一对, 立马返回
            left += 1
            right -= 1
        # 这里return的是left>right时, left与right相同的一对
        # 能走到这里说明从未遇到不等，返回的是最终相遇位置（意味着该区间是回文）。循环退出时一定是left>=right, 所以left>=right是True
        return left, right



# @lc code=end



#
# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "abca"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

