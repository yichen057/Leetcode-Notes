#
# @lc app=leetcode id=541 lang=python3
# @lcpr version=30305
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (53.15%)
# Likes:    2301
# Dislikes: 4360
# Total Accepted:    359.9K
# Total Submissions: 677.3K
# Testcase Example:  '"abcdefg"\n2\n"abcd"\n2'
#
# Given a string s and an integer k, reverse the first k characters for every
# 2k characters counting from the start of the string.
# 
# If there are fewer than k characters left, reverse all of them. If there are
# less than 2k but greater than or equal to k characters, then reverse the
# first k characters and leave the other as original.
# 
# 
# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *
# 每隔 2k 个字符，反转前 k 个字符
# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 方法一: 切片反转
        # res = list(s) # str 在python里是不可变的, 所以必须转为可变的列表list, 才能对里面的字符进行修改和交换
        # for i in range(0, len(res), 2*k): # 使用range(start, stop, step) 函数来确定需要调换的初始位置。i的值从索引0开始, 循环到列表末尾结束, 每一次循环, i=0, 2k, 4k,...
        #     res[i: i+k] = res[i:i+k][::-1] # 反转前k个字符后, 更改原值为反转后值. 用切片整体替换, 而不是一个个替换
# res[i:i+k]：取出从位置 i 开始的 k 个字符
# 例如：i=0, k=2 → res[0:2] = ['a', 'b']
# [::-1]：反转切片（Python 反转语法）
# ['a', 'b'][::-1] = ['b', 'a']
# 赋值回原位置：整体替换（不需要逐个交换）
# Python 切片自动截断, 无需做判断
        
        # 方法二: reverse自主实现(two pointer approach)
        def reverse_substring(text: List[str]) -> List[str]:
            left, right = 0, len(text)-1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        
        res = list(s)
        for i in range(0, len(s), 2*k):
            res[i: i+k] = reverse_substring(res[i: i+k])

        return ''.join(res) # 将 list 转回 str. 用空字符串 '' 作为连接符，将列表 res 中的所有字符连接起来。eg: ['a', 'b', 'c'] -> 'abc'
    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "abcdefg"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

#

#补充卡码网题目: 替换数字 
#给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。
# 例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。
# 对于输入字符串 "a5b"，函数应该将其转换为 "anumberb"
# 输入：一个字符串 s,s 仅包含小写字母和数字字符。
# 输出：打印一个新的字符串，其中每个数字字符都被替换为了number
# 样例输入：a1b2c3
# 样例输出：anumberbnumbercnumber
# 数据范围：1 <= s.length < 10000。
class Solution:
    def replace_number(self, s: str) -> str:
        """
        题目：将字符串 s 中的每个数字字符替换为 "number"
        核心思路：先扩容，然后从后向前填充，避免频繁移动元素。
        """
        # --- 第一步：统计有多少个数字 ---
        digit_count=0
        for char in s:
            if char.isdigit():
                digit_count += 1

        # --- 第二步：计算扩容后的新长度 ---
        # 原字符串长度
        old_length = len(s)
        # 新长度 = 原长度 + (数字个数 * 5)
        # 为什么乘5？因为 "number" 是6个字符，原数字占1个，替换后相当于多占了5个坑位
        new_length = old_length + (digit_count * 5)

        # --- 第三步：创建新列表（预先占位） ---
        # Python字符串不可变，所以我们需要一个列表来模拟字符数组
        # 创建一个长度为 new_length 的列表，里面全填上空字符
        res = [''] * new_length

        # --- 第四步：定义双指针（核心！） ---
        # old_ptr 指向原字符串的最后一个字符
        old_ptr = old_length - 1
        # new_ptr 指向新列表的最后一个空位
        new_ptr = new_length - 1

        # --- 第五步：从后向前遍历 ---
        # 如果从前向后填充，每次遇到一个数字插入 "number"，后面的所有字符都要向后移动，时间复杂度会变成 O(n^2)。
        # 从后向前填充的好处是：直接把字符放到最终位置，每个字符只处理一次，时间复杂度是 O(n)。
        while old_ptr >= 0:
            current_char = s[old_ptr]
            
            # --- 情况A：如果是数字，填入 "number" ---
            if current_char.isdigit():
                # 我们需要填入 'n', 'u', 'm', 'b', 'e', 'r' 这6个字符
                # 因为是从后往前填，用切片操作
                # 例如：new_ptr=10 时，填入下标 5-10 的位置
                start_pos = new_ptr - 5
                end_pos = new_ptr + 1
                res[start_pos:end_pos] = "number"
                new_ptr -= 6

            # --- 情况B：如果是字母，直接复制过来 ---
            else:
                res[new_ptr] = current_char
                new_ptr -= 1
            
            # 无论填什么，旧指针都要向前走 1 格
            old_ptr -= 1

        # --- 第六步：将列表转回字符串并返回 ---
        return "".join(res)
    
# --- 运行测试代码 ---
if __name__ == "__main__":
    # 实例化解题类
    solution = Solution()
    
    # 测试用例 1
    test1 = "a1b2c3"
    result1 = solution.replace_number(test1)
    print(f"输入: {test1}")
    print(f"输出: {result1}")
    print(f"预期: anumberbnumbercnumber")
    print()
    
    # 测试用例 2
    test2 = "a5b"
    result2 = solution.replace_number(test2)
    print(f"输入: {test2}")
    print(f"输出: {result2}")
    print(f"预期: anumberb")