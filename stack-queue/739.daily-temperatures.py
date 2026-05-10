#
# @lc app=leetcode id=739 lang=python3
# @lcpr version=30403
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (68.64%)
# Likes:    14734
# Dislikes: 376
# Total Accepted:    1.7M
# Total Submissions: 2.5M
# Testcase Example:  '[73,74,75,71,69,72,76,73]\n[30,40,50,60]\n[30,60,90]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
# 
# 
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
# 
# Constraints:
# 
# 
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 方法一: Brute force method. 时间复杂度：O(n^2); 总空间复杂度是O(n), 因为这里创建了一个长度为n的结果数组要存ans; 额外空间复杂度：O(1)，如果不把输出数组 ans 算进去。
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break # break 只跳出当前所在的最近一层循环。
        return ans
# 方法二: 单调栈
#  stack 存还没找到更高温度的下标。当前温度如果比栈顶那天高，就说明栈顶那天的答案找到了。答案 = 当前下标 - 栈顶下标。时间和空间复杂度是O(n)
class Solution:
    def dailyTemperatures(temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index

            stack.append(i)

        return ans

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

