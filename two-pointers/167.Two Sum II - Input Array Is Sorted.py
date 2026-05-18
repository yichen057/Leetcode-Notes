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
    # 本题要注意两点: 1. 要求返回 1-indexed, 每个index+1; 2. 已知array是sorted的
    # 本题最好的方法是方法一: two pointers. 本题核心在于sorted array + target sum → two pointers
    # method 1: two pointers method
    # TC: O(n), 每次循环不是 left += 1，就是 right -= 1。两个指针最多总共移动 n 次
    # SC: O(1), 因为只用了几个变量: left, right, total
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: 
            return [-1, -1]
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1] # Return the indices of the two numbers index1 and index2, each incremented by one
            elif total < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

        # 双指针法(同时记录了原数组每个元素的index)
        #  if not numbers: 
        #     return [-1, -1]
        # num = [(number, index) for index, number in enumerate(numbers)] # 该num是为了记录num元素和其对应index, 本方法可以不记录index, 因为无需sort, 所以index不会被打乱
        # # 上面这句等价于下面这句
        # num = []
        # for index, number in enumerate(numbers):
        #     num.append((number, index))

        # left, right = 0, len(numbers) - 1
        # while(left < right):
        #     if num[left][0] + num[right][0] > target:
        #         right -= 1
        #     elif num[left][0] + num[right][0] < target:
        #         left += 1
        #     else:
        #         return [num[left][1]+1, num[right][1]+1 ]
            
        # return [-1, -1]

        # method 2: Hashmap method
        # TC: O(n); SC: O(n) 
        #  if not numbers: 
        #     return [-1, -1]
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            dictNum = {} # record each visited element(key) and its index (value)
            for i, num in enumerate(numbers):
                need = target - num
                if need in dictNum:
                    return [i+1, dictNum[need]+1]
                dictNum[num] = i # 注意此处方括号里是[num], 而不是平常写的[i], key是element不是index
            return [-1, -1]

        # method 3: brute force method
        # TC: O(n^2); SC: O(1) 
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            if not numbers: 
                return [-1, -1]
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i+1, j+1]
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

