#
# @lc app=leetcode id=1672 lang=python3
# @lcpr version=30400
#
# [1672] Richest Customer Wealth
#
# https://leetcode.com/problems/richest-customer-wealth/description/
#
# algorithms
# Easy (88.67%)
# Likes:    4845
# Dislikes: 389
# Total Accepted:    1.2M
# Total Submissions: 1.4M
# Testcase Example:  '[[1,2,3],[3,2,1]]\n[[1,5],[7,3],[3,5]]\n[[2,8,7],[7,1,3],[1,9,5]]'
#
# You are given an m x n integer grid accounts where accounts[i][j] is the
# amount of money the i​​​​​^​​​​​​th​​​​ customer has in the
# j​​​​​^​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# 
# A customer's wealth is the amount of money they have in all their bank
# accounts. The richest customer is the customer that has the maximum
# wealth.
# 
# 
# Example 1:
# 
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return
# 6.
# 
# 
# Example 2:
# 
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
# 
# Example 3:
# 
# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17
# 
# 
# 
# Constraints:
# 
# 
# m == accounts.length
# n == accounts[i].length
# 1 <= m, n <= 50
# 1 <= accounts[i][j] <= 100
# 
# 
#

import sys
import os

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

# @lc code=start
# ### 1. 题目大意
# 给你一个 $m \times n$ 的整数网格 `accounts`，其中：
# - `accounts[i]` 代表第 `i` 位客户。
# - `accounts[i][j]` 代表第 `i` 位客户在第 `j` 家银行存的钱。
# **任务**：算出每位客户在所有银行的存款总和（即总资产），并返回**最富有**的那位客户拥有的资产数额。
# ### 2. 解题思路: 这道题的核心是 **2D Array Traversal（二维数组遍历）**，但比周长那题简单，因为它不需要考虑邻居关系，只需要累加。
# 1. **外层循环**：遍历每一位客户（即每一行）。
# 2. **内层操作**：计算该客户当前所有银行存款的总和 `sum(customer_accounts)`。
# 3. **全局更新**：维护一个变量 `max_wealth`，如果当前客户的资产比 `max_wealth` 大，就更新它。
class Solution:
    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     # 方法一: 用索引写嵌套循环, 不推荐
    #     max_sum = 0      
    #     for i in range(len(accounts)):
    #         current_customer_sum = 0 # 重点! 每换一个客户, 清空当前累加值

    #         for j in range(len(accounts[i])):
    #             current_customer_sum += accounts[i][j]
    #         if current_customer_sum> max_sum:
    #             max_sum = current_customer_sum
    #     return max_sum
    # 方法二: 无索引写嵌套循环, 推荐. 时间复杂度O(m*n)
    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     max_sum = 0
    #     for customer in accounts: # 无需索引, 直接写
    #         current_customer_sum = 0 # 重点! 每换一个客户, 清空当前累加值
    #         for money in customer: 
    #             current_customer_sum += money
    #         if current_customer_sum> max_sum: # 后面和第一个方法代码一样
    #              max_sum = current_customer_sum
    #     return max_sum
    # 方法三: 使用max()和sum()内置函数
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for customer in accounts:
            # 使用内置 sum() 函数直接算出一行的总和
            current_wealth = sum(customer)
            max_sum = max(max_sum, current_wealth)
        return max_sum

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[1,2,3],[3,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5],[7,3],[3,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,8,7],[7,1,3],[1,9,5]]\n
# @lcpr case=end

#

