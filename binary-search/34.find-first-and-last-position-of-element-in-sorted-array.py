#
# @lc app=leetcode id=34 lang=python3
# @lcpr version=30403
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (48.40%)
# Likes:    23297
# Dislikes: 645
# Total Accepted:    3.3M
# Total Submissions: 6.7M
# Testcase Example:  '[5,7,7,8,8,10]\n8\n[5,7,7,8,8,10]\n6\n[]\n0'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 方法一:
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         def binarySearch(find_left):
#             left, right = 0, len(nums) - 1
#             result = -1
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if nums[mid] == target: 
#                     result = mid
#                     if find_left:
#                         right = mid - 1
#                     else:
#                         left = mid + 1
#                 elif nums[mid] > target:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return result
#         return [binarySearch(True), binarySearch(False)]
# 方法二:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left = 第一个 >= target的index
        def lower_bound():
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        # right = 最后一个 <= target的index, 即第一个>target的index - 1
        def upper_bound():
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        left = lower_bound()
        if left ==len(nums) or nums[left] != target:
            return [-1, -1]
        right = upper_bound() - 1
        return [left, right]
 # @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

