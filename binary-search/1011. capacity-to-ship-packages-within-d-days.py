#
# @lc app=leetcode id=1011 lang=python3
# @lcpr version=30403
#
# [1011] Capacity To Ship Packages Within D Days
#
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (73.96%)
# Likes:    11064
# Dislikes: 291
# Total Accepted:    783.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5\n[3,2,2,4,1,4]\n3\n[1,2,3,1,1]\n4'
#
# A conveyor belt has packages that must be shipped from one port to another
# within days days.
# 
# The i^th package on the conveyor belt has a weight of weights[i]. Each day,
# we load the ship with packages on the conveyor belt (in the order given by
# weights). We may not load more weight than the maximum weight capacity of the
# ship.
# 
# Return the least weight capacity of the ship that will result in all the
# packages on the conveyor belt being shipped within days days.
# 
# 
# Example 1:
# 
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in
# 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# 
# Note that the cargo must be shipped in the order given, so using a ship of
# capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6,
# 7), (8), (9), (10) is not allowed.
# 
# 
# Example 2:
# 
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in
# 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# 
# 
# Example 3:
# 
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= days <= weights.length <= 5 * 10^4
# 1 <= weights[i] <= 500
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 对于某一种运输分组方案，船的 capacity 等于这几天中“每天装载总重量”的最大值。
# 题目要找的是：在所有合法分组方案中，让这个最大值尽可能小。minimum possible maximum daily load 最小化“每天运输总重量”的最大值
# 按照原顺序，把 weights 分成最多 days 组，每组代表一天运输的包裹，求所有分组方案中，“最大组和”的最小值。公式化: minimize  max(第1天总重量, 第2天总重量, ..., 第days天总重量)
# 总结: 每个方案的 capacity 是当天总重量中的最大值；题目求的是所有合法方案中，这个最大值的最小可能值。
# TC: O(n * log(sum(weights)))
# SC: O(1), 未创建随输入大小增长的新数组或字典
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search based on ship capacity
        # 二分搜索的范围[max(weights), sum(weights)], 设s = sum(weights)-max(weights)+ 1, 所以二分查找的次数是O(log s), 一般可以简写为O(log(sum(weights)))
        start, end = max(weights), sum(weights)
        while start + 1 < end:
            mid = (start + end) // 2

            # 找最小可行 capacity：mid 可行，继续往左找更小的容量
            # 每次二分都调用这个函数, 该函数内需要遍历所有packages一次, TC=O(n), n = len(weights), 一共进行O(log s)次, 所以总共O(n* log s), 即O(n)*log(sum(weights))
            if self.canShip(weights, days, mid):
                end = mid
            else:
                # mid 不可行，必须增大容量
                start = mid

        # 找最小可行答案，所以先检查更小的 start
        # 最后额外调用一次canShip(), TC = O(n), 不会改变整体时间复杂度
        if self.canShip(weights, days, start):
            return start
        # end 从初始化开始就一定可行
        return end

    def canShip(self, weights: List[int], days: int, capacity: int) -> bool:
        day = 1 # 注意: day初始化为1而不是0
        current_load = 0
        
        for weight in weights:
            current_load += weight

            # 当前包裹放不进今天，开启新的一天
            if current_load > capacity:
                day += 1
                current_load = weight # 这里不用重置为0, 直接从该个weight重新开始加总计算

                # 已经超过规定天数，不需要继续计算, 可提前返回False
                if day > days:
                    return False
        return True
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#

