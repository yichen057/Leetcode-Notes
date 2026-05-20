#
# @lc app=leetcode id=162 lang=python3
# @lcpr version=30403
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (46.96%)
# Likes:    14669
# Dislikes: 4957
# Total Accepted:    2.4M
# Total Submissions: 5.2M
# Testcase Example:  '[1,2,3,1]\n[1,2,1,3,5,6,4]'
#
# A peak element is an element that is strictly greater than its neighbors.
# 
# Given a 0-indexed integer array nums, find a peak element, and return its
# index. If the array contains multiple peaks, return the index to any of the
# peaks.
# 
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
# always considered to be strictly greater than a neighbor that is outside the
# array.
# 
# You must write an algorithm that runs in O(log n) time.
# 
# 
# Example 1:
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        # peak可能在两端
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
    
            # 1) 如果mid向左上方倾斜, 选左半边
            if nums[mid] < nums[mid-1]:
                end = mid
            # 2) 如果mid向右上方倾斜, 选右半边
            elif nums[mid] < nums[mid+1]:
                start = mid
            # 3) 如果mid为peak, 直接返回
            else:
                return mid
        
        # 下面的判断是有必要的，因为你的二分循环退出时，循环退出条件是：start+1>=end, 不一定已经直接找到 peak。通常就是start 和 end 相邻了
        print("start:", start, "end:", end)
        # 因为题目要求保证一定有peak, 所以返回start和end中大的一个
        if nums[start] < nums[end]:
            return end
        return start

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#

