#
# @lc app=leetcode id=15 lang=python3
# @lcpr version=30305
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (38.27%)
# Likes:    34784
# Dislikes: 3234
# Total Accepted:    5.5M
# Total Submissions: 14.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]\n[0,1,1]\n[0,0,0]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *


# @lc code=start
# 本题使用双指针方法: 3Sum用双指针是因为排序后自动去重最简洁(排序后相同的数相邻，continue跳过即可, 自动去重)，而字典需要额外的集合去重逻辑
class Solution:
# method 1该方法的去重思路是: 找到一个答案后，都先离开当前用过的位置, 然后跳过和刚才用过的值相同的元素，避免重复答案。
# Time complexity: O(n^2)
# Space complexity: O(n), Depends on language you use. In python, sorting algorithm use Timsort which uses O(n) space.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # List[List[int]]: 表示“整数列表的列表”——即外层是一个列表，里面每个元素又是一个 List[int]（一个整数序列）。用来表示多个三元组/数组的集合很常见。
        result = []
        nums.sort() # 排序是关键

        for i in range(len(nums)):
            # 如果第一个元素已经>0, 不需要进一步检查
            if nums[i] > 0:
                return result
            
            # 获取第一个数, 并对第一个数去重
            # 如果当前数和上一个数一样，说明这个数的情况已经处理过了，跳过。
            # 比如 [-1, -1, 0, 1]，处理完第一个 -1 后，第二个 -1 就不用再处理了。
            # Check if the current element is a duplicate of the previous element and skip it if it is
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 初始化双指针Initialize two pointers to point to the elements next to the current element i and at the end of the array, respectively.
            left = i + 1
            right = len(nums) - 1

            # 获取第二和第三个数并去重
            # 外层是“做查找”的循环，内层是“去重并保证边界”的循环，两者职责不同，不能省
            while left < right: # 此处right不能>=left, 因为一旦二者相等, 两个指针指向同一个位置, 那b和c就是一个数, 就不符合triple三元数组了, 所以left!=right
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # 找到一个解后
                    result.append([nums[i], nums[left], nums[right]]) # 会将一个列表作为元素添加到 result 中, append() 方法只接受 一个参数。如果传三个参数，会抛出 TypeError
                    # 找到答案并去重后，双指针同时收缩，准备找下一组
                    right -= 1
                    left += 1
                    # 去重是去除相同的三元组，不是去重数组本身。

                    # 对第二和第三个数即对nums[left]和nums[right]去重

                    # 对右指针去重：Decrement the right pointer to skip any duplicate elements.
                    # left < right 必须在内层也判断，防止跳过重复时指针交错（越界/变成无效区间）
                    while left<right and nums[right] == nums[right + 1]: # right 是往左移动的。所以新的 nums[right] 要和它右边刚刚经过的值比较
                        right -= 1 # 立即跳过所有重复的 right 值

                    # 对左指针去重：Increment the left pointer to skip any duplicate elements.
                    while left < right and nums[left] == nums[left - 1]: # left 是往右移动的。所以新的 nums[left] 要和它左边刚刚经过的值比较
                        left += 1 # 立即跳过所有重复的 left 值
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 方法二: set+tuple to remove duplicate triplets, then convert set of tuples to list of lists
        # TC: O(nlogn) + O(n^2) + O(k)), 因为最坏 k = O(n^2)，所以：O(n log n + n^2 + n^2) = O(n^2), where k is the number of unique triplets
        # SC: O(k) for set()+ O(k) for list of list=O(k), k是去重后的triplet数量, 最坏情况k = n^2, 所以worst case O(n^2), because setRes stores unique triplets
        setRes = set() # To remove duplicate triplets.它保存所有去重后的 triplets。假设结果数量是 k，那么：setRes space = O(k)
        nums.sort() # To use two pointers
        # nums.sort()这是 in-place 排序，不会新建一个新的 nums list。但 Python 的 Timsort 内部可能使用额外空间。面试/LeetCode 常见写法可以写：Ignoring sorting auxiliary space: O(k), Counting Python sort auxiliary space: O(n + k)

        #  for + while 总共的total time complexity = O(n^2)
        for i, a in enumerate(nums): # 最多跑 n 次
            print("i:", i)
            left, right = i + 1, len(nums)-1 # 注意left和right的初始化是在for loop里while loop外, left依赖于i
            while left < right: # 对每个固定的 i，left 和 right 总共最多移动 n 次。
                total = a + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    setRes.add((a, nums[left] , nums[right])) # set.add()底层是hash table, 平均插入时间是场数时间
                    # set无顺序, add只是加入集合, 并不像list.append是加到末尾
                    # set里只能装hashable and immutable element, 不可变的数据类型通常可以放进 set；可变的数据类型通常不能放进 set。tuple 可以放进 set, 前提是tuple里的元素也都是hashable, set里不能装list, dict和set, 可以装int, float, str, bool, tuple
                    print(setRes)
                    left += 1
                    right -= 1
                    print("after adding left: ",left)
                    print("after adding right: ",right)
        # return [[a,b,c] for (a,b,c) in setRes] 
        return [list(t) for t in setRes] # 上面的表达和本句, both can convert a set of tuples into a list of lists.
        # 本句的时间复杂度分析如下: 假设最终有 k 个 triplets，那么转换是O(k), 因为每个 tuple 长度固定是 3，所以每个转换是 O(1)。在最坏情况下，k 可能是 O(n^2)，所以这一步最坏是：O(n^2). 本句的空间复杂度, 因为是创建了一个list of list, 空间是O(k), 最坏情况下 k 可以到 O(n^2)，所以最坏空间复杂度是：O(n^2)
        
          
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    
    # Test case 1: Example from problem
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"Test 1: {nums1}") # f-string的主要用途：在字符串中直接嵌入变量或表达式
    print(f"Output: {result1}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]]")
    print()
    
    # Test case 2: No triplet sums to 0
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    print(f"Test 2: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: []")
    print()
    
    # Test case 3: All zeros
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    print(f"Test 3: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: [[0, 0, 0]]")
    print()
    
    # Test case 4: Additional test with negatives
    nums4 = [-2, 0, 1, 1, 2]
    result4 = solution.threeSum(nums4)
    print(f"Test 4: {nums4}")
    print(f"Output: {result4}")
    print()




#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

