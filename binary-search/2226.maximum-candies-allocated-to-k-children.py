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
class Solution:
    # TC: log(max(candies))
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if not candies:
            return 0
        
        # Initialize切割长度: start and end, end = min(max in L, sumL/k), 即min(所有木头中的最大值, 所有木头长度和/木头目标段数)
        start, end = 1, min(max(candies), sum(candies) // k)

        # if end < 1, it cannot complete the task, return 0
        if end < 1:
            return 0
        
        while start + 1 < end:
            mid = (start+end)//2
            # 长度为mid的木头总数 >=目标总数, 继续增长木头长度, 选右边
            if self.get_count(candies, mid) >= k:
                start = mid
            # 长度为mid的木头总数 < 目标总数, 继续缩短木头长度, 选左边
            else:
                end = mid
        
        # 因为之前排除了无解的情况, 所以这里一定有解, 非start即end
        # 如果end符合要求, 首选end因为end更长, 否则选start
        if self.get_count(candies, end) >= k:
            return end
        return start

    def get_count(self, candies, length):
        count = 0
        for wood in candies:
            pieces = wood // length
            count += pieces
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

