#
# @lc app=leetcode id=912 lang=python3
# @lcpr version=30403
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (55.91%)
# Likes:    7253
# Dislikes: 845
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '[5,2,3,1]\n[5,1,1,2,0,0]'
#
# Given an array of integers nums, sort the array in ascending order and return
# it.
# 
# You must solve the problem without using any built-in functions in O(nlog(n))
# time complexity and with the smallest space complexity possible.
# 
# 
# Example 1:
# 
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not
# changed (for example, 2 and 3), while the positions of other numbers are
# changed (for example, 1 and 5).
# 
# 
# Example 2:
# 
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

# @lc code=start
# 方法一: 容易超时Memory Limit Exceeded, 因为这个版本虽然容易懂，但是它会创建很多新数组, 空间开销比较大。
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.quick_sort(nums)
    
#     def quick_sort(self, nums):
#         if len(nums) <= 1:
#             return nums
        
#         pivot = nums[len(nums)//2]

#         left = []
#         mid = []
#         right = []

#         for num in nums:
#             if num < pivot:
#                 left.append(num)
#             elif num > pivot:
#                 right.append(num)
#             else:
#                 mid.append(num)
#         return self.sortArray(left) + mid + self.sortArray(right)
# 方法二: 原地 in-place QuickSort
# i 和 j 是 index。
# nums[i] 和 nums[j] 才是 value。
# i 负责找左边“不够小”的 value。
# j 负责找右边“不够大”的 value。
# 如果 i <= j，说明这两个错误位置还有效。所以交换 nums[i] 和 nums[j]。交换 index i 和 index j 上的两个值。
class Solution:
    def sortArray(self, nums):
        self.quick_sort(nums, 0, len(nums) - 1) # 对 nums 这个数组，从 index 0 到 index len(nums) - 1 这一整段进行排序。
        return nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        
        pivot = nums[(left + right)// 2]

        # 在递归版 quick sort 里，我们不是每次都排序整个数组，而是排序数组中的某一段, 所以无需类似的初始化i = 0, j = len(nums) - 1
        # 这一次 partition 只处理 nums[left:right+1] 这一段。递归时，left 和 right 会变小，不能再用整个数组的范围。
        i = left
        j = right

        while i <= j:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            # 此时nums[i] >= pivot and nums[j] <= pivot
            if i <= j: # if i <= j 只是确认这两个指针是否还在有效范围内, 有无越界
                nums[i], nums[j] = nums[j], nums[i] # 如果还没交错，就交换 nums[i] 和 nums[j]。
                i += 1
                j -= 1
        
        self.quick_sort(nums, left, j)
        self.quick_sort(nums, i, right)

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    test_cases = [
    [5, 2, 9, 1, 7, 3], # 1. 基础乱序out of order
    [1, 2, 3, 4, 5], # 2. 已经有序 in order
    [5, 4, 3, 2, 1], # 3. 倒序 reverse(inverted order)
    [3, 1, 2, 3, 3, 0], # 4. Has duplicates
    [2, 2, 2, 2], # 5. all the same
    [-1, 5, 0, -3, 2], # 6. has negative vals
    [], # 7. empty list
    [10], # 8. only one element
]

for nums in test_cases:
    original = nums[:] # nums[:] 是 Python 的切片语法，表示把 nums 整个列表复制一份。
    result = solution.sortArray(nums)
    print(original, "->", result)



#
# @lcpr case=start
# [5,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,2,0,0]\n
# @lcpr case=end

#

