#
# @lc app=leetcode id=57 lang=python3
# @lcpr version=30403
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (45.29%)
# Likes:    11910
# Dislikes: 923
# Total Accepted:    1.8M
# Total Submissions: 4M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]\n[[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
# 
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
# 
# Return intervals after the insertion.
# 
# Note that you don't need to modify intervals in-place. You can make a new
# array and return it.
# 
# 
# Example 1:
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# method 1: binary search + merge
# insert the newInterval using binary search based on the start element and merge the overlapping intervals by comparing the end of the last inerval with the start of the new interval
# Binary Search: O(log n)
# Insert: O(n): 因为intervals.insert(...) 本身是 O(n)，因为后面的元素要整体后移。
# Merge: O(n):  插入后还要再 merge 一遍，也是 O(n)。
# Total Time: O(n), 所以二分没有真正降低总复杂度。代码比三段式更绕，边界更容易错。
# Space: O(n): 如果不算返回结果空间，额外空间是 O(n)，因为你用了 output。
# 完整重叠判断是：lastStart <= newEnd and newStart <= lastEnd, 而在merge loop里, 数组已经按start排序, 所以一定有lastStart<=start, 区间本身一定有start<=end, 所以可以推出lastStart <= newEnd, 也就是完整判断的第一半, 所以只需判断另一半: newStart <= lastEnd.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        start, end = 0, len(intervals)-1

        while start + 1 < end:
            mid = (start+end) // 2
            if intervals[mid][0] >= newInterval[0]:
                end = mid
            else:
                start = mid
        # 结束后start和end都有可能答案, 因为是要插到第一个>=target的前面, 所以先判断start, 再判断end
        # 此时start + 1>= end, 其实就两种可能: start + 1 == end, 和 start == end
        if intervals[start][0] >= newInterval[0]: # 插到第一个 >= target 的前面, 更好理解, 如果用<=, 表示插到最后一个 <= target 的后面
            intervals.insert(start, newInterval)
        elif intervals[end][0] >= newInterval[0]:
            intervals.insert(end, newInterval)
        else:
            intervals.insert(end+1, newInterval)
        
        print("intervals after insersion",intervals)
        
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(end,lastEnd) # 注: 这里lastStart <= start已成立, 因为前面已经排序, 所以无需再对output[-1][0]判断min(lastStart, start) = lastStart永远成立
            else:
                output.append([start, end])
        return output
    
# method 2: 三段式扫描数组(面试和刷题更推荐 Method 2。因为intervals 按 start 升序排列，且彼此不重叠)
# 时间复杂度：O(n): 因为Scan all intervals once: O(n)
# 空间复杂度：O(n)。因为Result array: O(n), 如果不算输出数组，额外空间可以认为是 O(1)。
# 左边区间->重叠区间->右边区间, 三个连续区域
# 第一阶段(收集所有在 newInterval 左边、且不重叠的区间): i < n and intervals[i][1] < newInterval[0]:只要还在左边区域, 就一直收集
# 第一阶段结束时, i自动停在第二阶段起点, 第一阶段结束后已经保证：curEnd >= newStart, 即newStart <= curEnd
# 第二阶段(merge所有和 newInterval 重叠的区间): while i < n and intervals[i][0] <= newInterval[1]:
# 第三阶段(收集所有在 newInterval 右边、且不重叠的区间): while i < n:
# eg: [1,2] | [3,5] [6,7] [8,10] | [12,16]
           #与newInterval[4, 8]重叠

# 判断重叠的完整条件: newStart <= lastEnd and lastStart <= newEnd
# 此处用while是因为需要一直往前走, 直到条件失效; 而for循环是用来把所有元素都看一遍
# 另外注意本题的intervals是按start升序排列
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
         # 1. 收集所有在 newInterval 左边、且不重叠的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1 # 注意要移动指针
        # 2. 合并所有和 newInterval 重叠的区间
        # 此时i自动停在第二阶段起点, 第一阶段结束后已经保证：lastEnd >= newStart, 即newStart <= lastEnd, 所以判断重叠区间只需判断另外一部分: lastStart <= newEnd:
        while i < n and intervals[i][0] <= newInterval[1]: # merge类问题, 这里如果start == lastEnd, 接触也算重叠, 所以需要把等号的情况也考虑在内, 不只是<
            newInterval[0] = min(newInterval[0], intervals[i][0]) # 注意此处更新的是newInterval, 不是intervals[i]
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval) # 注意要在这一轮while循环走完后再res.append()

        # 3. 收集所有在 newInterval 右边、且不重叠的区间
        while i< n:
            res.append(intervals[i])
            i += 1
        
        return res

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#

