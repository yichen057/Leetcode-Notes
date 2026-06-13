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
# 3Sum:[nums[i], nums[left], nums[right]]
# 固定 nums[i]
# 用 left / right 找另外两个数

# 4Sum:([nums[k], nums[i], nums[left], nums[right]])
# 固定 nums[k]
# 固定 nums[i]
# 用 left / right 找另外两个数
# 代码结构如下:
# nums.sort()

# for k in range(n):              # 固定第 1 个数 nums[k]
    # if k > 0 and nums[k] == nums[k - 1]: # 第一层去重, 跳过重复的第一个数nums[k]
    #     continue
#     for i in range(k + 1, n):   # 固定第 2 个数 nums[i]
        # if i > k + 1 and nums[i] == nums[i - 1]: # 第二层去重, 跳过重复的第二个数nums[i], 且对于每一个固定的 k，i 是从 k + 1 开始的。
        #     continue
# # 在 i 后面的部分，用 left/right 找两个数，使四数之和等于 target: nums[left] + nums[right] == target - nums[k] - nums[i]
#         left = i + 1            # 第 3 个数
#         right = n - 1           # 第 4 个数

#         while left < right:
#             total = nums[k] + nums[i] + nums[left] + nums[right] # 因为 left 和 right 在 while 里面不断变化,所以total 要放在 while内
#             # 情况一: 找到答案, 然后移动指针两边都往中间收缩，继续找下一组, 然后再需要去重left/right
#             if total == target: 
#                 1) 找到一个quadruplet, 加入答案
#                 result.append([nums[k], nums[i], nums[left], nums[right]])
#                 2) 移动指针
#                 left += 1
#                 right -= 1
#                 3) 移动指针后去重 left/right:
#                 while left < right and nums[left] == nums[left + 1]:
                #     left += 1

                #   while left < right and nums[right] == nums[right - 1]:
                #     right -= 1

#             elif total < target:
#                 left += 1

#             else:
#                 right -= 1
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        # The first for loop
        for k in range(n):
            # 对nums[k]剪枝处理pruning(在排序后，如果已经可以确定后面不可能再找到答案，就提前停止，少做无用循环):
            # 如果数组排序后, 当前第一个数nums[k]已经比target大，而且它是正数，target也是正数，那么后面不可能再凑出target了，可以直接结束外层循环。
            # 这里的nums[k]>0判断多余, 可以省略. 这句不写也没问题, 不写更稳, 因为剪枝只是优化，不是必须。
            if nums[k] > target and nums[k] >0 and target > 0:
                break # 这里使用break，统一通过最后的return返回
            # 对nums[k]去重处理: 在前任k-1的时候，通过内部那个 exhaustive（穷尽的）双指针搜索，已经全部确定并存档了。
            # 前任 (k-1)：我有更广阔的视野（后面所有数字），我能找到的组合是最全的。
            # 现任 (k)：我和前任长得一样（值相同），但我能看到的范围（候选数字）比他还小。既然他把“以 -1 为首”的所有组合都找出来了，我再找也找不出新花样，只能找出重复的旧账。
            #所以，直接 `continue` 跳过，是为了防止录入重复的答案，而不是因为没找到答案
            if k > 0 and nums[k] == nums[k-1]:
                continue
            # The second for loop, 注意这个second loop要和上面的if对齐, 而不是和continue对齐
            for i in range(k+1, n):
                # 对nums[i]剪枝处理:
                # 固定了 nums[k] 和 nums[i] 之后，如果这两个数加起来已经大于正数 target，那么后面再加 left/right 只会更大，所以可以停止当前 i 循环。
                if nums[k] + nums[i] > target and target > 0:
                    break
                if i > k + 1 and nums[i] == nums[i-1]: # 跳过第二个数的重复值
                    continue

                # 以下是left/right指针移动, 同三数之和逻辑, 参考题目15. 注意下面的two pointers要和上面的if对齐, 而不是和continue对齐
                # 初始化双指针
                left, right = i+1, n-1
                # 获取第三和第四个数并去重
                while right > left:
                    total = nums[k] + nums[i] + nums[left] + nums[right]
                    if total == target:
                        # 找到一个解后
                        result.append([nums[k], nums[i], nums[left], nums[right]]) # 会将一个列表作为元素添加到 result 中, append() 方法只接受 一个参数。如果传三个参数，会抛出 TypeError

                         # 找到答案后，双指针同时收缩，准备找下一组
                        right -= 1
                        left += 1

                        # 立即跳过所有重复的left值, 对左指针(即第三个数)去重
                        # right > left 必须在内层也判断，防止跳过重复时指针交错（越界/变成无效区间）
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        # 立即跳过所有重复的right值, 对右指针(即第四个数)去重
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                        # 去重是去除相同的三元组，不是去重数组本身。
                       
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

