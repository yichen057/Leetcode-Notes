#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (49.87%)
# Likes:    13766
# Dislikes: 515
# Total Accepted:    1.6M
# Total Submissions: 3.2M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to
# target. If there is no such subarray, return 0 instead.
# 
# 
# Example 1:
# 
# 
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
# 
# 
# Example 2:
# 
# 
# Input: target = 4, nums = [1,4,4]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#

# @lc code=start
# 这题最关键的点就是：当窗口已经满足 window_sum >= target 时，要用 while 不断移动左指针，尝试把窗口缩到最短。什么时候用 while 移动左指针？你可以用这个规则判断：如果移动一次左指针后，窗口可能仍然满足条件，并且你还想继续优化答案，就用 while。
# sliding window的优化点是: 
# 右指针不回头, 不需要让右指针回到左指针；
# 左指针也不回头；
# 通过维护 window_sum 来复用之前计算过的信息。

# 本题核心口诀: 可变窗口求最短：通常用 while valid
# sum 不够，right 继续扩。
# sum 够了，left 一直缩，直到不够为止。
# 每次缩之前都更新最短长度。
# 模板:
# while window_sum >= target:
#     update answer
#     remove left
#     l += 1

# 如果固定长度窗口：通常 if 就够:因为每轮右边只加入一个元素，窗口最多只会超长 1。所以移出一个左边元素就一定恢复到长度 k。
# 模板:
# if r - l + 1 > k:
#     remove left
#     l += 1
class Solution:
    # Variable-size Sliding Window: minimum valid window
    # TC: O(n), because both left and right pointers only move forward.
    # SC: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window_sum = 0
        minLen =float('inf') # 求最短，用 inf。最后没更新过，再返回 0 或空结果。
# 极值初始化口诀:
# 最长长度从 0 开始。
# 最短长度从 inf 开始。
# 最大/最小数值最好用第一个真实窗口初始化。
# 如果可能全负数，max 不要初始化为 0。

        for r in range(len(nums)):
            #print("r:",r)
            # Expand the window by adding nums[right].
            window_sum += nums[r]
            #print("current window_sum:", window_sum)

            # 此处使用while是因为要考虑能不能去掉左边一个元素, 移动一次左指针后，sum 仍然 >= target, 即窗口可能仍然invalid？如果仍然 >= target，说明窗口还能更短, 那就继续去掉左边。
            # If the current window satisfies the condition,
            # keep shrinking it from the left to find the shortest valid window.
            while window_sum >= target:
                minLen = min(minLen, r-l+1)
                #print("current minLen", minLen)
                #print("before move l",l)
                # Remove nums[left] from the window.
                window_sum -= nums[l]
                #print("after remove left window_sum:", window_sum)
                l += 1
                #print("after move l:",l)
                
        return 0 if minLen == float('inf') else minLen

# @lc code=end

