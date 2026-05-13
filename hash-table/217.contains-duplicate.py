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
    # Method 1: one-loop + set approach
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     # Initialize a set to store visited values
    #     seen = set()
    #     # One-Loop Efficiency: If the very first two numbers are duplicates (e.g., [1, 1, 2, 3, 4...]), the one-loop version stops at the second element. It is much faster in the "Average Case."
    #     for val in nums:
    #         # If item is already in the set, we found a duplicate
    #         if val in seen:
    #             return True
    #         # Otherwise, track the value and keep moving
    #         seen.add(val)
        
    #     # If the loop finishes without finding a duplicate
    #     return False

    # Method 2: two-loop + dictinoary approach
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     map = {} # space complexity: O(n). 需要一个 map 来存储数组中的数字。在最坏情况下（所有数字都不同），map 会存储 n 个键值对。
    #     # Two Loops time complexity: n (first loop) + n (second loop) = 2n -> O(n) ignore constant term.
    #     # Two-Loop Efficiency: It must wait to finish the entire first loop (counting everything) before it even starts the second loop to check for duplicates.
    #     for num in nums:
    #         map[num] = map.get(num, 0) + 1
    #     for freq in map.values():
    #         if freq >= 2:
    #             return True
    #     return False
    # Method 3: length comparison approach
    # While elegant, this approach always takes O(n) space and time, 
    # whereas the fist loop approach can return True early as soon as it hits the first duplicate.
    def containsDuplicate(self, nums):
      return len(nums) != len(set(nums))
    # 当你调用 set(nums) 时，时间和空间复杂度是O(n). 计算机在底层做了以下工作：
    # 1) 遍历数组：它必须从头到尾扫描一遍 nums 数组（长度为 n）。
    # 2) 哈希计算与插入：对于数组中的每一个数字，计算机都要计算它的哈希值，并尝试将其存入集合（Set）中。
    # 3) 去重：在存入过程中，集合会自动处理重复项。因为这个过程涉及到了对 n 个元素的处理，所以时间复杂度是 O(n)。
    
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

