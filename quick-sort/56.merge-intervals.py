#
# @lc app=leetcode id=56 lang=python3
# @lcpr version=30403
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (51.89%)
# Likes:    24741
# Dislikes: 909
# Total Accepted:    4M
# Total Submissions: 7.8M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]\n[[1,4],[4,5]]\n[[4,7],[1,4]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# Example 3:
# 
# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else:
                output.append([start, end])
        
        return output

# Time complexity : O(nlogn)
# 1) 排序 intervals.sort() → O(n log n)
# 2) 后面那个 for 循环,从头到尾扫一遍 → O(n)
# 加起来是 O(n log n) + O(n)。复杂度相加时只保留增长最快的那一项,n log n 比 n 大,所以总的算 O(n log n)。
# Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(nlogn) complexity of sorting.

# Space complexity : O(logN) (or O(n))
# 先解决一个最容易误会的点:output 数组不算进去!
# 你大概会想:"output 最多存 n 个区间,这不就 O(n) 了吗?" 但算法分析里,空间复杂度一般指辅助空间 / 额外空间 = 除了"输入"和"输出"之外、你自己额外开的空间。output 是题目要求你必须返回的答案,属于"输出",按惯例不计入。
# 所以真正要数的额外空间只剩两块:
# 1) 循环里那几个变量 lastEnd / start / end → O(1) 常数,忽略;
# 2) 排序算法自己内部用掉的空间 ← 唯一的大头。
# 也就是说,整道题的空间复杂度,完全由"你用的排序是怎么实现的"决定。
# Python 的 list.sort() 用的是 Timsort,最坏情况要 O(n) 辅助空间,所以你这份 Python 代码严格说空间是 O(n);C++ 的 std::sort 是 O(log n)。面试时直接报"时间 O(n log n),空间 O(log n) 或 O(n)、取决于排序实现"就稳了,这样答还能顺带秀一下你懂底层。
# If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) # 时间复杂度: O(n log n)
        # 先排序的原因是: 按每个区间的开始值从小到大排。排好之后,有个很爽的保证:能重叠的区间一定是挨着的。所以我们只需要拿"新区间"和"结果里最后一个区间"比较就够了,不用回头看前面的。
        output = [intervals[0]] # 这是一个装着区间的列表. 为什么要先把第一个区间塞进去?因为后面的逻辑是"拿新区间去和结果里最后一个比",总得先有一个东西可比吧,所以把第一个当"种子"先放进去。
        for start, end in intervals[1:]: # 时间复杂度: O(n)
            lastEnd = output[-1][1] # 结果列表里的最后一个区间, [1] = 这个区间的结束值/右端点(索引 0 是开始,1 是结束)

            # 当判断出重叠时(start <= lastEnd),要把最后一个区间的右端点往右伸长。
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd) # 为什么用 max 而不是直接 = end? 因为新区间有可能整个被"包"在里面
            else:
                output.append([start, end])
        return output

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,7],[1,4]]\n
# @lcpr case=end

#

