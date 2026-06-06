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
# 本题得用merge sort, 时间复杂度一定是O(n log n), 不会像quick sort被卡成 O(n^2)。
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        temp = [0] * len(nums)
        self.merge_sort(nums, 0, len(nums) - 1, temp)
        return nums
    
    def merge_sort(self, nums:List[int], start: int, end: int, temp: List[int]) -> None:
        if start >= end:
            return 
        
        mid = (start + end) // 2

        self.merge_sort(nums, start, mid, temp)
        self.merge_sort(nums, mid+1, end, temp)

        self.merge(nums, start, mid, end, temp)

    def merge(self, nums:List[int], start: int, mid: int, end: int, temp: List[int]) -> None:
        left = start
        right = mid + 1
        index = start

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                temp[index] = nums[left]
                left += 1
            else:
                temp[index] = nums[right]
                right += 1
            index += 1 # 注意: 别忘了移动temp上的index指针

        while left <= mid:
            temp[index] = nums[left]
            left += 1
            index += 1

        while right <=end:
            temp[index] = nums[right]
            right += 1
            index += 1
        
        for i in range(start, end + 1):
            nums[i] = temp[i]

# quick sort 最坏的时间复杂度是O(n^2), 平均时间复杂度是O(log n), 平均空间复杂度O(log n), 省空间
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums
    
    def quick_sort(self, nums:List[int], start: int, end: int) -> None:
        if start >= end:
            return
        
        left, right = start, end

        pivot = nums[(start + end) // 2] # quick sort的pivot是固定的, 当pivot平均是: O(n log n), 最坏 O(n^2), 所以可能会报错: Time Limit Exceeded. 两个解决方案:
        # 1. 随机pivot: import random, pivot = nums[random.randint(start, end)], 平均 O(nlogn),空间 O(logn)
        # 2. merge sort: 稳定O(n log n) , 只是需要额外的O(n)空间, 由于temp: O(n)主导, 递归栈O(log n )不主导

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)

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

