#
# @lc app=leetcode id=35 lang=python3
# @lcpr version=30403
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (51.27%)
# Likes:    18895
# Dislikes: 903
# Total Accepted:    4.8M
# Total Submissions: 9.3M
# Testcase Example:  '[1,3,5,6]\n5\n[1,3,5,6]\n2\n[1,3,5,6]\n7'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# 
# Example 2:
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# 
# 
# Example 3:
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
# from common.node import *

# @lc code=start
# 找第一个 >= target的位置 
# TC: O(log n)
# SC: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        # 如果 target 比数组最后一个数还大，应该插入到数组末尾，也就是 len(nums)
        if target > nums[-1]:
            return len(nums)

        # 如果end = len(nums), 表示把数组末尾之后的位置也纳入答案范围。不用再单独做上述判断
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # print("mid:", mid)
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        # print("start:", start)
        # print("end:", end)  
        # 到达二分部分时, 此时数组中一定至少有一个元素满足：nums[index] >= target(因为前面判断了if target > nums[-1]即target比最大元素还大, 循环结束后答案只可能是start 或 end     
        # 找最左边符合 nums[index] >= target 的位置，所以先检查 start
        if nums[start] >= target: # 注意这里是大于等于号, 不是等于号!
            return start
        return end

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    nums1= [1, 3, 5, 6]
    target1 = 0 # target比所有数小
    target2 = 7 # target比所有数大
    target3 = 5 # target存在
    target4 = 2 # target不存在且插入中间
    print(solution.searchInsert(nums1, target1)) # expected output: 0
    print(solution.searchInsert(nums1, target2)) # expected output: 4
    print(solution.searchInsert(nums1, target3)) # expected output: 2
    print(solution.searchInsert(nums1, target4)) # expected output: 1






#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

