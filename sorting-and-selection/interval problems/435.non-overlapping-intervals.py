#
# @lc app=leetcode id=435 lang=python3
# @lcpr version=30403
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (57.17%)
# Likes:    9194
# Dislikes: 261
# Total Accepted:    1M
# Total Submissions: 1.8M
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]\n[[1,2],[1,2],[1,2]]\n[[1,2],[2,3]]'
#
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.
# 
# Note that intervals which only touch at a point are non-overlapping. For
# example, [1, 2] and [2, 3] are non-overlapping.
# 
# 
# Example 1:
# 
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 本题需和LC56题目有所区别: Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping. 在56题里这种情况是属于重合情况的, 因此overlap定义为: start < lastEnd, 而非<=.
# LC56: 重叠->合并->保留更大的 end, 所以max(lastEnd,end)
# LC435: 重叠->必须删一个->保留更小的 end, 所以min(prevEnd,end)
# 以上是这两题最核心的区别。
# method 1: length difference method, LC56题方法的延伸变种!
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        output = [intervals[0]] # 注意这里初始化, intervals[0]外还有一个[], 合并后还是个list of list
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start < lastEnd:
                # 遇到重叠，删除一个，保留结束更早的
                output[-1][1] = min(lastEnd, end) # output: [[1, 2], [2, 3], [3, 4]], 因为本题要找的是return the minimum number of intervals to remove, 实际可以转换为希望保留尽可能多的 intervals，所以删除数才会最少, 目标是make the rest non-overlapping. 
                # 注意: max 是 LC56 合并区间用的；min 是 LC435 删除重叠用的。
                # output[-1][1] = max(lastEnd, end) # 错误示范! ❌ output: [[1, 3], [3, 4]]
            else:
                output.append([start, end])
        print("output:",output)
        return len(intervals) - len(output)
# method 2: count method, 推荐该方法!
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < lastEnd: # overlapping
                count += 1
                lastEnd = min(lastEnd, end) # 遇到重叠，删除一个，保留结束更早的
            else: # non-overlapping, just update the lastEnd value
                lastEnd = end
        return count

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[1,2],[2,3],[3,4],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,2],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3]]\n
# @lcpr case=end

#

