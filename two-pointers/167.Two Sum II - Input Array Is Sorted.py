#
# @lc app=leetcode id=167 lang=python3
# @lcpr version=30202
#
# [167] Two Sum II - Input Array Is Sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (63.77%)
# Likes:    12804
# Dislikes: 1489
# Total Accepted:    2.9M
# Total Submissions: 4.5M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
# 
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2.
# 
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
# 
# Your solution must use only constant extra space.
# 
# 
# Example 1:
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
# return [1, 2].
# 
# 
# Example 2:
# 
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
# return [1, 3].
# 
# 
# Example 3:
# 
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
# return [1, 2].
# 
# 
# 
# Constraints:
# 
# 
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
# 
# 
#

# @lc code=start

class Solution:
    # 双指针法: 时间复杂度O(n); 空间复杂度O(n):因为新建了一个 num 列表
#     构造 num：for 循环一次 → O(n)。
# 双指针扫描：left 和 right 各最多走 n 步 → O(n)。
# 👉 总时间复杂度：
# 输入有序：O(n)
# 输入无序 + 排序：O(n log n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: 
            return [-1, -1]
        
        num = [
            (number, index)
            for index, number in enumerate(numbers) # 注意: 此处没有冒号
        ]
        # 上述语句等同于下面的: 注意冒号加的位置
        # num = []
        # for index, number in enumerate(numbers):
        #     num.append((number, index))

        left, right = 0, len(numbers) - 1
        while(left < right):
            if num[left][0] + num[right][0] > target:
                right -= 1
            elif num[left][0] + num[right][0] < target:
                left += 1
            else:
                return [num[left][1]+1, num[right][1]+1 ]
            
        return [-1, -1]
    
    # 哈希表法: 时间复杂度和空间复杂度都为O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: 
            return [-1, -1]
        
        hash = {}
        for index, number in enumerate(numbers):
            if target - number in hash:
                return [hash[target - number] + 1, index + 1]
            hash[number] = index

        return [-1, -1]
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#

