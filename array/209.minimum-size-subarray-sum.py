#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (49.87%)
# Likes:    13766
# Dislikes: 515
# Total Accepted:    1.6M
# Total Submissions: 3.2M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to
# target. If there is no such subarray, return 0 instead.
# 
# 
# Example 1:
# 
# 
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
# 
# 
# Example 2:
# 
# 
# Input: target = 4, nums = [1,4,4]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        window_sum = 0
        result = float('inf')
        for right in range(len(nums)):#此时换成左闭右闭区间, 用for循环right就是窗口里最后一个元素, 不用手动right+=1
            window_sum += nums[right]
        # while right < len(nums):
        #     # 增大窗口,扩张右边界, 使和达到或者超过target
        #     window_sum += nums[right] # 此时是right未知的元素被加入
        #     right += 1
            # 此时由于right+=1, 窗口区间变成[left, right)右开, right-1位置的元素刚被加入
            while window_sum >= target:
                # 缩小窗口, 收缩左边界, 尝试得到最短长度
                # 先计算长度，再收缩左边界。窗口满足条件时，应该立即记录下此时的长度（因为它可能是最优的）。然后再尝试收缩，看能不能缩得更短，同时仍满足条件。如果收缩之后不满足条件，就会退出内层 while，等右边再扩张。
                subLength = right - left +1 # 左闭右闭区间的长度是right-left+1
                # subLength = right - left #滑动窗口的长度, [left, right)的长度是right-left, [left, right]的长度是right-left+1
                result = min(subLength, result)
                window_sum = window_sum - nums[left]
                left += 1
        return 0 if result == float('inf') else result #如果不存在满足条件的子数组，题目要求返回 0, 而不是返回 inf。

# @lc code=end

