#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (58.42%)
# Likes:    11532
# Dislikes: 1601
# Total Accepted:    2.1M
# Total Submissions: 3.5M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
# 
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# 
# 
# Return true if n is a happy number, and false if not.
# 
# 
# Example 1:
# 
# 
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()     # setup an empty list to store the square of each digit
        while n!= 1:
            for i in str(n): # int n -> str n to traverse it.
                square = int(i) ** 2 # str i -> int i to square itself
                seen.append(square)
            n = sum(seen) # sum up all the squares of element in the list
            # n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            seen.append(n)
        return True

class Solution:
    def isHappy(self, n: int) -> bool:
        # 判环的两个方法: 用集合或快慢指针检测, 检测是否出现过相同状态. 
        # 环指的是某个状态重复出现, 程序进入循环. 判环是为了防止无限循环, 题目类型包括快乐数, 链表检测, dfs, 图的遍历等
        # 方法一: 用集合set记录所有出现过的数: 先判断当前n有没有出现过, 没有出现过再把它加进集合记录下来, 然后计算下一轮的n, 即新的平方和sum(int(i) ** 2 for i in str(n))
        seen = set() # 用集合set记录所有出现过的平方和结果n
        while n != 1: # 每次计算新的n之前, 先检查它是否出现过
            if n in seen: # Cycle Detection: 如果n 重复出现, 说明形成了环陷入了循环, 不是快乐数
                return False
            seen.add(n) # 第一次出现的数字都加入集合; 一旦有数字第二次出现, 意味着进入了一个循环

            # 计算下一轮的n: 把每一位平方后求和
            # 第一种简写法
            # n = sum(int(i) ** 2 for i in str(n))
            # 第二种展开写法
            total = 0
            for ch in str(n):
                total += int(ch) ** 2
            n = total

        return True
    
        # 方法二: 快慢指针
        # 计算每位平方和
        def next_number(num:int) -> int: # 这只是一个小工具函数，负责计算“下一步的平方和”：
            return sum(int(i) ** 2 for i in str(num))
        
        # 初始化快慢指针
        slow = n
        fast = next_number(n)

        # 快指针走两步, 慢指针走一步
        # 当fast == 1: 到达快乐数; slow == fast: 说明陷入循环, 不是快乐数
        while fast != 1 and slow != fast:
            slow = next_number(slow) # 慢走一步, 算一次平方和
            fast = next_number(next_number(fast)) # 快走两步, 算两次平方和

        return fast == 1 # 如果fast == 1, 说明是快乐数
        
# @lc code=end

