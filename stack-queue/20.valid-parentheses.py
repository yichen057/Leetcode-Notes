#
# @lc app=leetcode id=20 lang=python3
# @lcpr version=30305
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (43.47%)
# Likes:    27307
# Dislikes: 1977
# Total Accepted:    7.1M
# Total Submissions: 16.3M
# Testcase Example:  '"()"\n"()[]{}"\n"(]"\n"([])"\n"([)]"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# 
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# 
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([])"
# 
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: s = "([)]"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
# 括号不匹配的情况有三种: 
# 1. 字符串里左方向的括号多余了, 所以不匹配. 遍历完字符串, 但是栈不为空, 说明有相应的左括号没有有括号来匹配, return false
# 2. 括号没多余, 但是括号的类型不匹配. 遍历字符串匹配的过程中, 发现栈里没有匹配的字符, return false
# 3. 字符串有右方向的括号多余了, 所以不匹配. 遍历字符串匹配的过程中, 栈已为空, 没有匹配的字符了, 说明右括号没有找对应的左括号, return false
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 创建list作为栈
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item: # 处理第二和第三种情况
            # 这里的判断顺序要注意, 如果直接取空栈里的元素, 会报异常, 所以需要先判断栈是否为空
            # python里, stack的查看栈顶用s[-1]; 判断栈是否为空用if not stack; 入栈用stack.append(x); 出栈用stack.pop()
                return False
            else: # 当栈不为空 且栈顶元素等于当前字符, 即找到了一对闭合的括号,匹配成功, 则用pop()把栈顶元素弹出
                stack.pop()
        
        # 最后栈空才算完全匹配
        return not stack # 如果栈都遍历完后, 栈仍有值非空, 则为第一种情况, return false; 如果栈已为空(if not stack), 则return True
        # return True if not stack else False
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

