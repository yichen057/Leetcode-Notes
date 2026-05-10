#
# @lc app=leetcode id=217 lang=python3
# @lcpr version=30403
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (64.31%)
# Likes:    13994
# Dislikes: 1372
# Total Accepted:    6.4M
# Total Submissions: 9.9M
# Testcase Example:  '[1,2,3,1]\n[1,2,3,4]\n[1,1,1,3,3,4,3,2,4,2]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# 
# Output: true
# 
# Explanation:
# 
# The element 1 occurs at the indices 0 and 3.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4]
# 
# Output: false
# 
# Explanation:
# 
# All elements are distinct.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# 
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *
from typing import List
''' 
UMPIRE template

# Understand
inputs:integer array:nums
outputs:boolean: true: at least twice in the array; False: only once, distinct
constraints:
edge cases: 
1) each value appears only once; 
2) empty list; 
3) each value appears at least twice

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
use Set to store visited value in the array
  # Plan (pseudocode)
initilize a set to store future visited value in the array
iterate the array, check whether each item is in the set:
if item in set: return True
if item not in set: add it to the set
Finally after the iteration, return False
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
Time: O(n): Traverse the list exactly once
Space: O(n): In the worst case (all elements distinct), the set stores all n elements.
'''
# @lc code=start
class Solution:
    # Method 1: loop approach
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     # Initialize a set to store visited values
    #     seen = set()
    #     for val in nums:
    #         # If item is already in the set, we found a duplicate
    #         if val in seen:
    #             return True
    #         # Otherwise, track the value and keep moving
    #         seen.add(val)
        
    #     # If the loop finishes without finding a duplicate
    #     return False
    # Method 2: length comparison approach
    # While elegant, this approach always takes O(n) space and time, 
    # whereas the fist loop approach can return True early as soon as it hits the first duplicate.
    def containsDuplicate(self, nums):
      return len(nums) != len(set(nums))
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    # Test Case 1: All distinct
    nums1 = [1, 2, 3, 4, 5]
    # Test Case 2: Empty List
    nums2 = []
    # Test Case 3: All duplicates
    nums3 = [1, 1, 2, 2, 3, 3]
    print(f"Test 1:{solution.containsDuplicate(nums1)}")  
    print(f"Test 2:{solution.containsDuplicate(nums2)}")    
    print(f"Test 3:{solution.containsDuplicate(nums3)}")  
    # Expected output: 
    # False
    # False
    # True

#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,3,3,4,3,2,4,2]\n
# @lcpr case=end

#

