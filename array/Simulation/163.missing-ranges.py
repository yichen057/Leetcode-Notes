#
# @lc app=leetcode id=163 lang=python3
# @lcpr version=30400
#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Easy (35.53%)
# Likes:    1181
# Dislikes: 3021
# Total Accepted:    307.1K
# Total Submissions: 864.2K
# Testcase Example:  '[0,1,3,50,75]\n0\n99\n[-1]\n-1\n-1'
#
# You are given an inclusive range [lower, upper] and a sorted unique integer
# array nums, where all elements are within the inclusive range.
# 
# A number x is considered missing if x is in the range [lower, upper] and x is
# not in nums.
# 
# Return the shortest sorted list of ranges that exactly covers all the missing
# numbers. That is, no element of nums is included in any of the ranges, and
# each missing number is covered by one of the ranges.
# 
# 
# 
# 
# Example 1:
# 
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]
# Explanation: The ranges are:
# [2,2]
# [4,49]
# [51,74]
# [76,99]
# 
# 
# Example 2:
# 
# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing
# numbers.
# 
# 
# 
# Constraints:
# 
# 
# -10^9 <= lower <= upper <= 10^9
# 0 <= nums.length <= 100
# lower <= nums[i] <= upper
# All the values of nums are unique.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 本题是考察区间处理和边界逻辑的经典面试题。
# 难度：Easy-Medium (简单偏中等)
# 类型：Arrays (数组) / Interval (区间)
# 解析：这道题比普通的数组遍历要难一些，因为它涉及到“状态同步”。你需要维护一个 next_expected 变量，并处理数组首尾的边界情况。在 LeetCode 中，这类涉及合并或寻找区间的题目非常经典。
# 题意：给定一个范围 [lower, upper] 和一个已经存在的线索列表 clues，找出这个范围内所有缺失的数字，并以“区间”的形式返回。
# Understand：
# 输入：clues = [0, 1, 3, 50, 75], lower = 0, upper = 99
# 输出：[[2, 2], [4, 49], [51, 74], [76, 99]]
# 注意：如果缺失的是单个数字，区间就是 [x, x]。
# Plan：
# 为了方便处理，先将 clues 排序。
# 设定一个指针 next_expected = lower，代表我们目前期待看到的最小数字。
# 遍历 clues 中的每个数字 c：
# 如果 c > next_expected，说明 next_expected 到 c - 1 这一段都丢了。记录区间 [next_expected, c - 1]。
# 更新 next_expected = c + 1。
# 收尾工作：循环结束后，如果 next_expected <= upper，说明最后还有一段缺失，记录 [next_expected, upper]。
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums.sort()
        missing_ranges=[]
        next_expected = lower

        for c in nums:
            if c > next_expected:
                missing_ranges.append([next_expected, c-1])
            next_expected = c + 1 # 注: 一定要更新next_expected指针! 否则它永远指向lower

        # 这一步也不能忘了, 循环结束后, 最后一段upper以内, nums以外的整数也得包含
        if next_expected <= upper:
            missing_ranges.append([next_expected, upper])
        
        return missing_ranges
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [0,1,3,50,75]\n0\n99\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n-1\n-1\n
# @lcpr case=end

#

