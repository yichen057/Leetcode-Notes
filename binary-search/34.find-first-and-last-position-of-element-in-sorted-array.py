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
# from common.node import *

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
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # left = 第一个 >= target的index
#         def lower_bound():
#             lo, hi = 0, len(nums)
#             while lo < hi:
#                 mid = (lo + hi) // 2
#                 if nums[mid] < target:
#                     lo = mid + 1
#                 else:
#                     hi = mid
#             return lo
#         # right = 最后一个 <= target的index, 即第一个>target的index - 1
#         def upper_bound():
#             lo, hi = 0, len(nums)
#             while lo < hi:
#                 mid = (lo + hi) // 2
#                 if nums[mid] <= target:
#                     lo = mid + 1
#                 else:
#                     hi = mid
#             return lo
#         left = lower_bound()
#         if left ==len(nums) or nums[left] != target:
#             return [-1, -1]
#         right = upper_bound() - 1
#         return [left, right]
# 方法三: 按模板写, 推荐!
class Solution:
    # TC: O(log n)
    # SC: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 边界判断删掉了not target in numSet: 是因为是否存在target, 让二分自己判断即可
        if not nums:
            return [-1, -1]
        # def lowerBound():
        #     start, end = 0, len(nums) -1
        #     while start + 1 < end:
        #         mid = (start + end) // 2
        #         if nums[mid] >= target: # find the starting position of target, 往左找
        #             end = mid
        #         else:
        #             start = mid
        #     if nums[start] == target:
        #         return start
        #     if nums[end] == target:
        #         return end
        #     return -1
        # def upperBound():
        #     start, end = 0, len(nums) -1
        #     while start + 1 < end:
        #         mid = (start + end) // 2
        #         if nums[mid] <= target: # find the ending position of target, 往右找
        #             start = mid
        #         else:
        #             end = mid
        #     if nums[end] == target:
        #         return end
        #     if nums[start] == target:
        #         return start
        #     return -1
        # return [lowerBound(), upperBound()]
# 上述lowerBound() 和 upperBound() 主要只有两处不同：
# 1. 循环中，等于 target 时往左找还是往右找；
# 2. 循环结束后，先检查 start 还是先检查 end。
# 因此可以合并成一个辅助函数，用参数 find_first 控制查找方向：
        def findBound(findFirst: bool) -> int:
            start, end = 0, len(nums) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if findFirst:
                    # 找第一个target:往左找
                    # nums[mid] == target 时，继续往左找
                    if nums[mid] >= target:
                        end = mid
                    else:
                        start = mid
                else:
                    # 找最后一个target: 往右找
                    # nums[mid] == target 时，继续往右找
                    if nums[mid] <= target:
                        start = mid
                    else:
                        end = mid
            
            if findFirst:
                # 找最左边的target, 所以先检查start
                if nums[start] == target:
                    # print("最左边的target, start:", start)
                    return start
                if nums[end] == target:
                    # print("最左边的target, end:", end)
                    return end
            else:
                # 找最右边的target, 所以先检查end
                if nums[end] == target:
                    # print("最右边的target, end:", start)
                    return end
                if nums[start] == target:
                    # print("最右边的target, start:", start)
                    return start

            return -1

        first = findBound(True)
        # 如果没有找到第一个 target，说明 target 不存在，不需要继续寻找最后一个 target
        if first == -1:
            return [-1, -1]
        # print("first:",first)
        last = findBound(False)
        # print("last:",last)
        return [first, last]
                
 # @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    # 用例1: 有多个target, expected output: [3, 4]
    nums1 = [5, 7, 7, 8, 8, 10] 
    target1 = 8
    # 用例2: 只有一个target, expected output: [2, 2]
    nums2 = [5, 7, 8, 10]
    target2 = 8
    # 用例3: target不存在, expected output: [-1, -1]
    nums3 = [5, 7, 7, 8, 8, 10]
    target3 = 6
    # 用例4：数组只有一个元素, expected output: [0, 0]
    nums4 = [8]
    target4 = 8
    print(solution.searchRange(nums1, target1))
    print(solution.searchRange(nums2, target2))
    print(solution.searchRange(nums3, target3))
    print(solution.searchRange(nums4, target4))




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

