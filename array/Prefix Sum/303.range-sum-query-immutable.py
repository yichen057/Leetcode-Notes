#
# @lc app=leetcode id=303 lang=python3
# @lcpr version=30403
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (72.33%)
# Likes:    3892
# Dislikes: 2023
# Total Accepted:    945K
# Total Submissions: 1.3M
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
  '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, handle multiple queries of the following
# type:
# 
# 
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.
# 
# 
# Implement the NumArray class:
# 
# 
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).
# 
# 
# 
# Example 1:
# 
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
# 
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= left <= right < nums.length
# At most 10^4 calls will be made to sumRange.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Method 1: 暴力解法:
class NumArray:
    # Init: TC: O(1)
    def __init__(self, nums: List[int]): 
        self.nums = nums

    # Query: TC: O(n)
    def sumRange(self, left: int, right: int) -> int:# 注意本题要返回的是int不是List[int]
        prefixSum = 0
        for i in range(left, right+1):
            prefixSum += self.nums[i]
    
        return prefixSum
# Method 2: Prefix Sum解法:
class NumArray:
    # 标准解法是在 __init__ 里提前算好 Prefix Sum, TC: O(n)
    def __init__(self, nums: List[int]): 
        self.prefix = [0] # 表示前0个元素的和是0, prefix[i]=nums[0] ~ nums[i-1] 的总和
        # 写法一:
        for num in nums:
            self.prefix.append(self.prefix[-1]+num) # 用prefix数组的最后一个元素(即最新的前一个元素之和)再加上当前元素
        # 写法二: 好理解, 这里的runningSum永远等于self.prefix[-1]即最新的 cumulative sum
        runningSum = 0
        for num in nums:
            runningSum += num
            self.prefix.append(runningSum)
            
    # TC: O(1). 求nums[left:right+1]的区间和
    # 区间[left, right], sumRange(left,right)=prefix[right+1]-prefix[left]
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# ["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]\n
# @lcpr case=end

#

