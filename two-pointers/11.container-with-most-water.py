#
# @lc app=leetcode id=11 lang=python3
# @lcpr version=30403
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (60.01%)
# Likes:    34368
# Dislikes: 2213
# Total Accepted:    5.4M
# Total Submissions: 9M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]\n[1,1]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

# @lc code=start
class Solution:
    # Method 1: Brute force solution, but got error: time limit exceeded
    # def maxArea(self, height: List[int]) -> int:
    #     res = 0 
    #     for l in range(len(height)):
    #         for r in range(l+1, len(height)):
    #             area = min(height[l], height[r]) * (r - l)
    #             res = max(res, area)
    #     return res
    # Method 2: Two pointer - efficient solution
    # linear time solution: O(n)
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1 # we want the width to be as big as possible
        res = 0
        while left < right: # to compute the area, we should have width, so left > right
            area = min(height[left], height[right]) * (right - left) # [left, right] 之间的矩形面积, 高度是由 height[left] 和 height[right] 较小的值决定的。
            res = max(res, area)
            # 双指针技巧，移动较低的一边: 那条边可能会变高，使得矩形的高度变大，进而就「有可能」使得矩形的面积变大；相反，如果你去移动较高的那一边，矩形的高度是无论如何都不会变大的，所以不可能使矩形的面积变得更大。
            if height[left] < height[right]:
                left += 1 # increment left pointer cus we want to maximize both of heights
            else:
                right -= 1 # decrement right pointer
            # if height[left] = height[right], we could increment left pointer or decrement right pointer, so we can just condense it.
        return res
     
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.maxArea([1, 1]))
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

