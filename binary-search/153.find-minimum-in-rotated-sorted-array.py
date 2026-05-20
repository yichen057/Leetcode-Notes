#
# @lc app=leetcode id=153 lang=python3
# @lcpr version=30403
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (54.68%)
# Likes:    15502
# Dislikes: 676
# Total Accepted:    3.1M
# Total Submissions: 5.7M
# Testcase Example:  '[3,4,5,1,2]\n[4,5,6,7,0,1,2]\n[11,13,15,17]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might
# become:
# 
# 
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# 
# 
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# 
# Given the sorted rotated array nums of unique elements, return the minimum
# element of this array.
# 
# You must write an algorithm that runs in O(log n) time.
# 
# 
# Example 1:
# 
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# 
# 
# Example 2:
# 
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4
# times.
# 
# 
# Example 3:
# 
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4
# times. 
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 本题最好通过画图的形式去理解
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 特殊情况处理, 需要跟面试官确认特殊情况的返回值
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # this step can be ignored!
            # if nums[mid] < nums[mid+1] and nums[mid] < nums[mid - 1]:
            #     return nums[mid] 
            # 如果mid > end, 起点在右边, 抛弃左边
            if nums[mid] > nums[end]: #注意, 这里nums[mid]不和相邻的值比较, 而是和nums[end]比较
                start = mid
            # 如果mid < end, 起点在左边, 抛弃右边
            # 注意: 题目声明不存在相等元素, 所以这里else, 等价于mid < end
            else:
                end = mid
        # debug 用的
        # print("start:", start, ", end:", end, ", nums[start]:", nums[start], ", nums[end]:", nums[end])
        # 返回start和end指向的最小值
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]
        # 或者直接用min()去取最小值
        # return min(nums[start], nums[end])
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end

#

