#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30202
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (56.18%)
# Likes:    63808
# Dislikes: 2327
# Total Accepted:    18.5M
# Total Submissions: 33M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
# 
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

# @lc code=start
# 求元素, 哈希表做法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        hashset = set()
        for num in nums:
            # [2,4,5], target = 8, 如果在这里直接给hashset添加元素, 会错误返回[4,4]
            if target - num in hashset:
                return num, target-num #返回的是两个元素num和(target-num)
            hashset.add(num)
        return [-1, -1] 

# 求索引, hashmap做法, 时间复杂度是O(n), 空间复杂度由于额外用了一个dict来存储数值和索引, 所以空间复杂度是O(n)
# 对于需要返回所找的两个数在数组中的下标(即索引)时, 哈希表算法比双指针算法更好, 因为双指针需要将下标和值同时进行排序
# 本题的五个重点: 
# 1) 为什么使用哈希表做法? 当遍历到某元素a时, 想判断(target-a)是否之前遍历过.
#    而当判断元素是否在集合里出现过, 就要用哈希法和哈希表结构. 把遍历过的元素加到一个集合里, 这个集合就要用到哈希表的结构
#    如果之前遍历过, 那么就找到了一对, 可以直接return下标; 如果未遍历过, 则把当前元素a加入到map集合中;
# 2) 为什么使用map: 存放(元素, 索引), 用map(key, value), map[key] = value
# 3) 为什么使用unordered map: 因为其底层是哈希结构, 可以直接做映射, 而map和multi-map的底层为红黑树;
# 4) map的作用是什么: 用来存放遍历过的元素;
# 5) map的key和value是用来做什么的: 因为map可以最快时间查找key是否在map里出现过, 因此元素作为key, 下标索引作为value.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        hash = {} # 用hash存{数值: 索引}的映射. 是Python 的哈希表，适合做 快速查找、映射、统计。
        # 推荐方法一: enumerate()
        for i, num in enumerate(nums): # i = index, num = current value, 遍历数组一次, 时间复杂度是O(n)
        # 这里 enumerate(nums) 返回一个迭代器，里面是 (索引, 元素) 的元组, 注意不是(元素, 索引). 这就是为什么for循环里要写成i, num。
        # 在 Python 里，遍历列表时默认只能拿到值, 如果还想要下标，就要用 enumerate()：. 
        # enumerate() 用来同时拿到 索引 + 值，比 range(len(nums)) 更优雅。
        # 所以 for i, num in enumerate(nums) 会自动解包成 i 和 num。
            if target - num in hash: # 哈希表查找，平均时间复杂度 O(1)。
                return [hash[target - num], i] # 返回的是两个数的索引, num的索引i和(target-num)的索引hash[target-num]
            hash[num] = i # 没出现过就存到hash里, 表示key: 当前数值num; value: 它的索引是i. 哈希表插入, 时间复杂度是O(1)
        # 方法二: range(len(nums))
        # for i in range(len(nums)):# 循环nums数值, 并添加映射, i是索引'''
        #     if target - nums[i] in hash:
        #         return [hash[target - nums[i]], i]
        # 无解的情况
        return [-1, -1]   

# 求元素, 双指针+排序算法, 如果题目中数组的无序的, 那么时间复杂度O(nlogn)+O(n)=O(nlogn); 
# 如果输入数据是无序的, 需要做sort()排序
# 如果输入数据已经排好序了, 即数组是有序的, 用双指针算法比哈希表算法(哈希算法的时间复杂度和空间复杂度都是O(n))要好, 不用排序的话其时间复杂度降为O(n), 空间复杂度O(1)   
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        
        # O(nlog(n))
        numbers.sort()

        # O(n)
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target: 
                # 数组排序后, 如果最小数+最大数大于target, 那么右指针指向的最大数加谁都会大于target, 所以应该把其跳过看其他元素
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else: # 此时numbers[left]+number[right]=target
                return numbers[left], numbers[right]
        
        return [-1, -1]

# 求索引, 双指针+排序算法: Two Sum 题的排序解法：排序保证能用双指针查找；取出原始索引保证答案符合题目要求。
#时间复杂度: 有序数组O(n), 无序数组:O(n log n); 空间复杂度O(n), 因为新建了一个 num 列表
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        
        # 新生成一个nums 是一个 列表 (list), 里面的每个元素是一个二元元组 (tuple), 即 nums = [(值, 索引), (值, 索引), ...]。
        nums = [
            (number, index) # 圆括号里的 (number, index) 是元组 (tuple)，不是数组 (list)
            for index, number in enumerate(numbers) # 这里把 enumerate 解包成 index, number，然后再交换顺序存成 (number, index)
        ]
        # 上述语句等价于
        # nums = []
        # for index, number in enumerate(numbers):
        #     nums.append((number, index))

        # 把 (数值, 索引) 按数值升序排列，方便双指针。
        # Python 的元组比较规则：先比第一个元素，若相等再比第二个。eg: [(10, 0), (20, 1), (30, 2)]
        nums.sort()


        left, right = 0, len(numbers) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target: 
                # 数组排序后, 如果最小数+最大数大于target, 那么右指针指向的最大数加谁都会大于target, 所以应该把其跳过看其他元素
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                return sorted(nums[left][1], nums[right][1]) # 把找到的两个数的原始索引按升序返回
        
        return [-1, -1]

# 求索引, 穷举法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): # i + 1 表示循环的起始索引（也就是“从 i 的下一个位置开始”). 
                # range(start, stop), 表示生成一个从 start 到 stop - 1 的整数序列。
                if nums[i] + nums[j] == target:
                    return [i, j]
            return []



# @lc code=end




#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

