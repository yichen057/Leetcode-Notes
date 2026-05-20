#
# @lc app=leetcode id=658 lang=python3
# @lcpr version=30403
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (49.67%)
# Likes:    9108
# Dislikes: 936
# Total Accepted:    822.6K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,4,5]\n4\n3\n[1,1,2,3,4,5]\n4\n-1'
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.
# 
# An integer a is closer to x than an integer b if:
# 
# 
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# 
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
# 
# Output: [1,1,2,3]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
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
    # TC: O(log n) for binary search target + (O(k) for for loop expansion + O (k log k)) for sorting results, 由于 O(k log k) 比 O(k) 大，所以可以简化成：O(log n + k log k)
    # SC: O(k) for results space and sorted output, 最多存k个元素
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = self.findUpperCloset(arr, x)
        left = right - 1

        # 找到中届线后, 从中界线两边找最近的k个数字, 合并两个排好序的array
        # 两根指针从中间往两边扩展背向而行, 依次找到最接近的k个数
        results = []
        for _ in range(k): # merge sorted array, merge过程的时间复杂度: O(k), results长度是k, 不是n
            # 如果左边更接近, 选左边
            if self.isLeftCloser(arr, x, left, right): # x: target
                results.append(arr[left]) 
                left -= 1 # 背向移动双指针
            else:
                results.append(arr[right])
                right += 1

        return sorted(results) # return the result list sorted in ascending order. TC= O(n log n)
        #sorted(nums)返回的是new array, 未修改原array, 可操作任何可迭代对象;nums.sort()仅限列表, 返回值None, 会修改原表, space complexity depends. 会返回一个新的 list，也需要 O(k) 额外空间。
        # 推荐你用 left_results + right_results 这种写法，避免最后 sorted(results)。
# 方法二:
# findUpperClosest: O(log n)
# 扩展 k 个元素: O(k)
# 拼接结果: O(k)
# Total Time Complexity: O(log n + k)
# Space Complexity: O(k)    
# class Solution:
#     # TC: O(log n + k)
#     # SC: O(k)
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         right = self.findUpperClosest(arr, x)
#         left = right - 1
#         left_results = []
#         right_results = []
#         for _ in range(k):
#             if self.isLeftCloser(arr, x, left, right):
#                 left_results.append(arr[left])
#                 left -= 1
#             else:
#                 right_results.append(arr[right])
#                 right += 1
#         return left_results[::-1] + right_results # left_results是按从大到小收集的，所以 reverse 后变成升序, 而right_results本身就是升序

    def isLeftCloser(self, nums, target, left, right): # 现在应该选左边吗？
    # 注意本函数的边界检查容易遗漏
        # 如果左边已耗尽, 返回False
        if left < 0 :
            return False

        # 如果右边已经没有元素可以选了，那只能选左边，所以返回 True。
        if right >= len(nums):
            return True
        
        return target - nums[left] <= nums[right] - target
        # 此处有等号, 是因为如果左右距离相等时选左边
        
    # 第一步: 找中界线: 找到>=target的最左数字 or <=target的最右数字, 本题以前者为例, 用二分法模板. 时间复杂度O(log n)
    def findUpperCloset(self, nums, target): # 找第一个 >= target 的位置, 也就是 lower bound / insertion position。
        start, end = 0, len(nums) -1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target: # 更靠左的符合条件, 丢掉右边
                end = mid
            # mid < target: 更靠右的符合条件, 丢掉左边
            else:
                start = mid

        # 因为要找最左数, 所以这里需要先判断start 
        if nums[start] >= target:
            return start
        # 如果end不行, 再判断start
        if nums[end] >= target:
            return end

        # 找不到>=target的数, 说明数组里所有数都<target, 这时target应该插入到数组最后面, 也就是len(nums) 
        return len(nums)



    
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,2,3,4,5]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,4,5]\n4\n-1\n
# @lcpr case=end

#

