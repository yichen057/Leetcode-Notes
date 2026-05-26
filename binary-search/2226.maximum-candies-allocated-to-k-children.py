#
# @lc app=leetcode id=2226 lang=python3
# @lcpr version=30403
#
# [2226] Maximum Candies Allocated to K Children
#
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
#
# algorithms
# Medium (49.88%)
# Likes:    1843
# Dislikes: 86
# Total Accepted:    207.7K
# Total Submissions: 416.3K
# Testcase Example:  '[5,8,6]\n3\n[2,5]\n11'
#
# You are given a 0-indexed integer array candies. Each element in the array
# denotes a pile of candies of size candies[i]. You can divide each pile into
# any number of sub piles, but you cannot merge two piles together.
# 
# You are also given an integer k. You should allocate piles of candies to k
# children such that each child gets the same number of candies. Each child can
# be allocated candies from only one pile of candies and some piles of candies
# may go unused.
# 
# Return the maximum number of candies each child can get.
# 
# 
# Example 1:
# 
# Input: candies = [5,8,6], k = 3
# Output: 5
# Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and
# candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of
# sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children.
# It can be proven that each child cannot receive more than 5 candies.
# 
# 
# Example 2:
# 
# Input: candies = [2,5], k = 11
# Output: 0
# Explanation: There are 11 children but only 7 candies in total, so it is
# impossible to ensure each child receives at least one candy. Thus, each child
# gets no candy and the answer is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candies.length <= 10^5
# 1 <= candies[i] <= 10^7
# 1 <= k <= 10^12
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
from typing import List

class Solution:
    # n = len(candies)
    # U = min(max(candies), sum(candies) // k)，表示每个孩子最多可能分到的糖果数
    # TC: O(n * log U)
    # SC: O(1)
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if not candies:
            return 0

        # 二分的对象不是数组下标，而是：
        # 每个孩子可以得到的糖果数量 amount

        # 每个孩子最少尝试分 1 颗糖
        start = 1

        # 每个孩子最多能分到的糖果数有两个限制：
        # 1. 不能超过某一堆糖的最大数量，因为不能把不同糖果堆合并给一个孩子
        # 2. 不能超过所有糖果总数平均分给 k 个孩子的数量
        end = min(max(candies), sum(candies) // k)

        # 如果总糖果数连每个孩子 1 颗都无法满足，那么答案就是 0
        # 这个判断很重要不能忽略, 否则通不过
        if end < 1:
            return 0

        while start + 1 < end:
            mid = (start + end) // 2

            # 判断：如果每个孩子分 mid 颗糖，
            # 最多能够满足多少个孩子
            child_count = self.get_child_count(candies, mid)

            if child_count >= k:
                # mid 可行：
                # 至少可以满足 k 个孩子
                # 但题目要求每个孩子尽可能多拿糖，
                # 所以继续往右找更大的可行 amount
                # 普通情况如果是找第一个xxx这里应该是end = mid, 但是本题是找最大
                start = mid
            else:
                # mid 不可行：
                # 每个孩子分 mid 颗时，无法满足 k 个孩子
                # 说明 amount 太大，需要往左找更小的 amount
                end = mid

        # 循环结束后，只剩下 start 和 end 两个候选答案。
        # 本题要找最大的可行 amount，所以先检查更大的 end。
        if self.get_child_count(candies, end) >= k:
            return end

        return start

    def get_child_count(self, candies: List[int], amount: int) -> int:
        # count 表示：
        # 如果每个孩子得到 amount 颗糖，
        # 所有糖果堆最多可以满足多少个孩子
        count = 0

        for pile in candies:
            # 当前这一堆糖，最多可以分给多少个孩子
            children = pile // amount
            count += children

        return count

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [5,8,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,5]\n11\n
# @lcpr case=end

#

