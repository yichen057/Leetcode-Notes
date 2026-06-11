#
# @lc app=leetcode id=3507 lang=python3
#
# [3507] Minimum Pair Removal to Sort Array I
#
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/
#
# algorithms
# Easy (55.69%)
# Likes:    191
# Dislikes: 44
# Total Accepted:    54.6K
# Total Submissions: 93K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array nums, you can perform the following operation any number of
# times:
# 
# 
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs
# exist, choose the leftmost one.
# Replace the pair with their sum.
# 
# 
# Return the minimum number of operations needed to make the array
# non-decreasing.
# 
# An array is said to be non-decreasing if each element is greater than or
# equal to its previous element (if it exists).
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,2,3,1]
# 
# Output: 2
# 
# Explanation:
# 
# 
# The pair (3,1) has the minimum sum of 4. After replacement, nums =
# [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# 
# 
# The array nums became non-decreasing in two operations.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,2]
# 
# Output: 0
# 
# Explanation:
# 
# The array nums is already sorted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # # 方法一: 统一写在一个函数里. 
        # 时间复杂度为O(n²). 每轮耗时 = for循环(n) + pop(n) = 2n; 总共最多 n-1 轮, 所以总耗时 = (n-1) × 2n = 2n² - 2n; 用大 O 表示法，忽略常数和低阶项：O(2n² - 2n) = O(n²)
        # 注: for 和 pop 是相加不是取其一，但因为都是 O(n)，最终结果一样。
        #
        # result = 0 # 操作次数初始化为0

        # while True: # 外层 while：最多执行 n-1 次（数组从 n 个元素变成 1 个
        #     # 找最小和的同时, 顺便检查是否有序
        #     min_sum = float('inf') # 最小值的初始化为无穷大
        #     min_idx = 0 # 记录最小和的位置
        #     is_sorted = True

        #     # 一次遍历, 同时做两件事
        #     # 内层 for：每次 O(n)
        #     for i in range(len(nums) - 1): # 注意: 此处i是index, 不是元素, 所以不能用for i in (len(nums) - 1):
        #         if nums [i] > nums [i+1]: # 判断是否是非递减数组的, 如果前面的比后面大，就不是非递减
        #             is_sorted = False #不是非递减数组, 可以找接着找相邻元素的最小和的位置了
        #         # 找相邻元素的最小和
        #         pair_sum = nums[i] + nums[i+1]
        #         if pair_sum < min_sum:
        #             min_sum = pair_sum
        #             min_idx = i
            
        #     # 遍历完所有元素后, 认定该数组是非递减数组, 说明result = 0
        #     if is_sorted:
        #         break

        #     # 找到相邻元素的最小和后, 合并这两个元素为他们的和, 第二个元素作pop移除
        #     nums[min_idx] = min_sum
        #     # pop 操作：从中间删除元素，需要移动后面的元素，也是 O(n)
        #     nums.pop(min_idx + 1)
        #     # 操作次数+1
        #     result += 1
        
        # return result

        # 方法二: 利用辅助函数来检查数组是否为非递减. 时间复杂度：O(n²)，因为每次操作都要遍历数组
        def is_sorted():
            for i in range(len(nums) -1):
                if nums[i] > nums[i + 1]: # 如果前面的比后面大，就不是非递减
                    return False
            return True
        
        ans = 0 # 记录操作次数

        # 只要数组还不是非递减的，就继续操作
        while not is_sorted(): # while第1层：最多 n-1 次. 操作a: is_sorted() 遍历数组，O(n). 
        # for i in range(n): range(n) 不是每轮都重新算; while not is_sorted(): is_sorted() 每轮都要重新调用！所以 is_sorted() 每轮都会执行，它就是 while 循环的一部分
        # 每轮 while 的耗时: 操作a+操作b+操作c = n+n+n= 3n
        # while 执行次数：最坏情况下，每次只合并两个元素，数组长度从 n 变成 1，需要 n-1 次。
        # 总耗时: (n-1) × 3n = 3n² - 3n, 忽略常数 3 和低阶项 -3n：O(3n² - 3n) = O(n²)
            min_sum = float('inf') # 初始化为无穷大
            min_idx = 0 # 记录最小和的位置

            for i in range(len(nums) -1): # 操作b: 遍历数组，O(n)
                pair_sum =nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i
                
            # 合并：把 nums[min_idx] 和 nums[min_idx+1] 替换成它们的和
            nums[min_idx] = min_sum
            nums.pop(min_idx + 1) # 删除后面那个元素. 操作c: 删除元素，O(n)

            # 操作次数+1
            ans += 1

        return ans

# @lc code=end

