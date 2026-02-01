#
# @lc app=leetcode id=150 lang=python3
# @lcpr version=30305
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (56.69%)
# Likes:    8544
# Dislikes: 1176
# Total Accepted:    1.6M
# Total Submissions: 2.9M
# Testcase Example:  '["2","1","+","3","*"]\n' +
  '["4","13","5","/","+"]\n' +
  '["10","6","9","3","+","-11","*","/","*","17","+","5","+"]'
#
# You are given an array of strings tokens that represents an arithmetic
# expression in a Reverse Polish Notation.
# 
# Evaluate the expression. Return an integer that represents the value of the
# expression.
# 
# Note that:
# 
# 
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish
# notation.
# The answer and all the intermediate calculations can be represented in a
# 32-bit integer.
# 
# 
# 
# Example 1:
# 
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 方法一: C++直译版(推荐, 最适合算法面试和刷题)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:# 题目已知的输入就已经是一个切割好的字符串数组了。
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/": # 遍历到操作符, 对相邻元素作运算
            # C++ 的 pop() 是没有返回值的。而Python 的 pop() 干了两件事：既弹出了元素，又顺手把这个元素拿给你了。
            # 在 Python 里，stack.pop() = C++ top() + C++ pop()。放心直接用！
                num1 = stack.pop()
                num2 = stack.pop()

                if i == "+":
                    stack.append(num2+num1)
                elif i == "-":
                    stack.append(num2 - num1) # 减法和除法对运算有顺序要求, 需要次顶元素-/栈顶元素, 即num2-num1, num2/num1
                elif i == "*":
                    stack.append(num2 * num1)
                elif i == "/":
                    # 【关键点】Python 的整除 // 和 C++ 不一样
                    # C++ 的 / 是向零取整 (例如 -3/2 = -1)
                    # Python 的 // 是向下取整 (例如 -3//2 = -2)
                    # 所以要用 int(num2 / num1) 来完美模拟 C++ 的行为. 它利用了 int() 函数“只取整数部分”的特性，避开了 Python // 运算符“向下取整”的特性。
                    stack.append(int(num2/num1))
            else: # 
                stack.append(int(i)) # 这里将元素character 转为数字, 遍历到数字, 直接添加到stack里

        result = stack[-1] # 获取栈顶元素
        stack.pop() # 弹出stack里最后的元素,不是必须的, 只是释放内存
        return result

# 方法二: 字典映射版. 最适合实际工程开发
# 如果你是在写一个计算器软件，而不是做算法题，这种写法最好。因为它解耦了。如果以后要增加一个 ^ (乘方) 运算，你只需要在 op_map 字典里加一项，不需要去改主循环的代码。这符合“开闭原则”。
from operator import add, sub, mul

def div(x, y):
    # 使用整数除法的向零取整方式
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))
# / 是浮点数真除法：不管是不是整数，它都会算出浮点数结果。例如 -13 / 5 = -2.6。
# // 是纯整数运算，精度无限。Python 的 // 规则是 “向下取整”（向负无穷取整）
# int() 是向零取整：int(-2.6) 会直接把小数点后面砍掉，变成 -2

class Solution(object):
    op_map = {'+': add, '-': sub, '*': mul, '/': div} 
    # 这是一个字典，左边是字符串符号，右边是实际的函数名。
    # 当 token 是 "+" 时，self.op_map["+"] 就会拿到 add 这个函数。
    # 当 token 是 "-" 时，拿到 sub 函数，以此类推。
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面. 这里非常关键的一点是参数顺序：op1 是栈里较深的的元素（被减数/被除数），op2 是栈顶弹出的元素（减数/除数），顺序不能乱。
                # 拿到函数后，紧接着的 (op1, op2) 就是在调用它。 假设 token 是 "+"，那么代码实际上就在执行：add(op1, op2)  等同于 op1 + op2
                # 最后，把函数算出来的结果（比如 3），再次压入栈顶，供后面的运算使用。
        return stack.pop()      
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

