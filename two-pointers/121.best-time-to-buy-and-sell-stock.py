#
# @lc app=leetcode id=121 lang=python3
# @lcpr version=30403
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (56.76%)
# Likes:    35797
# Dislikes: 1423
# Total Accepted:    8M
# Total Submissions: 14.1M
# Testcase Example:  '[7,1,5,3,6,4]\n[7,6,4,3,1]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
# 
# 
# Example 1:
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
# 
# 
# Example 2:
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
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
    # Method 1: Brute force
    # TC: O(n^2) 展开是O(n * (n-1)); SC: O(1)
    # i = 0, j 跑 n-1 次
    # i = 1, j 跑 n-2 次
    # i = 2, j 跑 n-3 次
    # ...
    # i = n-2, j 跑 1 次
    # 所以总次数是：(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2
    # 所以总的时间复杂度是O(n(n - 1) / 2), 去掉常数和低阶项以后，就是：O(n^2)
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxP:
                    maxP = profit
        return maxP
    # Method 2: Two pointer
    # TC: O(n); SC: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            # profitable investment:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > maxP:
                    maxP = profit
            else: # nonprofitable, update the left pointer to the lower value cus we want to buy low
                l = r
            r += 1 # update the right pointer
        return maxP
                

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

