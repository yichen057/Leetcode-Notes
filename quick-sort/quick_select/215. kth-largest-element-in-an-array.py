#
# @lc app=leetcode id=215 lang=python3
# @lcpr version=30403
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (68.95%)
# Likes:    18855
# Dislikes: 976
# Total Accepted:    3.7M
# Total Submissions: 5.3M
# Testcase Example:  '[3,2,1,5,6,4]\n2\n[3,2,3,1,2,4,5,5,6]\n4'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
# 
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
# 
# Can you solve it without sorting?
# 
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# quick select: 平均时间复杂度O(n), 最差时间复杂度O(n^2), 空间复杂度O(logn), 只递归包含答案的range, 不断partition缩小范围: 三个范围: >pivot, <pivot, ==pivot
# 而quickl sort两边都找, >=pivot, <=pivot
# Quick Select 比 Quick Sort 快. 因为它只递归一边, 而不是两边都递归
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums: List[int], start: int, end: int, k: int) -> int:
        if start == end:
            return nums[start] # 注意: 这里返回的不是index: start. 而是返回元素: nums[start]
        
        left = start
        right = end
        pivot = nums[(left+right)//2]

        while left <= right:
            while left <= right and nums[left] > pivot:# 此处从大小排序, 注意这里的左边区间是大于pivot而不是小于pivot. 这里是降序数组
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            
            if left <= right: # 注: 这个 if left <= right: 应该在外层 while left <= right: 里面。否则如果 nums[left] 和 nums[right] 都不能移动，外层 while 会一直卡住，导致 TLE(time limit exceeded)。
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # 此时partition结束, right > left, 分区后有三个区域: 下面的target指的是第k大元素的index
        # [start...right]            > pivot    当target <= right, 答案在right左边
        # [right + 1...left - 1]    == pivot    当right < target < left, 答案在==pivot中间
        # [left...end]               < pivot    当target >= left, 答案在left右边

        # 降序数组中的第k大的index: target = start + k - 1
        target = start + k - 1
        # 1) > pivot区间, 左边
        if target <= right:# 注意: 这里是小于等于号, 并非小于号
            return self.quickSelect(nums, start, right, k)
        # 2) < pivot区间, 右边
        if target >= left:
            return self.quickSelect(nums, left, end, k - (left-start)) 
            # 这里的k-(left-start)是将全局排名转为局域排名: k是在全局数组里的第k大, 转为右边局域区间数组的第[k-(left-start)]大
        # 3) == pivot区间, 中间
        return nums[right + 1] # right + 1是 == pivot区域内的第一个元素的index


       
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,2,1,5,6,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,1,2,4,5,5,6]\n4\n
# @lcpr case=end

#

