#
# @lc app=leetcode id=875 lang=python3
# @lcpr version=30403
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (50.03%)
# Likes:    13801
# Dislikes: 923
# Total Accepted:    1.6M
# Total Submissions: 3.2M
# Testcase Example:  '[3,6,7,11]\n8\n[30,11,23,4,20]\n5\n[30,11,23,4,20]\n6'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
# 
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
# 
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
# 
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
# 
# 
# Example 1:
# 
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# 
# 
# Example 2:
# 
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# 
# 
# Example 3:
# 
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# TC: O(n * log m)
# SC: O(1)
# n = len(piles), m = max(piles)
#   这里二分的不是数组下标，而是 Koko 的吃香蕉速度 speed。
# * 最小速度：1
# * 最大速度：max(piles)，因为每小时吃完最大的一堆已经足够快
# * canFinish(speed)：用这个速度，能否在 h 小时内吃完
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search based on speed (k)
        start, end = 1, max(piles)

        while start + 1 < end:
            mid = (start + end) // 2

            # 找最小可行速度：如果 mid 速度已经可以吃完，继续往左找更小的速度
            if self.canFinish(piles, h, mid):
                end = mid
            else:
                # mid 速度太慢，必须提高速度，往右找
                start = mid
        
        # 找最小可行答案，所以先检查更靠左的 start
        if self.canFinish(piles, h, start):
            return start
        if self.canFinish(piles, h, end):
            return end 
        return -1
    
    def canFinish(self, piles: List[int], h: int, speed: int) -> bool:
        total_hours = 0
        for banana in piles:
            # 吃完当前这一堆需要的小时数：ceil(bananas / speed), 两数相除结果向上取整
            hours = (banana + speed - 1) // speed
            total_hours += hours
        return total_hours <= h
        

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

