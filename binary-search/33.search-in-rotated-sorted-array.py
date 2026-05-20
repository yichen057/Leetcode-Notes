#
# @lc app=leetcode id=33 lang=python3
# @lcpr version=30403
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (44.47%)
# Likes:    30105
# Dislikes: 1833
# Total Accepted:    4.4M
# Total Submissions: 10M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0\n[4,5,6,7,0,1,2]\n3\n[1]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly left rotated at an
# unknown index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# search in a rotated sorted array
# 本题找target index, 但数组被旋转过
# 数组不是整体有序, 而是每次二分, 左半边or右半边至少有一边有序

# 方法一: 推荐!
# 先按照LC153题利用二分法找最小值, 其次再根据target确定它在左上还是右下区间后, 再次利用二分法找目标值
# followup: 也可以用一次二分去做
# 把数组按值的大小可以分为几种区间情况: 中>尾>头; 尾>头>中(已包含头>中>尾的情况).
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
          
           # 1. 中>尾>头: 如果mid在[中>尾]区间(即左上方)
            if nums[mid] > nums[end]:
                # 1) target在中区
                if nums[start] <= target <= nums[mid]:
                    end = mid
                # 2) target在尾部or头部
                else:
                    start = mid

            # 2. 尾>头>中: 如果mid在[头>中]区间(即右下方), 这部分同时包含了 头> 中> 尾
            else:
                # target在中区 
                if nums[mid] <= target <= nums[end]:
                    start = mid
                # target在尾部or头部
                else:
                    end = mid
        print("start:",start, "end:", end)
        # 在无重复数据中寻找target, 先判断start或end都可以
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

# 方法二:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            # 左半边有序
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # 右半边有序
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

