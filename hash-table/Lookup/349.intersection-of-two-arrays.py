#
# @lc app=leetcode id=349 lang=python3
# @lcpr version=30403
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (77.74%)
# Likes:    6948
# Dislikes: 2347
# Total Accepted:    1.9M
# Total Submissions: 2.4M
# Testcase Example:  '[1,2,2,1]\n[2,2]\n[4,9,5]\n[9,4,9,8,4]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
# 
# 
# Example 1:
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

''' UMPIRE template

  # Understand
inputs:two integer arrays
outputs:intersection array, each element must be unique, cannot be the same
constraints:
edge cases: 
1) no intersection, return []; 
2) if there are duplicates, result can only return unique intersected values

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
Array + Set
  # Plan (pseudocode)
 1. create a set to store intersected unique value
 2. convert nums1 to a set
 3. check the nums2, if nums2 in the set, add the value in the set
 4. return the list of set
  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
time: O(n) + O(m) = O(n), n= len(nums1), m = len(nums2)
space: O(y) + O(n) = O(n)
'''
# @lc code=start
class Solution:
    # 方法一: Use set 
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        setNums1 = set(nums1) # always traverse the entire list, use a set to ensure uniqueness. TC: O(m)

        for val in nums2: # TC: O(m)
            if val in setNums1:
                result.add(val) # TC:O(1) average
        return list(result)
    # 方法二: Python has a built-in operator for set intersections:
        return list(set(num1) & set(nums2))
    # 方法三: Use list
        result = []
        setNums1 = set(nums1)

        for val in nums2:
            if val in setNums1:
                result.append(val)
                setNums1.remove(val) # prevents duplicates in the result
        return result
# @lc code=end

       

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    # test case 1: intersection exist
    nums1 = [1, 3, 8, 9]
    nums2 = [2, 3, 9, 7]
    print(f"Test1: {solution.intersection(nums1, nums2)}") # Expected: [3, 9]
    # test case 1: no intersection
    nums3 = [1, 3, 8, 9]
    nums4 = [2, 4, 7, 0]
    print(f"Test2: {solution.intersection(nums3, nums4)}") # Expected: []
    nums5 = [1, 2, 2, 1]
    nums6 = [2, 2]
    print(f"Test3: {solution.intersection(nums5, nums6)}") # Expected: [2]



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

