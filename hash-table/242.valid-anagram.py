#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (67.03%)
# Likes:    13559
# Dislikes: 456
# Total Accepted:    5.3M
# Total Submissions: 7.9M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 长度不等直接返回, 不用浪费计算
        if len(s) != len(t):
            return False
        
        # 用数组的哈希法做
        record = [0] * 26 # 创建长度为26的数组, 默认值为0. 题目里只有小写字母 'a'..'z'，它们的 ASCII 是 97~122。
        for i in s:
            record[ord(i)-ord("a")] += 1 # 用 ord(i) - ord("a")，就把 'a' 映射到 0，'z' 映射到 25，这样只需要一个 长度为 26 的数组。
            # ord() 在 Python 里就是把字符转换成 Unicode 编码（常见情况就是 ASCII 值）。
        for i in t:
            record[ord(i)-ord("a")] -= 1
            # 方法一, 提前判断
            if record[ord(i)-ord("a")] < 0:
            # 注意判断条件不能写!=0, 因为此处这个判断还没有把整个t都遍历完. 
            # s里同一个字母如果出现2次以上, 则count里元素对应是>=2的, 那t在减1时, 第一次-1得到的值未必等于0 ,有可能大于0, 那么对于>0的情况, 如果这里判断为不等于0, 就会提前误判
                return False
            
        #方法二: 循环后遍历这个新数组统一检查, 看有没有元素不为0, 则return false
        # for i in range(26):
        #     if record[i] != 0:
        #         return False
        return True
    
#     对比结论
# 最坏复杂度：方法一 = 方法二 = O(n)
# 最好情况：方法一更快（可以提前返回），方法二还是要扫完
# 常数开销：方法一不需要额外检查数组，方法二多一个 O(26) 的循环，但这可以认为是常数级无关紧要
# @lc code=end

