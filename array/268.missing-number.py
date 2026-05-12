#
# @lc app=leetcode id=268 lang=python3
# @lcpr version=30403
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (71.96%)
# Likes:    14339
# Dislikes: 3477
# Total Accepted:    3.9M
# Total Submissions: 5.4M
# Testcase Example:  '[3,0,1]\n[0,1]\n[9,6,4,2,3,5,7,0,1]'
#
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,0,1]
# 
# Output: 2
# 
# Explanation:
# 
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is
# the missing number in the range since it does not appear in nums.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1]
# 
# Output: 2
# 
# Explanation:
# 
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is
# the missing number in the range since it does not appear in nums.
# 
# 
# Example 3:
# 
# 
# Input: nums = [9,6,4,2,3,5,7,0,1]
# 
# Output: 8
# 
# Explanation:
# 
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is
# the missing number in the range since it does not appear in
# nums.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
# 
# 
# 
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        for i in range (len(nums)+1): # Time complexity is: O(n+1) * O(n)= O(n^2), space complexity is O(1)
            if i not in nums: # TC = O(n)
                return i
# Method 2: Hashset method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range (len(nums)+1): # Time complexity is: O(n), space complexity is O(n)
            if i not in num_set: # TC = O(1)
                return i
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [3,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [9,6,4,2,3,5,7,0,1]\n
# @lcpr case=end

#

