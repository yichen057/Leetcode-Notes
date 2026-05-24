#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (59.87%)
# Likes:    12928
# Dislikes: 283
# Total Accepted:    3.4M
# Total Submissions: 5.7M
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1
        
        # while left <= right:
        #     middle = left + (right - left) // 2
        #     if nums[middle] > target:
        #         right = middle - 1
        #     elif nums[middle] < target:
        #         left = middle + 1
        #     elif nums[middle] == target:
        #         return middle
        # return -1

      # binary search template:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
        # 一般先检查start再检查end, 因为一般要求的是first index, 所以先检查更靠左的start, 如果start!=target, 再检查靠右的end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1    
# @lc code=end

