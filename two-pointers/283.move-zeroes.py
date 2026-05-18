#
# @lc app=leetcode id=283 lang=python3
# @lcpr version=30403
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (63.83%)
# Likes:    19518
# Dislikes: 607
# Total Accepted:    5.1M
# Total Submissions: 8.1M
# Testcase Example:  '[0,1,0,3,12]\n[0]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    # method 1: Two pointers method
    # TC: O(n)
    # SC: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # fast 找有效元素, slow 放有效元素
        slow = 0
        # put non-zero element to the front
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        # fill remaining elements in the array with 0's.
        for i in range(slow, len(nums)):
            nums[i] = 0
        
    # method 2: slicing array
    # TC: O(n) for nums[:] array copy + O(n²) remove operations including: O(n) calls * O(n) per remove = O(n²) + O(n) for (nums + res) also creates a temporary list = O(n²)
    # SC: O(n) for nums[:] array copy  + O(n) for res created + O(n) for (nums + res) also creates a temporary list= O(n)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        LeetCode 不看你的 return 值。它只检查原来的 nums 有没有被你改成目标结果。
        LeetCode 283 Move Zeroes 要求你原地修改 nums，不要 return 新数组。
        """
        res = []
        for n in nums[:]: # Iterate over a copy of nums, so it is safer to remove items from the original nums during the loop. If modifying a list while directly iterating over it can cause skipped elements or confusing behavior.
            if n == 0:
                res.append(n)
                nums.remove(n) # 如果你知道要删的是哪个值：nums.remove(value); 如果你知道要删的是哪个index: nums.pop(i)
                # 但是很多 LeetCode 题不推荐频繁 remove() 或 pop(i)，因为删除中间元素会导致后面的元素整体左移，时间复杂度是：O(n), 所以像 “Remove Element” 这种题，更常用 two pointers 覆盖法，不是频繁删除。
        nums[:] = nums + res # nums + res creates a new list, Then nums[:] = ... writes the result back into the original list
        # 把原来的 nums 内容整体替换成新内容, 塞回原来的 nums 里面。nums[:]在赋值左边, 指的是不换掉 nums 这个 list 对象本身，而是把它里面的内容整体替换掉。nums[:]在赋值右边, 指的是会创建一个 浅拷贝，也就是一个新的 list。

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

