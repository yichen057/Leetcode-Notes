#
# @lc app=leetcode id=523 lang=python3
# @lcpr version=30403
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (31.40%)
# Likes:    7008
# Dislikes: 719
# Total Accepted:    785.3K
# Total Submissions: 2.5M
# Testcase Example:  '[23,2,4,6,7]\n6\n[23,2,6,4,7]\n6\n[23,2,6,4,7]\n13'
#
# Given an integer array nums and an integer k, return true if nums has a good
# subarray or false otherwise.
# 
# A good subarray is a subarray where:
# 
# 
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# 
# 
# Note that:
# 
# 
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n
# * k. 0 is always a multiple of k.
# 
# 
# 
# Example 1:
# 
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up
# to 6.
# 
# 
# Example 2:
# 
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose
# elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# 
# 
# Example 3:
# 
# Input: nums = [23,2,6,4,7], k = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Approach 1: Prefix Sum and Hashing
# 题目问的是：subarray sum 是 k 的倍数
# 如果两个 prefix sum 的余数一样：prefixSum1 % k == prefixSum2 % k, 说明中间这段subarray的和可以被k整除
# length也不用单独维护, 可以用i - firstIndex[remainder]直接算
# LC525:HashMap 存 prefixSum
# LC523:HashMap 存 prefixSum % k
# 本质上都是找两个相同的状态, 然后利用当前位置-第一次出现的位置, 求区间
# eg:     nums = [1, 5, 2, 1,  5,  2,  1,  3], k = 5
# prefixSum = [0, 1, 6, 8, 9, 14, 16, 17, 20]
# remainder = [0, 1, 1, 3, 4,  4,  1,  2,  0]
#                 ^  ^     ^   ^ not valid, since subarray size is 1
#              ^  ^                ^       ^ 0...0和1...1, both subarrays are valid, return True
# Complexity Analysis
# Let n be the number of elements in nums.
# Time complexity: O(n)
# We iterate through the array exactly once. In each iteration, we perform a search operation in the hashmap that takes O(1) time. Therefore, the time complexity can be stated as O(n).
# Space complexity: O(n)
# In each iteration, we insert a key-value pair in the hashmap. The space complexity is O(n) because the size of the hashmap is proportional to the size of the list after n iterations.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        FirstIndex = {0: -1} # 本题关键hashmap不是存 prefixSum，而是存：prefixSum % k
        # key: remainder of prefixSum with k; value: index of remainder
        for i, num in enumerate(nums):
            prefixSum += num
            remainder = prefixSum % k

            if remainder in FirstIndex: 
            # 如果余数在hashtable里, 如果长度不满足条件, hashtable也不更新第一次出现的位置, 和LC525题一样
                if i - FirstIndex[remainder] >= 2:
                    return True
            else:
                FirstIndex[remainder] = i
        return False

    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [23,2,4,6,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n13\n
# @lcpr case=end

#

