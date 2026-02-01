#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (76.76%)
# Likes:    6631
# Dislikes: 2331
# Total Accepted:    1.6M
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 方法一: set方法:
        number_set = set() # 这个number_set是新创建的set哈希表, 用来存储nums1里的所有元素
        for i in nums1:
            number_set.add(i) # 把元素 i 本身加入到集合 number_set 中，而不是 “加索引为 i 的值”。


        result = set() # 结果直接用set, 自动去重
        for i in nums2: # 遍历nums2, 去number_set检查nums2的元素是否出现过
            if i in number_set: # 如果出现过, 放入去重的result集合里
                result.add(i) # set的添加用add, list的添加用append9
        
        return list(result) # set -> list, 返回的是list, 不要忘记转换
    
        # 方法二: 数组方法:
        number_set = [0]* 1001 # 题目限制 0 <= num <= 1000
        result = set()

        for i in nums1: # 遍历 nums1，把每个数出现的次数记录到 number_set[i], nums1 里出现过的数作为新set的索引
            number_set[i] =1 # i 代表number_set这个数组的索引
# 标记存在性, 而不是计数数组. 如果写 number_set[num] += 1，那它就变成了 计数数组，存的是出现次数。
# 索引：是 nums1 里的每个元素值。
# 存的值：是“出现过没有”。
# =1 表示出现过一次或多次。
# 如果要统计次数，就用 +=1。
        for i in nums2: # 检查nums2里的数是否出现在nums1里
            if number_set[i] == 1:
                result.add(i)
                           
        return list(result)

# # 注意这种写法不对for i in len(nums1): ❌
# # 在 Python 里，len(nums1) 返回的是整数，不能直接迭代。
# # 正确写法是 for i in range(len(nums1)): 或者更 Pythonic 的 for num in nums1:。
# @lc code=end