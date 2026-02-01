#
# @lc app=leetcode id=18 lang=python3
# @lcpr version=30305
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (39.63%)
# Likes:    12656
# Dislikes: 1525
# Total Accepted:    1.5M
# Total Submissions: 3.9M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0\n[2,2,2,2,2]\n8'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# Example 2:
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *

#本题的时间复杂度: O(n³). 虽然代码里只有两个 for 循环，但里面的 while (left < right) 本质上也是一层循环**，
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort() # 时间复杂度: O(n log n)
        n = len(nums)
        # The first for loop
        for k in range(n): # 时间复杂度: O(n)
            # 对nums[k]剪枝处理
            if nums[k] > target and nums[k] >0 and target > 0:
                break # 这里使用break，统一通过最后的return返回
            # 对nums[k]去重处理: 在前任k-1的时候，通过内部那个 exhaustive（穷尽的）双指针搜索，已经全部确定并存档了。
            # 前任 (k-1)：我有更广阔的视野（后面所有数字），我能找到的组合是最全的。
            # 现任 (k)：我和前任长得一样（值相同），但我能看到的范围（候选数字）比他还小。既然他把“以 -1 为首”的所有组合都找出来了，我再找也找不出新花样，只能找出重复的旧账。
            #所以，直接 `continue` 跳过，是为了防止录入重复的答案，而不是因为没找到答案
            if k > 0 and nums[k] == nums[k-1]:
                continue
            # The second for loop
            for i in range(k+1, n): # 时间复杂度: O(n)
                # 对nums[i]剪枝处理:
                if nums[k] + nums[i] > target and target > 0:
                    break
                # 对nums[i]去重处理:
                if i > k + 1 and nums[i] == nums[i-1]:
                    continue

                # 以下是left/right指针移动, 同三数之和逻辑, 参考题目15
                # 初始化双指针
                left, right = i+1, n-1
                # 获取第三和第四个数并去重
                while right > left: # 时间复杂度: O(n)
                    total = nums[k] + nums[i] + nums[left] + nums[right]
                    if total == target:
                        # 找到一个解后, 立即做left和right去重后收缩指针
                        result.append([nums[k], nums[i], nums[left], nums[right]]) # 会将一个列表作为元素添加到 result 中, append() 方法只接受 一个参数。如果传三个参数，会抛出 TypeError
                        # 立即跳过所有重复的left值, 对左指针(即第三个数)去重
                        # right > left 必须在内层也判断，防止跳过重复时指针交错（越界/变成无效区间）
                        while right > left and nums[left] == nums[left+1]:
                            left += 1
                        # 立即跳过所有重复的right值, 对右指针(即第四个数)去重
                        while right > left and nums[right] == nums[right-1]:
                            right -= 1
                        # 去重是去除相同的三元组，不是去重数组本身。
                        # 找到答案并去重后，双指针同时收缩，准备找下一组
                        right -= 1
                        left += 1
                    elif total < target:
                        left += 1
                    else: 
                        right -= 1
        return result
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

