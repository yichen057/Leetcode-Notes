#
# @lc app=leetcode id=852 lang=python3
# @lcpr version=30403
#
# [852] Peak Index in a Mountain Array
#
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Medium (66.85%)
# Likes:    8537
# Dislikes: 1954
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[0,1,0]\n[0,2,1,0]\n[0,10,5,2]'
#
# You are given an integer mountain array arr of length n where the values
# increase to a peak element and then decrease.
# 
# Return the index of the peak element.
# 
# Your task is to solve it in O(log(n)) time complexity.
# 
# 
# Example 1:
# 
# 
# Input: arr = [0,1,0]
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: arr = [0,2,1,0]
# 
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: arr = [0,10,5,2]
# 
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= arr.length <= 10^5
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# 本题最好通过画图的方式去理解区分mid的不同情况
# 注: 本题是没有重复点且先增后减的序列, n个整数, 找山顶最大值的index
# 如果有重复点的话, 这个二分法就不适用了, 不能判断是丢左边还是右边
# 判断的是“mid 到 mid+1 是上坡还是下坡”，这是山脉数组找 peak 最干净的二分写法,推荐!
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr:
            return -1
        start, end = 0, len(arr) -1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] > arr[mid + 1]: # 下坡, 山峰在左边, 丢掉右边
                end = mid
            else: # 上坡, 山峰在右边, 丢掉左边
                start = mid

        # 返回start和end中较大的值, 则为山顶
        if arr[start] > arr[end]:
            return start
        return end
        # 如果题目是返回peak的value, 可以这么写, 只比较两个数, 时间复杂度是O(1), 如果max是比较扫描整个数组, TC=)(n)
        # return max(nums[start], nums[end]) # 如果输入数据只有两个数,eg[1, 2] 则不会进入while, 直接做两数比最大值return即可
# 方法二:
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if not arr:
            return -1
        start, end = 0, len(arr)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid + 1] > arr[mid]:
                start = mid
            elif arr[mid - 1] > arr[mid]:
                end = mid
           
        if arr[start] > arr[end]:
            return start
        return end
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,10,5,2]\n
# @lcpr case=end

#

