#
# @lc app=leetcode id=665 lang=python3
# @lcpr version=30400
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (25.36%)
# Likes:    5852
# Dislikes: 788
# Total Accepted:    291.8K
# Total Submissions: 1.2M
# Testcase Example:  '[4,2,3]\n[4,2,1]'
#
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.
# 
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).
# 
# 
# Example 1:
# 
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# Example 2:
# 
# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one
# element.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# **Arrays (数组) + Greedy (贪心算法)**
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0 # 统计修改次数
        for i in range(len(nums)-1):
        # 第一层：这是你最关心的【前后比较】. 只要这行不成立，说明数组还是非递减的，程序会直接跳到下一个 i
            if nums[i] > nums[i+1]:
                count += 1 # 发现断层, 记录一次修改
                if count > 1:
                    return False
                
                # 第二层：这是【决策比较】: 只有在“发现断层”后，也就是前提条件是nums[i]>nums[i+1]我们才开启这个逻辑，决定如何修改
# 假设数组是 `[1, 4, 2]`：
# 1. 前后比较**：发现 `4 > 2`（`nums[i] > nums[i+1]`）。**断层确认！**
# 2. 决策时刻**：我们要改掉 `4` 或者 `2`。
# 3. 如果拿 `nums[i+1]`(2) 和 `nums[i]`(4) 比**: 比出来的结果肯定是 `2 < 4` 啊！这无法帮你决定是把 `4` 变小还是把 `2` 变大。
# 4. 拿 `nums[i+1]`(2) 和 `nums[i-1]`(1) 比：结果是 `2 >= 1`。
#    - **结论**：哪怕我把 `4` 削矮成 `2`，它依然比前面的 `1` 大。**最优决策**：削矮 `4`。

                # 如果是首对逆序，或者修改 nums[i] 就能解决问题
                if i == 0 or nums[i+1] >= nums[i-1]: # i == 0 是为了处理数组开头的特殊情况，防止程序在尝试回头看 `nums[i-1]` 时崩溃（报错 `IndexError`），同时也涵盖了一个重要的逻辑决策
                    pass # 方案 A：削矮 nums[i]，对未来无影响，所以 pass. 想象中修改了 nums[i] = nums[i + 1]，对下一次 i+1 和 i+2 的比较没有副作用，所以不用写
                    # 变小的是“过去”，不影响“未来”（`2` 还是小于 `5`）
                else:
                    nums[i+1] = nums[i] # # 方案 B：垫高 nums[i+1]，影响未来. 必须调大 nums[i + 1]，这会影响下一轮循环. 变大的是“未来”，必须更新，否则下一轮拿旧的 `2` 去比 `3` 就漏判了
                    # 找错：只允许出现一次 nums[i] > nums[i + 1]。改错：优先把大的调小；如果调小会导致比前面还小，就只能把小的调大。
        return True      

# **“把大的变小”永远比“把小的变大”更安全**。
# 当第一个元素 `nums[0]` 比第二个元素 `nums[1]` 大时：
# - 我们面前没有任何障碍（没有 `nums[-1]` 需要顾虑）。
# - 我们可以**无条件**地把 `nums[0]` 削减到和 `nums[1]` 一样大。
# - 这样改完后，`nums[0]` 和 `nums[1]` 齐平了，且不会破坏任何“前序关系”（因为前面根本没数）。   
### 如果不写 `i == 0` 会发生什么？
# 假设数组是 `[4, 2, 1]`：
# 1. **i = 0**：发现 `4 > 2`。
# 2. **如果没有 `i == 0` 直接走 `else`**：程序去比 `nums[1]`(2) 和 `nums[-1]`(1)。
# 3. **结果**：`2 > 1`（不满足 `nums[i+1] >= nums[i-1]`），程序会执行 `else` 里的 `nums[i+1] = nums[i]`，即把 `2` 改成 `4`。
# 4. **数组变成**：`[4, 4, 1]`。
# 5. **下一轮**：发现 `4 > 1`，`count` 变成 2，返回 `False`。**这是对的。**

# **但是！** 换个例子：`[4, 2, 3]`
# 1. **i = 0**：发现 `4 > 2`。
# 2. **如果不写 `i == 0`**：比 `nums[1]`(2) 和 `nums[-1]`(3)。
# 3. **结果**：`2 < 3`。程序走 `else` 把 `2` 改成 `4`。
# 4. **数组变成**：`[4, 4, 3]`。
# 5. **下一轮**：发现 `4 > 3`，返回 `False`。
# 6. **错误！** 这个数组明明改一次就能变好（改成 `[2, 2, 3]`），结果你因为没写 `i == 0` 导致决策错误，判定成了 `False`
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here




#
# @lcpr case=start
# [4,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,1]\n
# @lcpr case=end

#

