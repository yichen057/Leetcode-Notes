#
# @lc app=leetcode id=560 lang=python3
# @lcpr version=30403
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (47.27%)
# Likes:    25182
# Dislikes: 855
# Total Accepted:    2.4M
# Total Submissions: 5.2M
# Testcase Example:  '[1,1,1]\n2\n[1,2,3]\n3'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
#from common.node import *

# @lc code=start
''' UMPIRE template

  # Understand
inputs:integer array: nums, and an integer: k
outputs: integer: number of subarrays, sum = k
constraints:
edge cases:
1) if nums is an empty list, return 0
2) if cannot find subarray total == k, which means no valid subarray, then return 0
3) all the values are the same in nums, only choose contiguous group and total == k

  # Match (any problems this reminds you of, any helpful patters to solve this e.g. two pointer technique, any data structures this reminds you of )
Use dictionary{prefix_sum: # of prefix_sum}
  # Plan (pseudocode)
 1. create a frequency map
 2. traverse the nums, calcualte the prefix_sum, if the prefix_sum == k: add the item and its frequency into the frequency map
 3. return the value of the frequency map

  # Implement (python code)

  # Review (dry run of your code)

  # Evaluate (time and space complexity)
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # freq_dic stores {prefix_sum: frequency}
        # We initialize with {0: 1} to handle cases where prefix_sum == k
        freq_dic = {0: 1}
# 为什么要初始化 {0: 1}？
# 如果你不初始化 {0: 1}，当你的 prefix_sum 第一次刚好等于 k 时，代码去 freq_dic 里找 0，会发现找不到，导致漏掉这个从 数组开头算起 的子数组。
# 初始化 {0: 1} 的含义是：在数组开始之前，我们已经默认有一个“和为 0”的前缀存在了 1 次。
        prefix_sum = 0 # prefix_sum：我现在一共走了多远？
        count = 0 # count：到目前为止，我一共找到了多少段符合要求的k？

        for val in nums:
            prefix_sum += val

            # Check if (prefix_sum - k) exists in our history
            # If (currentPrefixSum - k) exists in our map, it means the elements between that previous point and our current point sum exactly to k.
            diff = prefix_sum - k # diff：为了凑够 k，我需要找以前哪个位置？
            if diff in freq_dic:
                count += freq_dic[diff] # freq_dtc[diff]: 以前那个位置我经过了几次？（经过几次，现在就能连成几个 k）
# 为什么要 count += freq_dic[diff] 而不是 +1？
# 因为如果有多个位置的前缀和都是 diff（比如数组里有 0，导致总和没变），那么每一个这样的位置到当前位置都能组成一个符合条件的子数组。
            # Record this prefix_sum in the map
            freq_dic[prefix_sum] = freq_dic.get(prefix_sum, 0) + 1
        return count
    
#「Two Sum on Prefix Sum」区别在于two sum 存的是数字need = target - num; 本题prefix Sum 存的是前缀和: need = currSum - k
# 本题允许有负数或者0 + subarray sum equals k + count
# => prefix sum + hashmap

# TC: O(n), 因为遍历了一次数组
# SC: O(n+1), worst case: nums里的prefix sum全部不同, 存了n+1个key(包括0:1)
# prefix做题思想:
# 某个区间和subarraySum = currSum - prevSum, 我们希望currSum - prevSum = k, 于是 prevSum = currSum - k, 这里的prevSum必须来自当前位置之前, 而不能是当前位置自己, 否则会产生空子数组, 不满足题目要求的non-empty subarray
# 所以只要统计prefixSum出现过几次, 就可以求return的count. 因为每出现1次, 都对应不同的起点, 因此形成一个新的和为k的连续子数组
# 所以count += prefixCount[currSum - k]
# 换种表述: prefix[r] - prefix[l-1] = k, 移项后得到prefix[l-1] = prefix[r] - k
# 只要以前出现过前缀和为prefix[l-1], 那么从那个位置后开始到当前位置r, 一定构成一个和为k额子数组. 
# 我们统计的应该是nums[l...r], 而不是nums[r+1...r]这种不存在的区间
# - 面试问题: Why do we query(查找) before inserting the current prefix sum?
# - 回答: Because we only want to match the current prefix sum with previously seen prefix sums.
# If we insert first, the current prefix sum could match itself when k = 0, which corresponds to an empty subarray of length 0. Since the problem only counts non-empty subarrays, we must query before inserting.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        # We initialize with {0: 1} to handle cases where prefix_sum == k
        # the dictionary stores {prefix_sum: frequency}
        prefixCount = {0: 1} # 代表数组还没开始前, 前缀和为0, 出现过一次, 这样提前设置是为了后续如果计算和为0时, 可以更新统计其次数

        for num in nums: # TC: O(n). 先查后存, 避免自己和自己配对
        # 1. 算出当前前缀和
        # 2. 查找以前有没有满足条件的前缀和, 先用历史数据找答案
        # 3. 再把当前前缀和加入 HashMap. HashMap里只能存“历史prefix sum”, 不能把当前prefix sum, 拿来和自己匹配

            currSum += num

            # prefixCount[currSum] = prefixCount.get(currSum, 0) + 1 ! 错误示范! 不可先存后查, 否则会让当前 prefix sum 和自己匹配，从而产生一个长度为 0 的子数组。而 LeetCode 560 统计的是：non-empty continuous subarrays, 即长度>=1的子数组

            prefixSum = currSum - k 

            # Query the hashmap to see how many times currSum-k has appeared before.
            count += prefixCount.get(prefixSum, 0) # 注意:此处的prefixSum对应的是旧的prefixSum, 而不是最新的, 所有需要先查后存
            # 上述一行代码可以用下面两行代码展开写, 可读性更强
            # if prefixSum in prefixCount:
            #     count += prefixCount[prefixSum]

            # Insert the current prefix sum into the hashmap.
            prefixCount[currSum] = prefixCount.get(currSum, 0) + 1

        return count

# Follow up:
# 如果本题改成num全是正整数positive integers(不包括负整数和0), 可以用sliding window, 是可变长度窗口, 把空间从 O(n) 降到 O(1)；
# 但原题允许负数，因此通用解法必须使用 Prefix Sum + HashMap，空间复杂度 O(n)。
# sum < k  -> 扩大窗口
# sum > k  -> 缩小窗口 (坏了才缩)
# sum == k -> 

# TC = O(n), 因为for...while..., right最多走n次, left最多走n次
# SC = O(1), 因为只用了left, right, windowSum和count几个变量

# 模板代码:模板 B：变长窗口，求最长
# 题目: LC 3, LC 424, LC 1004, LC 904
# 关键词: longest substring/subarray ...最长满足某条件的连续区间
# 做题策略: right 不断扩大窗口; 如果窗口坏了，就移动 left 修复; 修好后更新最长答案
# 口诀: 求最长：坏了才缩。修好以后，更新最大长度。
# def longest_window(data):
#     left = 0
#     answer = 0
#     window_state = ...

#     for right in range(len(data)):
#         # Add right element.
#         ...

#         # Fix the window if it becomes invalid.
#         while window_is_invalid:
#             # Remove left element.
#             ...
#             left += 1

#         # Now the window is valid.
#         answer = max(answer, right - left + 1)

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         left = 0
#         windowSum = 0

#         for right in range(len(nums)):
#             windowSum += nums[right]
#             while windowSum > k:
#                 windowSum -= nums[left]
#                 left += 1
#             if windowSum == k:
#                 count += 1
#         return count    

# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here
    # test case 1
    nums1 = []
    k1 = 5
    print(f"Test1: {solution.subarraySum(nums1, k1)}") # Expected: 0
    nums2 = [1, 2, 5, 4]
    k2 = 13
    print(f"Test2: {solution.subarraySum(nums2, k2)}") # Expected: 0
    nums3 = [1, 1, 1, 1]
    k3 = 2
    print(f"Test3: {solution.subarraySum(nums3, k3)}") # Expected: 3



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

