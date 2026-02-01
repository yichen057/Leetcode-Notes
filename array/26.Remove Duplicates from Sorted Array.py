#
# @lc app=leetcode id=26 lang=python3
# @lcpr version=30202
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (61.00%)
# Likes:    17472
# Dislikes: 20067
# Total Accepted:    6.7M
# Total Submissions: 11M
# Testcase Example:  '[1,1,2]'
#
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same. Then return the
# number of unique elements in nums.
# 
# Consider the number of unique elements of nums to be k, to get accepted, you
# need to do the following things:
# 
# 
# Change the array nums such that the first k elements of nums contain the
# unique elements in the order they were present in nums initially. The
# remaining elements of nums are not important as well as the size of nums.
# Return k.
# 
# 
# Custom Judge:
# 
# The judge will test your solution with the following code:
# 
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# 
# int k = removeDuplicates(nums); // Calls your implementation
# 
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
# ⁠   assert nums[i] == expectedNums[i];
# }
# 
# 
# If all assertions pass, then your solution will be accepted.
# 
# 
# Example 1:
# 
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements
# of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
# 
# 
# Example 2:
# 
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
# 
# 
#

# @lc code=start
# 这段代码的核心思想是 双指针： i：扫描数组, j：写入新位置
# 时间复杂度：O(n) （只遍历一次); 空间复杂度：O(1) （原地修改）
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # j 指针表示“下一个不重复元素要放的位置”。初始化为 1，因为第一个元素 nums[0] 一定是保留的。
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j]=nums[i]
                j+=1
        # 如果 nums[i] 和前一个 nums[i-1] 不相等，说明这是一个新元素, 把它放到 nums[j] 位置。
        # 然后 j++，指向下一个可以写入的位置。
        # 如果相等（说明是重复元素），就跳过，不写入。
        return j # 遍历完成后，前 j 个元素就是去重后的结果。j 就是新数组的长度。
        
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

