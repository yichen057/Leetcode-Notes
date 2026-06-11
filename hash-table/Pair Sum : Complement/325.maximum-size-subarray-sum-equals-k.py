#
# @lc app=leetcode id=325 lang=python3
# @lcpr version=30403
#
# [325] Maximum Size Subarray Sum Equals k
#
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
#
# algorithms
# Medium (50.88%)
# Likes:    2128
# Dislikes: 66
# Total Accepted:    222.2K
# Total Submissions: 436.7K
# Testcase Example:  '[1,-1,5,-2,3]\n3\n[-2,-1,2,1]\n1'
#
# Given an integer array nums and an integer k, return the maximum length of a
# subarray that sums to k. If there is not one, return 0 instead.
# 
# 
# Example 1:
# 
# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# 
# 
# Example 2:
# 
# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^5
# -10^4 <= nums[i] <= 10^4
# -10^9 <= k <= 10^9
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 题目要求最长长度, 我们需要最早出现的位置, 所以必须加
# 想找subarray sum = k, 根据prefixSum: currSum - prevSum = k, 变形为希望出现过: prevSum = currSum - k, 可以把prevSum(即need)视作target
# 而LC525题目, 是问0和1的数量相同的subarray, 需要先转换为0->-1, 1->1, 问题变成subarray sum == 0, 即k = 0, 所以need = curSum - 0 = curSum, 因此 LC525 里面你看不到单独的 need，因为：need == prefixSum, 所以可以直接查if prefixSum in firstIndex:
# LC525题里的prefixSum, 其实就是LC325题里的curSum, 只是名字不一样
# LC325: 找 sum == k, 所以查 curSum - k，存 curSum。
# LC525: 找 sum == 0, 所以查 curSum，存 curSum。LC 525 = 先把 0 变 -1，然后做 k=0 的 LC 325

# Complexity Analysis
# Given N as the length of nums,
# Time complexity: O(N)
# We only make one pass through nums, each time doing a constant amount of work. All hash map operations are O(1).
# Space complexity: O(N)
# Our hash map can potentially hold as many key-value pairs as there are numbers in nums. An example of this is when there are no negative numbers in the array.
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        maxLen = 0 
        curSum = 0
        firstIdx = {0: -1} # key: prefixSum, index: first_index of prefixSum
        # key是prefixSum, value存的是prefixSum第一次出现的index
        for i, num in enumerate(nums):
            curSum += num
            need = curSum - k
            # 对于prefix Sum题, 查 need 存 curSum
            if need in firstIdx:
                maxLen = max(maxLen, i - firstIdx[need])   
            if curSum not in firstIdx: # 题目要求最长长度, 我们需要最早出现的位置, 所以必须加这个判断
                firstIdx[curSum] = i # curSum 是实际出现过的prefixSum, need是target只是我们要找的数字, 所以我们肯定存hashpmap[curSum]
        return maxLen
         
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,-1,5,-2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-2,-1,2,1]\n1\n
# @lcpr case=end

#

