#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (71.96%)
# Likes:    11577
# Dislikes: 258
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '"abc"'
#
# Given a string s, return the number of palindromic substrings in it.
# 
# A string is a palindrome when it reads the same backward as forward.
# 
# A substring is a contiguous sequence of characters within the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# Example 2:
# 
# 
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
# Expand Around Possible Centers method:
# There are two types of palindromes: Odd and even length palindromes!
# TC: O(n^2), 对于odd length第一个n:starting at every single character as a middle position; 对于even length第一个n: starting at every pair of characters; 第二个n: expand outwards all the way to the end of string
# SC: O(1): We don't need to allocate any extra space since we are repeatedly iterating on the input string itself.
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)): # We choose all possible centers for potential palindromes
            # odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
# For every center, we can expand around it as long as we get palindromes (i.e. the first and last characters should match).
                l -= 1
                r += 1
            # even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count

# 引入helper function后的condense写法:
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPali(s, i, i)
            count += self.countPali(s, i, i+1)
        return count
    def countPali(self, s : str, l: int, r: int) -> int:
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

            
# @lc code=end

