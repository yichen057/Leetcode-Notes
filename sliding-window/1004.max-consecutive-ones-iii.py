#
# @lc app=leetcode id=1004 lang=python3
# @lcpr version=30403
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (67.74%)
# Likes:    10544
# Dislikes: 193
# Total Accepted:    1.4M
# Total Submissions: 2.1M
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2\n[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3'
#
# Given a binary array nums and an integer k, return the maximum number of
# consecutive 1's in the array if you can flip at most k 0's.
# 
# 
# Example 1:
# 
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# 
# Example 2:
# 
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is
# underlined.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# method 1: sliding window + frequency map
# Time Complexity: O(N), where N is the number of elements in the array. In worst case we might end up visiting every element of array twice, once by left pointer and once by right pointer.
# Space Complexity: O(1). We use constant space.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        ans = 0 
        l = 0
        freq_map = {}
        for r in range(len(nums)):
            # 加入 nums[r] 之前的窗口，如果合法，已经更新过答案；
            freq_map[nums[r]] = freq_map.get(nums[r], 0 ) + 1
           
            while nums[r] == 0 and freq_map[nums[r]] > k: # 注意: 此处用while, 加入 s[r] 之后如果非法，就固定 r，移动 l，直到当前窗口重新合法；
           
                #freq_map[nums[r]] -= 1 # 错误写法!
                freq_map[nums[l]] -= 1 # 注意, 这里是remove nums[left] 而不是remove nums[right]
                l += 1

            ans = max(ans, r - l + 1) # 以 r 结尾的合法窗口长度更新ans。

        return ans

# method 2: sliding window + count
# Time Complexity: O(N), where N is the number of elements in the array. In worst case we might end up visiting every element of array twice, once by left pointer and once by right pointer.
# Space Complexity: O(1). We do not use any extra space.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, ans, curr = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                curr += 1
            while curr > k:
                # if nums[r] == 0: 错误!
                if nums[l] == 0:
                    curr -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

