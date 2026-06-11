#
# @lc app=leetcode id=454 lang=python3
# @lcpr version=30305
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (57.69%)
# Likes:    5064
# Dislikes: 151
# Total Accepted:    377.2K
# Total Submissions: 652.7K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n[0]\n[0]\n[0]\n[0]'
#
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:
# 
# 
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 
# 
# 
# Example 1:
# 
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
# 
# 
# Example 2:
# 
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
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
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 使用unordered_map存nums1和nums2中的元素及其和
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap: # n1+n2是key, if key exist这个和之前出现过, 则在原有的次数基础上+1; if not, n1+n2这个和是第一次出现, 字典里还没有这个key, 则将其出现次数初始化为1
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
                # 替代写法: hashmap[n1+n2] = hashmap.get(n1+n2, 0) +1, 这句话其实包含了 “先取、再加、最后存” 三个动作
                # 语法格式是：value = hashmap.get(key, default_value)
                # 取 (Get): hashmap.get(n1+n2, 0): 只是读取数值, 这个和出现过吗？没出现过就当做 0 次，出现过就返回旧次数
                # 加 (Add): ...+1, 在刚才取出的数字基础上加 1。
                # 存 (Set): hashmap[n1+n2] = ..., 把最新的次数更新回字典里
        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                targetKey = 0-(n3 + n4)
                if targetKey in hashmap:
                    count += hashmap[targetKey] #注意, 由于count本身统计的就是出现的次数, 此处count需要加出现的次数, 次数是value, 而不是count+1
        return count
          
# @lc code=end

if __name__ == '__main__':
# 1. 实例化对象, 创建类的实例
    solution = Solution()
    # your test code here

    
    # 2. 准备测试数据 (示例数据)
    # A + B = [1-2, 1-1, 2-2, 2-1] = [-1, 0, 0, 1] -> map: {-1:1, 0:2, 1:1}
    # C + D = [-1+0, -1+2, 2+0, 2+2] = [-1, 1, 2, 4] ->找相反数 1, -1, -2, -4
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    
    # 3. 调用函数并打印结果
    result = solution.fourSumCount(nums1, nums2, nums3, nums4) # 通过实例调用方法
    print(f"满足条件的元组个数: {result}") 
    
    # 预期输出应该是 2
    # 解释:
    # 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
    # 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0



#
# @lcpr case=start
# [1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n[0]\n[0]\n
# @lcpr case=end

#

