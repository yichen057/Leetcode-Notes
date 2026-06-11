#
# @lc app=leetcode id=525 lang=python3
# @lcpr version=30403
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (51.45%)
# Likes:    8893
# Dislikes: 450
# Total Accepted:    687.2K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1]\n[0,1,0]\n[0,1,1,1,1,1,0,0,0]'
#
# Given a binary array nums, return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.
# 
# 
# Example 1:
# 
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number
# of 0 and 1.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# Example 3:
# 
# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 给定一个二元数组 nums，求0 和 1 
# 转换: 0->-1, 1->1, 这样问题就转成找最长subarray sum == 0, 也就是prefixSum 题目
# 如果两个位置的prefixSum一样, 即prefixSum[j] == prefixSum[i], 说明中间这一段的和是0, 相减为0, 也就代表中间这一段
# 0和1数量相同
# hashtable存的是prefixSum第一次出现的位置{prefixSum:first_index}

# method 1: brute force method, but time limit exceeded
# Time: O(n^2)
# Space: O(1)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        for l in range(len(nums)):
            # 对于暴力解法, 每个新的l都代表一个全新的子数组起点, 所以统计变量必须重新开始, 必须放在外层循环里面。
            # 如果是sliding window, 可以吧初始化放在循环外面, 因为窗口一直在延续, 是同一个窗口不断扩张和收缩
            # 判断口诀:
            # 统计变量是否属于当前窗口？是 → 可以放外面持续维护
            # 统计变量是否属于当前起点l? 是 → 每次l变化都要重新初始化, 本题描述的是nums[l...r]这个区间, 所以当l+=1时, zeroCount和oneCount必须清零重新统计
            print("l:",l)
            zeroCount = 0
            oneCount = 0
            for r in range(l, len(nums)):
                print("r:",r)
                if nums[r] == 0:
                    zeroCount += 1
                else:
                    oneCount += 1
                if zeroCount == oneCount:
                    maxLen = max(maxLen, r - l + 1) # 注意这里是 r - l + 1，因为 l 和 r 都是真正的子数组左右边界。
        return maxLen
# method 2: prefixSum method
# prefix[r] - prefix[l-1] = k, 移项后得到prefix[l-1] = prefix[r] - k
# 只要以前出现过前缀和为prefix[l-1], 那么从那个位置后开始到当前位置r, 一定构成一个和为k的子数组. 
# 我们统计的应该是nums[l...r], 而不是nums[r+1...r]这种不存在的区间
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        firstIndex = {0: -1} # key是prefixSum, value存的是prefixSum第一次出现的index
        prefixSum = 0
        maxLen = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefixSum -= 1
            else:
                prefixSum += 1

            if prefixSum in firstIndex:
                maxLen = max(maxLen, i - firstIndex[prefixSum]) # 这里不用减1是因为prefix[r] - prefix[l-1], 取的是l-1+1到r区间的长度, 可以直接减不用加1
            else:
                firstIndex[prefixSum] = i

        return maxLen
# 与LC325题统一的prefixSum代码写法:
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        firstIndex = {0: -1}
        curSum = 0
        maxLen = 0
        k = 0

        for i, num in enumerate(nums):
            if num == 0:
                curSum -= 1
            else:
                curSum += 1

            need = curSum - k   # 其实就是 curSum

            if need in firstIndex:
                maxLen = max(maxLen, i - firstIndex[need])

            if curSum not in firstIndex:
                firstIndex[curSum] = i

        return maxLen
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,1,1,0,0,0]\n
# @lcpr case=end

#

