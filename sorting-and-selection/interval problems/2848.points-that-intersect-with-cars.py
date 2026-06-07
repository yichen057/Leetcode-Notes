#
# @lc app=leetcode id=2848 lang=python3
# @lcpr version=30403
#
# [2848] Points That Intersect With Cars
#
# https://leetcode.com/problems/points-that-intersect-with-cars/description/
#
# algorithms
# Easy (73.41%)
# Likes:    380
# Dislikes: 37
# Total Accepted:    77.7K
# Total Submissions: 105.8K
# Testcase Example:  '[[3,6],[1,5],[4,7]]\n[[1,3],[5,8]]'
#
# You are given a 0-indexed 2D integer array nums representing the coordinates
# of the cars parking on a number line. For any index i, nums[i] = [starti,
# endi] where starti is the starting point of the i^th car and endi is the
# ending point of the i^th car.
# 
# Return the number of integer points on the line that are covered with any
# part of a car.
# 
# 
# Example 1:
# 
# Input: nums = [[3,6],[1,5],[4,7]]
# Output: 7
# Explanation: All the points from 1 to 7 intersect at least one car, therefore
# the answer would be 7.
# 
# 
# Example 2:
# 
# Input: nums = [[1,3],[5,8]]
# Output: 7
# Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8.
# There are a total of 7 points, therefore the answer would be 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# nums[i].length == 2
# 1 <= starti <= endi <= 100
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 对于 LC2848 这道题本身：Set method(method 2)解法更优; 但对于面试能力提升, merge interval method 1 解法更有价值

# Method 1:
# 本题可以看成LC56题的follow-up: 先做区间合并, 再把每个区间的长度加起来
# LC56：
# Merge Intervals
# 目标：得到新区间

# LC2848：
# 排序+ Merge Intervals + 求长度
# 目标：得到覆盖点数
# TC: O(n log n)
# SC : O(logN) (or O(n))
# 1) 循环里那几个变量 lastEnd / start / end → O(1) 常数,忽略;
# 2) 排序算法自己内部用掉的空间 ← 唯一的大头。
# 整道题的空间复杂度,完全由"你用的排序是怎么实现的"决定。
# Python 的 list.sort() 用的是 Timsort,最坏情况要 O(n) 辅助空间,所以你这份 Python 代码严格说空间是 O(n);C++ 的 std::sort 是 O(log n)。面试时直接报"时间 O(n log n),空间 O(log n) 或 O(n)、取决于排序实现"就稳了,这样答还能顺带秀一下你懂底层。
# If we can sort intervals in place, we do not need more than constant additional space, although the sorting itself takes O(logn) space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x:x[0]) # Sorting TC: O(n log n)
        output = [nums[0]]
        
        for start, end in nums[1:]: # merge: O(n)
            lastEnd = output[-1][1]
            if start<=lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        length = 0
        for start, end in output:
            length += end - start + 1

        return length
# method 2: brute force set method 且数据量小: 1 <= start <= end <= 100
# 时间和空间复杂度: O(100) = O(1); 或者说O(M), where M <= 100
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for x in range (start, end + 1):
                covered.add(x)
        return len(covered)                      
    
       
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [[3,6],[1,5],[4,7]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,8]]\n
# @lcpr case=end

#

