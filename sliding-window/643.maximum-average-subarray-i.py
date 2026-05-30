#
# @lc app=leetcode id=643 lang=python3
# @lcpr version=30403
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (47.82%)
# Likes:    4444
# Dislikes: 387
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '[1,12,-5,-6,50,3]\n4\n[5]\n1'
#
# You are given an integer array nums consisting of n elements, and an integer
# k.
# 
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10^-5 will be accepted.
# 
# 
# Example 1:
# 
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# 
# 
# Example 2:
# 
# Input: nums = [5], k = 1
# Output: 5.00000
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 先计算第一个长度为 k 的窗口和
# 再从k到len(nums)遍历, 求window_sum
# window_sum = window_sum + 右边加入一个新元素 - 左边移出一个旧元素, 持续更新 window_sum

# method 1: fixed_size sliding window + running sum for two loops(先计算第一个窗口和, 再计算其他), 更推荐!
# 本题要最终维护max_sum, 需要有一个真实有效的窗口对其初始化max_sum = first_window_sum, 所以先建立第一个窗口很自然
# for r in range(k):
#     current_sum += nums[r]

# max_sum = current_sum

# 注意要看本题的constraints: 
# 1 <= k <= n <= 105, 说明k最小为1
# -104 <= nums[i] <= 104, 说明元素可为负

# TC: O(n), because each element is added and removed at most once. 两个循环前后顺序执行，所以时间复杂度相加：O(k) + O(n - k) = O(n)
# 第一个循环处理前 k 个元素
# 第二个循环处理剩下 n - k 个元素
# 总共：k + (n - k) = n
# SC: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k <= 0 or k > len(nums):
            return 0

        current_sum = 0

        # Build the first window of size k.
        for r in range(k):
            current_sum += nums[r]

        # The first valid window initializes the answer. 第一个完整窗口直接初始化max_sum，所以无论元素是正数还是负数，都不会出错。
        max_sum = current_sum

        # Slide the window through the rest of the array.
        for r in range(k, len(nums)):
            current_sum = current_sum + nums[r] - nums[r-k] # Add the new right element and remove the old left element
            max_sum  = max(max_sum,current_sum)
        return round(max_sum / k, 5)

# method 2: fixed_size sliding window + running sum for one loop
# TC: O(n), because each element is added and removed at most once.
# SC: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or k <= 0 or k > len(nums):
            return 0
        
        l = 0
        window_sum = 0
        max_sum = float("-inf") # 注意! 这里max_sum初始化不可以为0, 如果数组中的所有长度为 k 的窗口和都是负数，max_sum 就永远错误地停留在 0。eg: nums = [-5, -4, -3], k = 2, output = -3.5 而不是0

        for r in range(len(nums)):
            # Add the new element on the right
            window_sum += nums[r]

            # keep the window length no larger than k
            if r - l + 1 > k:
                window_sum -= nums[l] # 注意, 减掉的最左边的元素, 并不是减掉最右边的元素
                l += 1

            # Record the sum only when the window length is exactly k.
            if r - l + 1 == k:
                # print("window_sum:",window_sum)
                max_sum = max(max_sum, window_sum)
                # print("max_sum:",max_sum)
        return max_sum / k
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,12,-5,-6,50,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n
# @lcpr case=end

#

