#
# @lc app=leetcode id=560 lang=python3
# @lcpr version=30403
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (47.27%)
# Likes:    25182
# Dislikes: 855
# Total Accepted:    2.4M
# Total Submissions: 5.2M
# Testcase Example:  '[1,1,1]\n2\n[1,2,3]\n3'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
#from common.node import *

# @lc code=start
''' UMPIRE template

  # Understand
inputs:integer array: nums, and an integer: k
outputs: integer: number of subarrays, sum = k
constraints:
edge cases:
1) if nums is an empty list, return 0
2) if cannot find subarray total == k, which means no valid subarray, then return 0
3) all the values are the same in nums, only choose contiguous group and total == k

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
Use dictionary{prefix_sum: # of prefix_sum}
  # Plan (pseudocode)
 1. create a frequency map
 2. traverse the nums, calcualte the prefix_sum, if the prefix_sum == k: add the item and its frequency into the frequency map
 3. return the value of the frequency map

  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # freq_dic stores {prefix_sum: frequency}
        # We initialize with {0: 1} to handle cases where prefix_sum == k
        freq_dic = {0: 1}
# 为什么要初始化 {0: 1}？
# 如果你不初始化 {0: 1}，当你的 prefix_sum 第一次刚好等于 k 时，代码去 freq_dic 里找 0，会发现找不到，导致漏掉这个从 数组开头算起 的子数组。
# 初始化 {0: 1} 的含义是：在数组开始之前，我们已经默认有一个“和为 0”的前缀存在了 1 次。
        prefix_sum = 0 # prefix_sum：我现在一共走了多远？
        count = 0 # count：到目前为止，我一共找到了多少段符合要求的k？

        for val in nums:
            prefix_sum += val

            # Check if (prefix_sum - k) exists in our history
            # If (currentPrefixSum - k) exists in our map, it means the elements between that previous point and our current point sum exactly to k.
            diff = prefix_sum - k # diff：为了凑够 k，我需要找以前哪个位置？
            if diff in freq_dic:
                count += freq_dic[diff] # freq_dtc[diff]: 以前那个位置我经过了几次？（经过几次，现在就能连成几个 k）
# 为什么要 count += freq_dic[diff] 而不是 +1？
# 因为如果有多个位置的前缀和都是 diff（比如数组里有 0，导致总和没变），那么每一个这样的位置到当前位置都能组成一个符合条件的子数组。
            # Record this prefix_sum in the map
            freq_dic[prefix_sum] = freq_dic.get(prefix_sum, 0) + 1
        return count


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    # test case 1
    nums1 = []
    k1 = 5
    print(f"Test1: {solution.subarraySum(nums1, k1)}") # Expected: 0
    nums2 = [1, 2, 5, 4]
    k2 = 13
    print(f"Test2: {solution.subarraySum(nums2, k2)}") # Expected: 0
    nums3 = [1, 1, 1, 1]
    k3 = 2
    print(f"Test3: {solution.subarraySum(nums3, k3)}") # Expected: 3



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

