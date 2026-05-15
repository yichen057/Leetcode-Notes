#
# @lc app=leetcode id=128 lang=python3
# @lcpr version=30403
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.09%)
# Likes:    22972
# Dislikes: 1243
# Total Accepted:    3.3M
# Total Submissions: 7M
# Testcase Example:  '[100,4,200,1,3,2]\n[0,3,7,2,5,8,4,6,0,1]\n[1,0,1,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# Example 3:
# 
# Input: nums = [1,0,1,2]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
#from common.node import *

# @lc code=start
class Solution:
    # method 1: set + length control
    # TC = O(n), SC = O(n)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numSet = set(nums) # 用set去装nums的元素, 后面lookup O(1)方便查. 本行在做list->set: 时间和空间复杂度都是O(n), 因为需要遍历nums一遍
    #     longest = 0
    #     for n in numSet: # !注意这里traverse的是numSet, 不是nums. 否则相同元素在数组里有很多个的话, 容易造成程序超时
    #     # outer loop: 时间复杂度O(n)
    #         # check if its the start of a sequence. 1st value of a sequence has no left neighbor.
    #         if (n-1) not in numSet: # 说明他是序列的第一个元素
    #             length = 0 # 初始化序列长度为0
    #             print("this cycle is: ", n)
    #             while (n + length) in numSet: # 判断其之后的元素是否在numset里
    #                 # 虽然有 while 循环，但 while 只从每个连续序列的起点开始扩展，不会对每个元素重复扩展。
    #                 # 只有当 n 是一个连续序列的起点时，才进入 while, 不会重复值扫描。
    #                 length += 1 # 这里的 length 每次 += 1 之后，下一轮 while 判断时会用新的 length 值。
    #                 # length += 1 同时有两个作用：1. 记录当前序列长度 2. 让下一轮去检查下一个数字
    #                 print("while loop length: ", length)
    #                 # 如果nums=[100, 4, 200, 1, 3, 2]时, while检查时:
    #                 # 100 → 101 停
    #                 # 200 → 201 停
    #                 # 1 → 2 → 3 → 4 → 5 停
    #                 # 整体上，每个数字最多被 while “作为连续序列的一部分”检查一次。
                    
    #             if length > longest:
    #                 longest = length
    #                 print("This cycle longest length is", longest)
    #             # longest = max(length, longest) # 上面两行和这一行的最大值取值相同效用
    #     return longest

    # method 2: set + consecutive element control, 推荐!
    # TC = O(n), SC = O(n)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numSet = set(nums)
    #     longest = 0
    #     for n in numSet:
    #         if (n-1) not in numSet:
    #             m = n + 1
    #             while m in numSet:
    #                 m += 1
    #             longest = max(m-n, longest)
    #     return longest
    
    # method 3: sort + sliding window (本题不适用, 因为不满足题目要求, 纯当练手)
    # 本方法的主要问题是每个 i 都重新向后扫描，造成重复计算, 时间复杂度太高, 会超时报错Time Limit Exceeded
    # TC = O(n^2), SC = O(n)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     sortedNums = sorted(set(nums)) # sorted()不会修改原表, 会新建一个列表, 利用set过滤重复值
    #     # 这行代码的时间复杂度=O(n) + O(m log m) , 最坏情况下m=n,所以是O(n log n) (因为m<=n)), 其中set(nums):O(n); sorted():O(m log m)
    #     # 空间复杂度 = O(n), 其中set(nums): O(m) ; sorted()=O(n), 会新建一个排序后的list, 也需要O(m). 最坏情况下所有元素都不重复m=n, 所以空间复杂度是O(n)

    #     longest = 0
    #     # 以下的for+while循环, 由于每次i变化时j都从i+1开始, 所以会重复扫描, 总次数= m*(m-1)/2, 所以最坏情况下, m=n, 时间复杂度: O(m^2)
    #     for i in range(len(sortedNums)): 
    #         # print("i: ", i)
    #         j = i + 1
    #         # print("j: ", j)
    #         while j < len(sortedNums) and sortedNums[j] - sortedNums[j-1] ==1 : # 注意: 得写j<len(..) 否则当i=len(sortedNums)-1时, j会越界
    #             j += 1
    #         # print("after while, j:", j, "i: ", i)
    #         longest = max(j-i, longest)
    #         # print("length is ", longest)
    #     return longest

    # method 3的优化版1: sort + sliding window
    # TC = O(n log n), SC = O(n)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     sortedNums = sorted(set(nums)) # 不会修改原表, 会新建一个列表, 利用set过滤重复值
    #     # 这行代码的时间复杂度=O(n) + O(m log m) = O(n log n) (因为m<=n)), 其中set(nums):O(n); sorted():O(m log m)
    #     # 空间复杂度 = O(n), 其中set(nums): O(n) 最坏情况下所有元素都不重复; sorted()=O(n), 会新建一个排序后的list

    #     longest = 0
    #     # 以下的while循环, 由于由i = j已经控制住了不会重复扫描, 总次数= m, 最坏情况下m=n, 所以时间复杂度O(n)
    #     i = 0
    #     while i < len(sortedNums):
    #         j = i + 1
    #         while j < len(sortedNums) and sortedNums[j] - sortedNums[j-1] ==1 : # 注意: 得写j<len(..) 否则当i=len(sortedNums)-1时, j会越界
    #             j += 1
    #         longest = max(j-i, longest)
    #         i = j
    #     return longest
    
    # method 3的优化版2: 排序后一次遍历, 推荐!
    # Time:  O(n log n); Space: O(n)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0

    #     sortedNums = sorted(set(nums))
    #     # 注意: 这里初始化的值是1, 一定要注意!!!
    #     longest = 1 
    #     curLen = 1

    #     for i in range(1, len(sortedNums)):
    #         if sortedNums[i] - sortedNums[i - 1] == 1:
    #             curLen += 1
    #         else:
    #             curLen = 1

    #         longest = max(longest, curLen)

    #     return longest

    # method 4: Sort directly and handle duplicates without using Set
    # TC: O (n log n) for sorting + O(n) for traversal = O(n log n); 
    # SC: O(1) for extra variables or O(n): nums.sort() modifies the list in-place, but Python sorting may still use auxiliary memory internally.
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        curLen = 1
        nums.sort() # sort()仅限列表, 返回值None, 会修改原表
        for i in range(1, len(nums)):
            # print("initial i:", i)
            if nums[i] == nums[i-1]: # dealing with duplicates this time, we should memorize the curLen previously counted instead of equals 1.
                continue
            # if nums[i] != nums[i - 1]:同上面的处理, just for reference
            #     curLen = 1
            elif nums[i] - nums[i-1] == 1:
                curLen += 1
            else:
                curLen = 1
            # print("curLen: ", curLen)
            longest = max(longest, curLen)
            # print("longest: ", longest)
        return longest



# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#

