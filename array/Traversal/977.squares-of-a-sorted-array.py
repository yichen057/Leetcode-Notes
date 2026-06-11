#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (73.31%)
# Likes:    9846
# Dislikes: 261
# Total Accepted:    2.3M
# Total Submissions: 3.2M
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
# 
# 
# 
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 左指针l, 右指针r和指向数组终止位置的i
        l, r, i = 0, len(nums)-1, len(nums)-1
        # 提前定义列表存放结果
        result = [float('inf')] * len(nums)
        # 或者 result =[0] * len(nums)
        # 区别: 
        # 1) [0] * len(nums) 结果数组、占位, 初始化成全 0。 → [0] * n
        # 2) [float('inf')] * len(nums) 未知值，一开始不知道答案，先放一个极大值初始化成全无穷大 (inf)，后面不断 min() 更新。需要用 min 比较 → [float('inf')] * n
        while l <= r: # 左右边界进行对比, 找出最大值
            if nums[l] ** 2 < nums[r] ** 2:
                result[i] = nums[r] ** 2
                r -= 1 #右指针往左移动
            else:
                result[i] = nums[l] ** 2
                l += 1 #左指针往右移动
            i -= 1 #存放结果的指针需要往前平移一位
        return result
# @lc code=end

