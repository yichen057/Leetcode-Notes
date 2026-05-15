#
# @lc app=leetcode id=238 lang=python3
# @lcpr version=30403
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (68.87%)
# Likes:    26037
# Dislikes: 1707
# Total Accepted:    4.5M
# Total Submissions: 6.6M
# Testcase Example:  '[1,2,3,4]\n[-1,1,0,-3,3]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
# 
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
# 
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
# 
# 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit
# integer.
# 
# 
# 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

''' UMPIRE template
# Understand
Input: nums, a list of integers.
Output: a list answer where answer[i] is the product of all elements in nums except nums[i].

Constraints:
- 2 <= nums.length <= 10^5
- The product of any prefix or suffix fits in a 32-bit integer.
- Must solve without division.
- Ideally O(n) time and O(1) extra space, excluding the output array.

Edge cases:
- nums contains one zero, e.g. [1, 2, 0, 4]
- nums contains multiple zeros, e.g. [0, 1, 0, 3]
- nums contains negative numbers
- nums length is 2

# Match
This is an array prefix/suffix product problem.
For each index i:
answer[i] = product of elements before i * product of elements after i.

Pattern:
- Prefix product from left to right
- Postfix product from right to left
- Store prefix products in result first, then multiply postfix products into result

# Plan (pseudocode)
1. Create result array res initialized with 1.
2. Traverse nums from left to right.
   - Store the product of all elements before index i in res[i].
   - Update prefix by multiplying nums[i].
3. Traverse nums from right to left.
   - Multiply res[i] by the product of all elements after index i.
   - Update postfix by multiplying nums[i].
4. Return res.

  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
  TC: O(n)
  SC: O(n), 2<=nums.length<=10^5, res = [1] * len(nums)随着输入变大, res也会变大, 所以是O(n)
  只有当数组长度固定, 比如用于是26, 空间复杂度才是常数级别O(1)
'''
# @lc code=start
# 核心思想: res[i] = i 左边所有数的乘积 * i 右边所有数的乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # don't forget to multiply nums[i] in the nums
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i] # don't forget to multiply nums[i] in the nums
        return res
  
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.productExceptSelf([1, 2, 3, 4]))



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

