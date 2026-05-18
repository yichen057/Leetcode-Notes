#
# @lc app=leetcode id=42 lang=python3
# @lcpr version=30403
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (67.33%)
# Likes:    36495
# Dislikes: 702
# Total Accepted:    3.6M
# Total Submissions: 5.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]\n[4,2,0,3,2,5]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 核心思路: water[i] = min(l_max, r_max) - height[i]
# # 展开写: water[i] = min(
#     # 左边最高的柱子
#     max(height[0..i]),  
#     # 右边最高的柱子
#     max(height[i..end]) 
# ) - height[i]
# 如果定义含i or 不含 i：公式依然是 min(l_max, r_max) - height[i]。
# 为什么含 i 也没错？ 假设 height[i] 是整个数组最高的柱子：
# l_max 会等于 height[i]
# r_max 会等于 height[i]
# min(l_max, r_max) - height[i] = height[i] - height[i] = 0, 结果正确：最高柱子存不住水
# Method 1: Brute Force, but Time Limit Exceeded
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height) 
#         res = 0
#         for i in range(1, n - 1):
#             l_max, r_max = 0, 0
#             # find the max height on the right of i (不含 i)
#             for r in range(i+1, n):
#                 r_max = max(r_max, height[r])
#             # find the max height on the left of i (不含 i)
#             for l in range(i):
#                 l_max = max(l_max, height[l])
#             # 如果自己就是最高的话，
#             # l_max == r_max == height[i]
#             # 核心解法: 计算当前柱子能接的雨水
#             water = min(l_max, r_max) - height[i] 
#             if water > 0: # 只有当计算结果大于 0 时才累加
#                 res += water
#         return res
# 因为你的 l_max 和 r_max 不包含 height[i]。 如果 height[i] 比它左边和右边的最高柱子都要高（例如 height[i] 是一个峰值），那么 min(l_max, r_max) 就会小于 height[i]，导致 water 变成负数。
# 加上 if water > 0 就可以过滤掉这些情况，保证结果正确。
# 对比
# 下面方法二的写法：遍历范围包含 i，保证 l_max >= height[i] 且 r_max >= height[i]，所以 min(...) - height[i] 永远非负，不需要判断。
# 你的写法：遍历范围不含 i，可能出现 l_max < height[i] 的情况，所以需要手动判断。
# Method 2: still Time Limit Exceeded
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(1, n - 1):
            l_max, r_max = 0, 0
            # 找右边最高的柱子
            for j in range(i, n):
                r_max = max(r_max, height[j])
            # 找左边最高的柱子
            for j in range(i, -1, -1):
                l_max = max(l_max, height[j])
            # 如果自己就是最高的话，
            # l_max == r_max == height[i]
            res += min(l_max, r_max) - height[i]
        return res       
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

